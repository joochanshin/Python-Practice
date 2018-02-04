from math import *
from complex import Complex

c = Complex(-2, 1)

def z (n, c):
    c = trunc(c)
    if n == 0:
        '''
        print "In if statement"'''
        return 0
    else:
        '''print "In else statement"
        print "mandel: ", mandelbrot(c, z-1)
        print "c: ", c'''

        return z(n-1, c)**2 + c


print z(10, c)


