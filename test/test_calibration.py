import json
import numpy as np
from numpy.testing import assert_equal, \
                          assert_allclose
from calibration import _interpolate_vector, \
                        _calibrate_matrix, \
                        apply_calibration
import tempfile


def test_interpolate_vector():
    v = [0.65, 0.7, 0.75]
    spacing = 2
    target_size = 5

    expected = [0.65, 0.675, 0.7, 0.725, 0.75]
    actual = _interpolate_vector(v, spacing, target_size)
    assert_equal(actual, expected)


def test_calibrate_matrix():
    matrix = np.array([
        [7.10059172, 6.58436214, 6.12244898, 5.70749108, 5.33333333],
        [26.03550296, 24.14266118, 22.44897959, 20.9274673, 19.55555556],
        [73.37278107, 68.03840878, 63.26530612, 58.97740785, 55.11111111],
        [163.31360947, 151.44032922, 140.81632653, 131.27229489, 122.6666667],
        [2.36686391, 2.19478738, 2.04081633, 1.90249703, 1.77777778],
        [49.70414201, 46.09053498, 42.85714286, 39.95243757, 37.33333333]])

    vector = np.array([0.65, 0.675, 0.7, 0.725, 0.75])

    expected = [
        [1.73205081, 1.73205081, 1.73205081, 1.73205081, 1.73205081],
        [3.31662479, 3.31662479, 3.31662479, 3.31662479, 3.31662479],
        [5.56776436, 5.56776436, 5.56776436, 5.56776436, 5.56776436],
        [8.30662386, 8.30662386, 8.30662386, 8.30662386, 8.30662386],
        [1.,         1.,         1.,         1.,         1.],
        [4.58257569, 4.58257569, 4.5825757, 4.58257569, 4.58257569]]
    actual = _calibrate_matrix(matrix, vector)
    assert_allclose(actual, expected)


def __write_calibration_params(fd, calibration_vector, calibration_spacing):
    calibration_params = {
        "calibration_info": {
            "calibration_spacing": calibration_spacing,
            "calibration_vector": calibration_vector
        }
    }
    json.dump(calibration_params, fd)
    fd.flush()


def test_apply_calibration():
    matrix = np.array([
        [7.10059172, 6.58436214, 6.12244898, 5.70749108, 5.33333333],
        [26.03550296, 24.14266118, 22.44897959, 20.9274673, 19.55555556],
        [73.37278107, 68.03840878, 63.26530612, 58.97740785, 55.11111111],
        [163.31360947, 151.44032922, 140.81632653, 131.27229489, 122.6666667],
        [2.36686391, 2.19478738, 2.04081633, 1.90249703, 1.77777778],
        [49.70414201, 46.09053498, 42.85714286, 39.95243757, 37.33333333]])

    with tempfile.NamedTemporaryFile(mode="w") as f:
        calibration_filename = f.name
        __write_calibration_params(f, [0.65, 0.7, 0.75], 2)

        actual = apply_calibration(calibration_filename, matrix)
        expected = [
            [1.73205081, 1.73205081, 1.73205081, 1.73205081, 1.73205081],
            [3.31662479, 3.31662479, 3.31662479, 3.31662479, 3.31662479],
            [5.56776436, 5.56776436, 5.56776436, 5.56776436, 5.56776436],
            [8.30662386, 8.30662386, 8.30662386, 8.30662386, 8.30662386],
            [1.,         1.,         1.,         1.,         1.],
            [4.58257569, 4.58257569, 4.5825757, 4.58257569, 4.58257569]]
        assert_allclose(actual, expected)
