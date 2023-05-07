import numpy as np
from pyspark.ml.linalg import Vectors

def t(x, a):
    return np.sign(x) * np.max(abs(x) - a, 0)

# Solving M sub-problems
def coordinate_descent(partition,w,z,beta,lmbd):
    delta_beta = np.zeros(len(beta))
    for row in partition:
        x_j = Vectors.dense(row[:-1])  # -1 not take the feature_id
        q = z + beta[row[-1]]*x_j  # to be checked
        delta_beta[row[-1]] = t(np.sum(w * x_j * q), lmbd) / np.dot(w, x_j**2) - beta[row[-1]]
    yield delta_beta