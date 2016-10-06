import scipy.io as scio


def read_matrix_market(filename):
    return scio.mmread(filename)