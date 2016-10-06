import numpy as np


def load_spectrum(filepath):
    spectrum = np.loadtxt(filepath)
    realpart = spectrum[:, 0]
    imagpart = spectrum[:, 1]
    return realpart, imagpart


def flock_size(flockpath):
    with open(flockpath) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def load_flock(flockpath):
    flock = open(flockpath, 'r')
    nf = flock_size(flockpath)
    for nummatrices, specpath in enumerate(flock):
        specpath = specpath.rstrip('\n')
        specpath += '.spectrum'
        realpart, imagpart = load_spectrum(specpath)
        if nummatrices == 0:
            ne = len(realpart)
            freal = np.empty([ne, nf])
            fimag = np.empty([ne, nf])
        freal[:,nummatrices] = realpart
        fimag[:,nummatrices] = imagpart
        print('- spectrum ' + str(nummatrices+1) + ' of ' + str(nf) + ' loaded:' + specpath)
    return nf, ne, freal, fimag