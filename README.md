# Calibration Vector Application

This repository contains code that provides a solution to a recruitment test provided by Planet.  
The test description can be found [here](doc/test-description.md).


## Comments

### Difficulties

While completing this assignment, the biggest difficulty was finding documentation for the python `gdal` module, for example regarding how to pass the `COMPRESS=LZW` option, or about whether there was an equivalent to `GDALClose()` that needed to be called after writing to the image file.  
In the end, StackOverflow was my most useful resource, as is so often the case.

### Documentation

For docstrings, I have copied the format used by `pandas`, but I'm not sure it's very standard and I haven't tried parsing it with a tool to ensure the output is what I expect. I might try reStructuredText next time.

### Conda create package

I wanted to create a conda module using `conda-build`, because I could then specify conda packages `gdal` and `numpy` as dependencies of my module. However, I ran into the error described in (https://github.com/conda/conda-build/issues/1502)[https://github.com/conda/conda-build/issues/1502], due to the fact that I have an encrypted HOME. I did not take the time to fix this by installing miniconda on a non-encrypted part of my drive, opting instead to provide a `setup.py` file, and asking for it to be run in a conda environment that already contains the dependencies.

### Assumptions

I have made a few assumptions regarding the input data:
- Calibration spacing is an integer
- Matrix contains only positive numbers

### Future work

I see several ways of improving this code:
- Provide instructions to package the code using `conda`
- Add exception handling in case bad input is provided
- Allow image transformations, for example using larger pixels if the image is too small
- In general, hard-coding less in the script to generate the image, to make it more flexible
- Provide a Dockerfile, for people who prefer having `docker` as their single dependency rather than `conda`. 


## Prerequisites

### Conda environment

Running the code requires `numpy` and `gdal`, and running the tests also requires `nose`. An _environment.yml_ file is provided for installing the dependencies with `conda`.  
Create the `planet-test` conda environment from the provided _environment.yml_ file:
```sh
conda env create -f environment.yml
```


### Install module

In the created conda environment, install the `image_matrix_calibration` module:
```sh
source activate planet-test
python setup.py install
```


## Command-line tools

### Image matrix calibration
A command-line wrapper around the `image_matrix_calibration` module is provided. It can be used as follows to generate a calibrated matrix and store it in a json file; example files are provided in the _example_data_ folder:
```sh
python calibrate_image_matrix.py example_data/calibration_params.json example_data/image_matrix.json > calibrated_image_matrix.json
```


### TIFF Image generation

To visualize the output matrix, the `generate_image_from_matrix` command-line tool is provided. It first scales all the pixel values to fill the range [0; 255], then uses the `gdal` module to create an image with 3 bands, compressed with LZW and whose values are unsigned ints. The transformations done to obtain the various bands are arbitrary. The tool can be used as follows:
```sh
python generate_image_from_matrix.py calibrated_image_matrix.json image.tif
```


This is the (zoomed in) resulting image:  
![](doc/image.tif)


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
