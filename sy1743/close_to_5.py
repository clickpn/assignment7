import numpy as np
# Author: Sida Ye
# DS-GA 1007 HW7
# Question 3


def close_to_5():

    """
    The function would return a 1-D array containing 10 values.
    Each value is the number closest to 0.5 from the corresponding row
    of the original array.
    """

    np.random.seed(1234)                            # set seed
    rand_mat = np.random.rand(10, 3)                # uniform in [0,1]
    x = np.repeat(0.5,30).reshape(10,3)             # create a matrix contains 0.5 with shape as 10x3
    sorted_mat = np.argsort(np.abs(rand_mat - x))   # sorted the number in each row
    target = sorted_mat[:, 0]                       # use fancy index
    result = []
    for i in range(rand_mat.shape[0]):
        result.append(np.around(rand_mat[i][target[i]], 5))
    return np.array(result)


