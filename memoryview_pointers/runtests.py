import numpy

from memoryview_pointers.matvec import matvec

A = numpy.array([[1,2,3],[4,5,6],[7,8,9]], dtype=numpy.double)
x = numpy.array([0.5,0.2,0.1], dtype=numpy.double)

y_numpy = numpy.dot(A,x)
print 'Numpy:'
print y_numpy

y_cython = matvec(A,x)
print '\nCython:'
print y_cython


