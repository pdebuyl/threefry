cimport threefry
import numpy as np

def n_normal(seed, int n):
    cdef threefry.rng r = threefry.rng(seed)
    cdef int i
    cdef double[:] result = np.empty(n)
    for i in range(n):
        result[i] = r.random_normal()
    
    return np.asarray(result)

