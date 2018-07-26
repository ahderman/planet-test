# Calibration Vector Application - Test Description

## Problem

In order to create more perfect pixels, we often apply operation to imagery such as
downsampling, noise removal, and calibration. Imagery can be thought of as an m by n
2­-dimensional array, or as a matrix. Each operation is defined by a function which takes a single
value, list, or matrix of values and applies that to each pixel in the image.

One image operation we perform is to apply a calibration vector to an image, in order to
compensate for the satellite sensor characteristics. A single entry with v values needs to be read
and applied to the image, where each row of the image has m pixels ( m ≥ v ≥ 1). Note that if v <
m, the calibration vector needs to be interpolated.

The calibration vector will be a JSON file in the form of:

```json
{
    "calibration_info": {
        "calibration_spacing": 2,
        "calibration_vector": [0.65, 0.7, 0.75]
    }
}
```

Where ```calibration_spacing``` denotes how far away each sample is in the vector (a spacing
of 1 means that the vector is not sub­sampled) and ```calibration_vector``` is the list of
calibration coefficients that need to be applied to the pixels in the image.

The calibration formula is Γ² = γ * α² where Γ is the calibrated matrix, γ is the uncorrected
matrix, and α is the calibration vector. Note that α and γ must share the same dimension (if the
matrix of pixels is m by n , then α must be length m ).

A sample 5 by 6 matrix γ is given below:
```json
[[7.10059172, 6.58436214, 6.12244898, 5.70749108, 5.33333333],
[26.03550296, 24.14266118, 22.44897959, 20.9274673, 19.55555556],
[73.37278107, 68.03840878, 63.26530612, 58.97740785, 55.11111111],
[163.31360947, 151.44032922, 140.81632653, 131.27229489, 122.6666667],
[2.36686391, 2.19478738, 2.04081633, 1.90249703, 1.77777778],
[49.70414201, 46.09053498, 42.85714286, 39.95243757, 37.33333333]]
```

## Solution

Please provide your Python solution which will perform the above-described calibration
correction to an image. At a minimum, provide a method which has the following signature:
```python
def apply_calibration(calibration_filename, image_matrix):
    # Your code here
    return calibrated_image_matrix
```

Your solution can be the necessary Python module(s) themselves, a Vagrant/Docker/Virtualenv
solution, and anything else you feel necessary to complete and code the challenge. Please
provide all files necessary to run your code, and a readme file with instructions.

You may use any third-party libraries you wish. This code should be reflective of production
code, so should contain some tests, comments, and should conform to PEP8 standards. It can
be Python 2 or Python 3 compatible, or both. Feel free to send a compressed archive (e.g. zip,
tgz) of the code or a public link to the code (e.g. on GitHub, Gitlab, etc.)

## Extras
As the domain we are in is image processing, a matrix by itself is not extremely useful. An
optional extra credit is to write out the matrix into an image using GDAL, the Geospatial Data
Abstraction Library. http://gdal.org

Your image should be a TIFF with LZW compression, with multiple bands, 8­bit unsigned int.
(The calibrated image data should be scaled to 8­bit values before being written). Each band
can simply have the calibrated image data. If you want, you can shift or modify the data that will
be written to each band in order to see something more than just a grayscale image!
