import json
import numpy as np


def apply_calibration(calibration_filename, image_matrix):
    calibration_info = {}

    with open(calibration_filename, "r") as f:
        calibration_info = _read_calibration_info(f)

    calibration_spacing = calibration_info["calibration_spacing"]
    calibration_vector = calibration_info["calibration_vector"]

    target_vector_size = image_matrix.shape[1]
    interpolated_vector = _interpolate_vector(calibration_vector,
                                              calibration_spacing,
                                              target_vector_size)

    return _calibrate_matrix(image_matrix, interpolated_vector)


def _read_calibration_info(fd):
    return json.load(fd)["calibration_info"]


def _calibrate_matrix(matrix, interpolated_vector):
    return np.sqrt(matrix * interpolated_vector**2)


def _interpolate_vector(vector, spacing, target_size):
    return np.interp(range(target_size),
                     range(0, target_size, spacing),
                     vector)
