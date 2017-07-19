Using threefry from Cython
==========================

The goal of threefry is to be usable equally from Python and from Cython.

An example is provided in `threefry's repository
<https://github.com/pdebuyl/threefry/tree/master/examples>`_ and is reproduced below.

The result is that the calls to the RNG are much faster than the corresponding Python
version. To actually build the example, have a look at the corresponding setup file in the
repository.

.. code:: cython

    cimport threefry
    import numpy as np

    def n_normal(seed, int n):
	cdef threefry.rng r = threefry.rng(seed)
	cdef int i
	cdef double[:] result = np.empty(n)
	for i in range(n):
	    result[i] = r.random_normal()

	return np.asarray(result)

