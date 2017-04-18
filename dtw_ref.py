import numpy
from scipy.spatial.distance import cdist

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def dtw_sq(s1, s2):
    cross_dist = cdist(s1.reshape((-1, 1)), s2.reshape((-1, 1)), "sqeuclidean")
    l1 = s1.shape[0]
    l2 = s2.shape[0]
    cum_sum = numpy.zeros((l1 + 1, l2 + 1))
    cum_sum[1:, 0] = numpy.inf
    cum_sum[0, 1:] = numpy.inf
    for i in range(l1):
        for j in range(l2):
            if numpy.isfinite(cum_sum[i + 1, j + 1]):
                pred_list = [cum_sum[i, j + 1], cum_sum[i + 1, j], cum_sum[i, j]]
                argmin_pred = numpy.argmin(pred_list)
                cum_sum[i + 1, j + 1] = pred_list[argmin_pred] + cross_dist[i, j]
    return numpy.sqrt(cum_sum[-1, -1])