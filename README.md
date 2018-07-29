# Calibration Vector Application

This repository contains code that provides a solution to a recruitment test provided by Planet.  
The test description can be found [here](test-description.md).


## Prerequisites

### Conda

Running the code requires `numpy` and `gdal`, and running the tests also requires `nose`. An _environment.yml_ file is provided for installing the dependencies with `conda`.  
Create the `planet-test` conda environment from the provided _environment.yml_ file:
```sh
conda env create -f environment.yml
```


## Command-line tools

### Image matrix calibration
A command-line wrapper around the `image_matrix_calibration` module is provided. It can be used as follows to generate a calibrated matrix and store it in a json file; example files are provided in the _example_data_ folder:
```sh
python calibrate_image_matrix.py example_data/calibration_params.json example_data/image_matrix.json > calibrated_image_matrix.json
```


### TIFF Image generation

To visualize the output matrix, the `generate_image_from_matrix` command-line tool is provided. It first scales all the pixel values to fill the range [0; 255], then uses the `gdal` module to create an image with 3 bands, compressed with LZW and whose values are unsigned ints. It can be used as follows:
```sh
python generate_image_from_matrix.py calibrated_image_matrix.json image.tif
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


## Future work
- Allow installing as a library via setuptools
- Exception handling in case bad input is provided
- Allow image transformations, for example using larger pixels if the image is too small
- Provide a Dockerfile


## Assumptions
- Calibration spacing is an integer
- Matrix contains only positive numbers


## Difficulties

While completing this assignment, the biggest difficulty was finding documentation for the python `gdal` module, for example regarding how to pass the `COMPRESS=LZW` option, or about whether there was an equivalent to `GDALClose()` that needed to be called after writing to the image file.  
In the end, StackOverflow was my most useful resource, as is so often the case.
