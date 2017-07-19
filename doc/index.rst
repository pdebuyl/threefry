.. threefry documentation master file, created by
   sphinx-quickstart on Wed Jul 19 16:06:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to threefry's documentation!
====================================

:Authors: Pierre de Buyl
:License: BSD 3-clause
:Website: http://pypi.python.org/threefry/

threefry is a random number generator proposed in the Random123 family.

This packages implements threefry in C and makes it available at the Python and Cython
levels.

Installation
------------

.. code::

    python3 -m pip install --user threefry

This will install the threefry module, include the declaration files threefry.h and
threefry.pxd that are necessary to "cimport" the module.


Contents
--------


.. toctree::
   :maxdepth: 2

   using_from_cython
   auto_examples/index

