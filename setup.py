try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import src.image_matrix_calibration as image_matrix_calibration

setup(
    name="image_matrix_calibration",
    version=image_matrix_calibration.version,
    description=image_matrix_calibration.__doc__.split("\n")[0],
    long_description=image_matrix_calibration.__doc__,
    author="Alexandre D'Erman",
    author_email="alex.derman@gmail.com",
    url="https://github.com/ahderman/planet-test",
    py_modules=["src.image_matrix_calibration"],
    license="MIT",
)
