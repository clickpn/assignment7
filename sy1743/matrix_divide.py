import numpy as np
# Author: Sida Ye
# DS-GA 1007 HW7
# Question 2


def matrix_divide(mat1, mat2):

    """
    matrix_divide takes two matrix or array as inputs. 
    Given mat1, it divides each column element-wise with the array b.
    """

    result = np.zeros(shape=(5,5))
    for i in range(mat1.shape[1]):
        result[:, i] = np.around(mat1[:, i] / mat2, 3)
    return result



