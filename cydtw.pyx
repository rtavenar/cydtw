import numpy
from scipy.spatial.distance import cdist

cimport numpy
DTYPE = numpy.float
ctypedef numpy.float_t DTYPE_t
# "def" can type its arguments but not have a return type. The type of the
# arguments for a "def" function is checked at run-time when entering the
# function.
cimport cython
@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def dtw(numpy.ndarray[DTYPE_t, ndim=2] s1, numpy.ndarray[DTYPE_t, ndim=2] s2):
    assert s1.dtype == DTYPE and s2.dtype == DTYPE
    # The "cdef" keyword is also used within functions to type variables. It
    # can only be used at the top indentation level (there are non-trivial
    # problems with allowing them in other places, though we'd love to see
    # good and thought out proposals for it).
    cdef int l1 = s1.shape[0]
    cdef int l2 = s2.shape[0]
    cdef int i = 0
    cdef int j = 0
    cdef int argmin_pred = -1
    cdef numpy.ndarray[DTYPE_t, ndim=2] cross_dist = cdist(s1, s2, "sqeuclidean").astype(DTYPE)
    cdef numpy.ndarray[DTYPE_t, ndim=2] cum_sum = numpy.zeros((l1 + 1, l2 + 1), dtype=DTYPE)
    cum_sum[1:, 0] = numpy.inf
    cum_sum[0, 1:] = numpy.inf
    cdef DTYPE_t pred = 0.
    for i in range(l1):
        for j in range(l2):
            cum_sum[i + 1, j + 1] = min(cum_sum[i, j + 1], cum_sum[i + 1, j], cum_sum[i, j]) + cross_dist[i, j]
    return numpy.sqrt(cum_sum[l1, l2])