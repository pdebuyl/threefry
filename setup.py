from setuptools import setup, Extension
from Cython.Build import cythonize

threefry_ext = cythonize(Extension("*",
                     sources=["threefry/threefry.pyx", "threefry/_threefry.c"],),
                     include_path=["threefry"],
                     )

setup(name='threefry',
      version='0.1.0.dev0',
      description='Threefry random number generator',
      author='Pierre de Buyl',
      license='BSD',
      packages=['threefry'],
      ext_modules=threefry_ext,
      setup_requires=['cython'],
      package_data={'threefry': ['__init__.pxd', 'threefry.pxd', 'threefry.h']},
      )
