# test case

import unittest
from unittest import TestCase
import numpy as np
import matplotlib.pyplot as plt
import make_2D_array as m2day
import matrix_divide as md
import close_to_5 as cl5
import mandelbrot as mand
from mandelbrot import *

"""test answer in different modules"""

class interval_unittest(unittest.TestCase):

    def setUp(self):
        pass

    # Question1 Answer Test

    def test_Q1_a(self):
        a = m2day.make_2D_array(5, 3, 1, 15)[[1, 3], ]
        b = np.array([[2., 7., 12.],[4., 9., 14.]])
        self.assertTrue(np.array_equal(a,b))

    def test_Q1_b(self):
        a = m2day.make_2D_array(5, 3, 1, 15)[:, 1]
        b = np.array([  6., 7., 8., 9., 10.])
        self.assertTrue(np.array_equal(a,b))

    def test_Q1_c(self):
        a = m2day.make_2D_array(5, 3, 1, 15)[1:4, :3]
        b = np.array([[2., 7., 12.], [3., 8., 13.], [4., 9., 14.]])
        self.assertTrue(np.array_equal(a,b))

    def test_Q1_d(self):
        a = m2day.make_2D_array(5, 3, 1, 15).T.reshape(1,15)[0][2:11]
        b = np.array([3., 4., 5., 6., 7., 8., 9., 10., 11.])
        self.assertTrue(np.array_equal(a,b))

    # Question2 Answer Test

    def test_Q2(self):
        a = np.arange(25).reshape(5, 5)
        b = np.array([1., 5, 10, 15, 20])
        c = md.matrix_divide(a,b)
        d = np.array([[ 0., 1., 2., 3., 4.], 
                      [1., 1.2, 1.4, 1.6, 1.8], 
                      [1., 1.1, 1.2, 1.3, 1.4], 
                      [ 1., 1.067, 1.133, 1.2, 1.267], 
                      [ 1., 1.05, 1.1, 1.15, 1.2]])
        self.assertTrue(np.array_equal(c,d))

    # Question3 Answer Test

    def test_Q3(self):
        a = cl5.close_to_5()
        b = np.array([0.43773, 0.27259, 0.27646, 0.501, 0.37025, 0.50308,
                      0.36489, 0.6154, 0.3972, 0.5681])
        self.assertTrue(np.array_equal(a,b))

if __name__ == '__main__':
    unittest.main()
