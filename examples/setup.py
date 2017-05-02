from setuptools import setup, Extension
from Cython.Build import cythonize

import threefry

setup(
    ext_modules=cythonize(Extension('use_threefry', ["use_threefry.pyx"], include_dirs=[threefry.get_include()]))
)
