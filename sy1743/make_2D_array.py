import numpy as np
# Author: Sida Ye
# DS-GA 1007 HW7
# Question 1


def make_2D_array(m, n, start, end):

    """
    make_2D_array takes input of number of rows as m, number of columns as n,
    start as starting number and end as ending number.
    It will return a 2-D arrary from start number to end number with m x n shape.
    """
    
    result = np.zeros(shape=(m, n))
    i = 0
    while i < m:
        result[i] = np.linspace(start+i, end+1+i-m, n)
        i = i + 1
    return result


