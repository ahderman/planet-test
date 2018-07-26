# Calibration Vector Application

This repository contains code that provides a solution to a recruitment test provided by Planet.  
The test description can be found [here](test-description.md).

## Prerequisites

Running the code requires `numpy`, and running the tests also requires `nose`. An _environment.yml_ file is provided for installing the dependencies with `conda`.  
Create the `planet-test` conda environment from the provided _environment.yml_ file:
```sh
conda env create -f environment.yml
```


## Command-line tool

A command-line wrapper around the calibration module is provided. It can be used as follows:
```sh
python calibrate_image_matrix.py calibration_params.json image_matrix.json
```

This assumes that the files _calibration_params.json_ and _image_matrix.json_ are formatted as follows:

_calibration_params.json_
```json
{
    "calibration_info": {
        "calibration_spacing": 2,
        "calibration_vector": [0.65, 0.7, 0.75]
    }
}
```

_image_matrix.json_
```json
[[7.10059172, 6.58436214, 6.12244898, 5.70749108, 5.33333333],
 [26.03550296, 24.14266118, 22.44897959, 20.9274673, 19.55555556],
 [73.37278107, 68.03840878, 63.26530612, 58.97740785, 55.11111111],
 [163.31360947, 151.44032922, 140.81632653, 131.27229489, 122.6666667],
 [2.36686391, 2.19478738, 2.04081633, 1.90249703, 1.77777778],
 [49.70414201, 46.09053498, 42.85714286, 39.95243757, 37.33333333]]
```


## Tests

The tests can be run with `nose`:
```sh
nosetests
```

or:
```sh
python -m nose
```


## Linting

To ensure that code is PEP8-compliant, the provided `conda` environment includes `Flake8`, which can be run with the following command:
```sh
flake8
```

or
```
python -m flake8
```


## Install and use as a library

TODO

## Future work
- Allow installing as a library via setuptools
- Add docstrings to functions
- Create TIFF with gdal
