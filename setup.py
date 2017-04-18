from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name='DTW',
    ext_modules=cythonize("dtw.pyx"),
    include_dirs=[numpy.get_include()]
)
