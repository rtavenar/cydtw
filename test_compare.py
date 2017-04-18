import time
import numpy

import dtw_ref
import dtw

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'

n_pairs, sz = 20, 300
numpy.random.seed(0)
data1 = numpy.random.randn(n_pairs, sz, 1).astype(numpy.float)
data2 = numpy.random.randn(n_pairs, sz, 1).astype(numpy.float)

t0 = time.time()
for i in range(n_pairs):
    d = dtw.dtw_sq(data1[i], data2[i])
print("Cython computation takes %f seconds for %d DTW of length %d (dimension %d)" % (time.time() - t0, n_pairs, sz, 1))

t0 = time.time()
for i in range(n_pairs):
    d = dtw_ref.dtw_sq(data1[i], data2[i])
print("Pure python computation takes %f seconds for %d DTW of length %d (dimension %d)" % (time.time() - t0, n_pairs,
                                                                                           sz, 1))
