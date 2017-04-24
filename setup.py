from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name="cydtw",
    description = "DTW computation made efficient using Cython",
    ext_modules=cythonize("cydtw.pyx"),
    include_dirs=[numpy.get_include()],
    install_requires=['Cython', 'numpy', 'scipy'],
    version="0.1.3.2",
    url="https://github.com/rtavenar/cydtw",
    author="Romain Tavenard",
    author_email="romain.tavenard@univ-rennes2.fr"
)
