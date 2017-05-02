import numpy as np
cimport numpy as np
from libc.math cimport sqrt, log
from libc.stdint cimport uint64_t

cdef class rng:
    def __cinit__(self):
        pass

    cpdef set(self, counter, key):
        self.counter.c0 = counter
        self.counter.c1 = 0
        self.key.c0 = key[0]
        self.key.c1 = key[1]

    def __init__(self, key1, key2=None):
        if key2==None:
            key2 = 0

        self.set(0, (key1, key2))
        self.has_gaussian = False

    cpdef double random_uniform(self):
        return threefry_double(&self.counter, &self.key)

    cpdef double random_normal(self):
        cdef int i
        cdef double x
        cdef double u1, u2, radius
        cdef bint found

        if self.has_gaussian:
            self.has_gaussian = False
            return self.gaussian_store
        else:
            found = False
            while not found:
                u1 = 2*self.random_uniform() - 1
                u2 = 2*self.random_uniform() - 1
                radius = (u1**2+u2**2)
                if ( ( radius < 1 ) and (radius > 0) ): found = True
            self.gaussian_store = u1 * sqrt( -2 * log(radius)/radius )
            self.has_gaussian = True

        return u2 * sqrt( -2 * log(radius)/radius )

    def status(self):
        print(self.counter.c0)
        print(self.counter.c1)
        print(self.has_gaussian)
        print(self.gaussian_store)
