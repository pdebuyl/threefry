from libc.stdint cimport uint64_t

cdef extern from "threefry.h":
    ctypedef struct threefry_t:
        uint64_t c0
        uint64_t c1

    uint64_t threefry_uint64(threefry_t *c, threefry_t *k)
    double threefry_double(threefry_t *c, threefry_t *k)

cdef class rng:
    cdef threefry_t counter
    cdef threefry_t key
    cdef bint has_gaussian
    cdef double gaussian_store

    cpdef set(self, counter, key)

    cpdef uint64_t random_uint64(self)
    cpdef double random_uniform(self)
    cpdef double random_normal(self)
