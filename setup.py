from setuptools import setup, Extension
from Cython.Build import cythonize

VERSION = '0.1.0'

threefry_ext = cythonize(Extension("*",
                                   sources=["threefry/threefry.pyx",
                                            "threefry/_threefry.c"],
                                   extra_compile_args=['-std=c99'],
                                   ),
                         include_path=["threefry"],
                         )

with open('threefry/version.py', 'w') as version_f:
    version_f.write(
        "__version__ = '{__version__}'".format(__version__=VERSION)
    )


setup(name='threefry',
      version=VERSION,
      description='Threefry random number generator',
      author='Pierre de Buyl',
      author_email='pdebuyl@pdebuyl.be',
      url='https://pypi.python.org/pypi/threefry',
      license='BSD',
      packages=['threefry'],
      ext_modules=threefry_ext,
      setup_requires=['cython'],
      package_data={'threefry': ['__init__.pxd',
                                 'threefry.pxd', 'threefry.h']},
      )
