#!/usr/bin/env python3

import json
import numpy as np
import sys

try:
    import image_matrix_calibration as calibration
except ImportError:
    from src import image_matrix_calibration as calibration


def calibrate_image_matrix():
    calibration_filename = sys.argv[1]
    image_matrix_filename = sys.argv[2]
    image_matrix = []

    with open(image_matrix_filename, "r") as f:
        image_matrix = np.array(json.load(f))

    calibrated_matrix = calibration.apply_calibration(calibration_filename,
                                                      image_matrix)
    print(json.dumps(calibrated_matrix.tolist()))


usage = f"""{__file__} <calibration_filename> <image_matrix_filename>
"""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        exit(2)

    calibrate_image_matrix()
