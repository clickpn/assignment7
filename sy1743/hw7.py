# DS-GA 1007 HW7
# Author: Sida Ye

import numpy as np


### Question 1
def make_2D_arrary(m, n, start, end):
    result = np.zeros(shape=(m, n))
    i = 0
    while i < m:
        result[i] = np.linspace(start+i, end+1+i-m, n)
        i = i + 1
    return result

print make_2D_array(5,3,1,15)

#a
print make_2D_array(5,3,1,15)[[1,3], ]

#b
print make_2D_array(5,3,1,15)[:, 1]

#c
print make_2D_array(5,3,1,15)[1:4,:3]

#d
print make_2D_array(5,3,1,15)

a = np.arange(1,16).reshape(3, 5)
a.transpose()



### Question 2
a = np.arange(25).reshape(5, 5)
b = np.array([1., 5, 10, 15, 20])

def matrix_divide(mat1, mat2):
    result = np.zeros(shape=(5,5))
    for i in range(mat1.shape[1]):
        result[:, i] = mat1[:, i] / mat2
    return result

print matrix_divide(a,b)

### Question 3

np.random.seed(1234)
rand_mat = np.random.rand(10, 3)    # uniform in [0,1]
x = np.repeat(0.5,30).reshape(10,3)
sorted_mat = np.argsort(np.abs(rand_mat - x))
target = sorted_mat[:, 0]
result = []
for i in range(rand_mat.shape[0]):
    result.append(rand_mat[i][target[i]])
print np.array(result)

### Question 4
import matplotlib.pyplot as plt
import numpy as np
 
def mandelbrot(x, y):
    N_max = 50
    some_threshold = 50
    c = x + 1j*y
    z = c
    for v in range(N_max):
        z = z**2 + c
        if abs(z) >= some_threshold:
            return False
    return True
 
X = np.arange(-2, 1, .005)
Y = np.arange(-1.5,  1.5, .005)
mask = np.zeros((len(X), len(Y)))
 
for iy, itemy in enumerate(Y):
    for ix, itemx in enumerate(X):
        mask[iy,ix] = mandelbrot(itemx, itemy)
 
plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')
plt.show()











