#!/usr/bin/env python3

import json
import numpy as np
import sys

from src import calibration


def main():

    calibration_filename = sys.argv[1]
    image_matrix_filename = sys.argv[2]
    image_matrix = []

    with open(image_matrix_filename, "r") as f:
        image_matrix = np.array(json.load(f))

    calibrated_matrix = calibration.apply_calibration(calibration_filename,
                                                      image_matrix)
    print(calibrated_matrix.tolist())


usage = f"""{__file__} <calibration_filename> <image_matrix_filename>
"""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        exit(2)

    main()
