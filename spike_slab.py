# Spike and Slab
import numpy as np
from scipy.stats import gamma, multinomial

def SSVS_prior_sample(w_vec, phi, r= 0.001):
    delta_vec = []
    for w in w_vec:
        delta_vec.append(np.random.choice(a = 2, p=[1-w, w]))
    delta_vec = np.asarray(delta_vec)
    print(delta_vec)
    alpha_vec = []
    for delta in delta_vec:
        alpha = np.random.normal(loc=0, scale=phi*r**(1-delta))
        alpha_vec.append(alpha)
    alpha_vec = np.asarray(alpha_vec)
    print(alpha_vec)
    return alpha_vec


def NMIG_prior_sample(w_vec, r= 0.001, a=1, scale=1):
    delta_vec = []
    for w in w_vec:
        delta_vec.append(np.random.choice(a = 2, p=[1-w, w]))
    delta_vec = np.asarray(delta_vec)
    print(delta_vec)
    alpha_vec = []
    for delta in delta_vec:
        phi = 1. / gamma.rvs(a=a, scale=scale)
        alpha = np.random.normal(loc=0, scale=phi*r**(1-delta))
        alpha_vec.append(alpha)
    alpha_vec = np.asarray(alpha_vec)
    print(alpha_vec)
    return alpha_vec


if __name__ == "__main__":
    w_vec = np.asarray([0.1, 0.1, 0.9, 0.1])
    phi = 1. / gamma.rvs(a=1, scale=1)
    alpha_vec = SSVS_prior_sample(w_vec, phi)
    alpha_vec = NMIG_prior_sample(w_vec)
