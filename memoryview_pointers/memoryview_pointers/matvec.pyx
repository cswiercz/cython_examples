import numpy
cimport numpy

cdef extern from 'matvec_doit.h':
    void matvec_doit(double*, double*, double*, int)

def matvec(double[:,:] matrix, double[:] vector):
    cdef int n = len(vector)
    cdef double[:] output = numpy.zeros(n, dtype=numpy.double)

    matvec_doit(&output[0], &matrix[0,0], &vector[0], n)

    return numpy.array(output)
