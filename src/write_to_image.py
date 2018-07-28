#!/usr/bin/env python

import gdal
import json
import numpy as np
import sys


def write_matrix_to_image(matrix_file_path, image_file_path):
    matrix = np.array([])
    nb_bands = 3

    with open(matrix_file_path, "r") as f:
        matrix = np.array(json.load(f))

    size_y, size_x = matrix.shape
    normalized_matrix = matrix / matrix.max()
    matrix_1 = np.round(normalized_matrix * 255).astype(int)
    matrix_2 = np.round(normalized_matrix * 127).astype(int)
    matrix_3 = np.round((1 - normalized_matrix) * 255).astype(int)

    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(image_file_path,
                            size_x,
                            size_y,
                            nb_bands,
                            gdal.GDT_Byte,
                            options=["COMPRESS=LZW"])
    dataset.GetRasterBand(1).WriteArray(matrix_1)
    dataset.GetRasterBand(2).WriteArray(matrix_2)
    dataset.GetRasterBand(3).WriteArray(matrix_3)


if __name__ == '__main__':
    matrix_file_path = sys.argv[1]
    image_file_path = sys.argv[2]
    write_matrix_to_image(matrix_file_path, image_file_path)
