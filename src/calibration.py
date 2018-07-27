"""
Module that allows applying calibration vectors to images.

The calibration formula is Γ² = γ * α² where Γ is the calibrated
matrix, γ is the uncorrected matrix, and α is the calibration vector.
Note that α and γ must share the same dimension (if the matrix of
pixels is m by n , then α must be length m).

If the length of α is less than m, it means that the calibration vector
vector is subsampled, and needs to be interpolated before it is
applied.
"""

import json
import numpy as np


def apply_calibration(calibration_filename, image_matrix):
    """Apply the provided calibration vector to the provided image matrix.

    Parameters
    ----------
    calibration_filename : string
        The path of the json file that describes the calibration vector.
        The expected format of this file is the following:
        {
            "calibration_info":
            {
                "calibration_spacing": int,
                "calibration_vector": float[]
            }
        }

    image_matrix : 2D numpy array
        The image matrix to calibrate.

    Returns
    -------
    Result : 2D numpy array
        The calibrated image matrix.
    """
    calibration_vector = []
    calibration_spacing = 1

    with open(calibration_filename, "r") as f:
        calibration_vector, calibration_spacing = _read_calibration_info(f)

    target_vector_size = image_matrix.shape[1]
    interpolated_vector = _interpolate_vector(calibration_vector,
                                              calibration_spacing,
                                              target_vector_size)

    return _calibrate_matrix(image_matrix, interpolated_vector)


def _read_calibration_info(fd):
    """Read calibration information from the provided stream.

    Parameters
    ----------
    fd : IO stream
        The stream should contain a json serialization of the
        calibration vector.

        The expected format of this file is the following:
        {
            "calibration_info":
            {
                "calibration_spacing": int,
                "calibration_vector": float[]
            }
        }

    Returns
    -------
    Result : tuple
        (calibration_vector, calibration_spacing).
    """
    calibration_data = json.load(fd)
    calibration_vector = (calibration_data["calibration_info"]
                                          ["calibration_vector"])
    calibration_spacing = (calibration_data["calibration_info"]
                                           ["calibration_spacing"])
    return (calibration_vector, calibration_spacing)


def _calibrate_matrix(matrix, vector):
    """Apply the calibration vector on the provided matrix.

    Parameters
    ----------
    matrix : numpy 2D array
        The intial image matrix.
    vector : numpy 1D array
        The compensation vector to apply.

    Returns
    -------
    Result : 2D numpy array
        The new matrix, with the caliration vector applied.
    """

    return np.sqrt(matrix * vector**2)


def _interpolate_vector(vector, spacing, target_size):
    """Interpolate the vector into a new one with the target size.

    Parameters
    ----------
    vector : array-like
        The vector to interpolate from.
    spacing: int
    target_size: int
        The size of the interpolated vector.

    Returns
    -------
    Result : numpy array
        The new, interpolated vector.
    """

    return np.interp(range(target_size),
                     range(0, target_size, spacing),
                     vector)
