import numpy as np
import matplotlib.pyplot as plt
import make_2D_array as m2day
import matrix_divide as md
import close_to_5 as cl5
import mandelbrot as mand
from mandelbrot import *



# Author: Sida Ye
# DS-GA 1007 HW7
# Main program

""" This is the main program to generate answer for assignment7 """

try:
    # Question 1

    #a
    print "\n The answer of Question 1, (a) is"
    print m2day.make_2D_array(5, 3, 1, 15)[[1, 3], ]

    #b
    print "\n The answer of Question 1, (b) is"
    print m2day.make_2D_array(5, 3, 1, 15)[:, 1:2]

    #c
    print "\n The answer of Question 1, (c) is"
    print m2day.make_2D_array(5, 3, 1, 15)[1:4, :3]

    #d
    print "\n The answer of Question 1, (d) is"
    print m2day.make_2D_array(5, 3, 1, 15).T.reshape(1,15)[0][2:11]

    # Question 2
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    print "\n The answer of Question 2 is"
    print md.matrix_divide(a,b)

    # Question 3
    print "\n The answer of Question 3 is"
    print cl5.close_to_5()

    # Question 4
    print "\n Generating plot.........."
    mask = mand.mandelbort_set(-2, 1, -1.5, 1.5)
    print "\n The plot of question 4 is saved as 'mandelbrot.png' in the current dictory."
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

except KeyboardInterrupt, ValueError:
    print "\n Interrupted!"
except TypeError:
    print "\n Type Wrong!"
except EOFError:
    print "\n Interrupted!"

