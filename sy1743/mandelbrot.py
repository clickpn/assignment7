import matplotlib.pyplot as plt
import numpy as np
# Author: Sida Ye
# DS-GA 1007 HW7
# Question 4


class mandelbrot(object):

    """
    The mandelbrot function would take two values, x and y.
    If a point (x,y) belongs to the Mandelbrot set, the function will return
    true, elsewise it returns false.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.N_max = 50
        self.some_threshold = 50


def mandelbrot_check(mande):
        c = mande.x + 1j*mande.y
        z = c
        for v in range(mande.N_max):
            z = z**2 + c
            if abs(z) >= mande.some_threshold:
                return False
        return True


def mandelbort_set(xmin, xmax, ymin, ymax):

    """
    The mandelbort_set function takes four inputs, xmin, xman, ymin and y max,
    as range of x and y respectively.
    It will return a 2-D boolean mask indicating which points are in the set.
    Get help from: http://rosettacode.org/wiki/Mandelbrot_set
    """

    X = np.arange(xmin, xmax, .005)
    Y = np.arange(ymin,  ymax, .005)
    mask = np.zeros((len(X), len(Y)))
 
    for pos_y, y in enumerate(Y):           # use for loop to do interation on x and y
        for pos_x, x in enumerate(X):
            mask[pos_x,pos_y] = mandelbrot_check(mandelbrot(x, y))
    return mask






