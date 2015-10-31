import matplotlib.pyplot as plt
import numpy as np
# Author: Sida Ye
# DS-GA 1007 HW7
# Question 4


def mandelbrot(x, y):

    """
    The mandelbrot function would take two values, x and y.
    If a point (x,y) belongs to the Mandelbrot set, the function will return
    true, elsewise it returns false.
    """

    N_max = 50
    some_threshold = 50
    c = x + 1j*y
    z = c
    for v in range(N_max):
        z = z**2 + c
        if abs(z) >= some_threshold:
            return False
    return True


def mandelbort_set(xmin, xmax, ymin, ymax):

    """
    The mandelbort_set function takes four inputs, xmin, xman, ymin and y max,
    as range of x and y respectively.
    It will return a 2-D boolean mask indicating which points are in the set.
    """

    X = np.arange(xmin, xmax, .005)
    Y = np.arange(ymin,  ymax, .005)
    mask = np.zeros((len(X), len(Y)))
 
    for pos_y, y in enumerate(Y):           # use for loop to do interation on x and y
        for pos_x, x in enumerate(X):
            mask[pos_y,pos_x] = mandelbrot(x, y)
    return mask






