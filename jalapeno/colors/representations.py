"""@package jalapeno.colors.representations

How to represent colors.
"""



import numpy as np



def rgb(r, g, b, scale=255):
    """
    @param r the red component, from 0-scale
    @param g the green component, from 0-scale
    @param b the blue component, from 0-scale
    @param scale [optional=255] the scale on which the colors are provided

    Converts three numbers given in rgb order from 0-scale to a numpy array.
    The parameter scale defaults to 255, the max value in most representations of RGB colors.
    If you want to provide your RGB triple from 0-1, include scale=1 in your argument list
    """
    return np.array([r, g, b]) / scale