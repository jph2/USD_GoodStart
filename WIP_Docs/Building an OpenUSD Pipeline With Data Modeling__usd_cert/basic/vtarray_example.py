"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 3 (typed arrays and scalable data handling)

Why this script exists:
- It shows how USD Vt arrays connect to Python and NumPy.
- This is key for high-volume data like telemetry and point clouds.

How to run:
- From the __usd_cert folder:
  python basic/vtarray_example.py

What to expect:
1) Creation of Vt arrays from Python buffers.
2) Conversion to/from NumPy arrays.
3) A practical bridge between data science arrays and USD typing.
"""

from pxr import Vt
import numpy as np
from array import array
# Python Arrays
vt_array = Vt.Vec3hArray.FromBuffer(array("f", [1,2,3,4,5,6])) # Returns: Vt.Vec3hArray(2, (Gf.Vec3h(1.0, 2.0, 3.0),Gf.Vec3h(4.0, 5.0, 6.0),))
# From Numpy Arrays 
Vt.Vec3hArray.FromNumpy(np.ones((10, 3)))
Vt.Vec3hArray.FromBuffer(np.ones((10, 3)))
# To Numpy arrays
np.array(vt_array)