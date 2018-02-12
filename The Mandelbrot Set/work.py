from math import *
import numpy as np
from complex import Complex


c1 = Complex(-2, 1)


def z(n, c):
    if n == 0:
        return Complex(0, 0)
    else:
        tmp = z(n - 1, c)
        return tmp * tmp + c


def accept_c(c):
    if abs(z(10, c)) > 2:
        return False
    else:
        return True


'''
print accept_c(c1)
for x in range(-2, 3):
    for y in range(-2, 3):
        print accept_c(Complex(x, y))
    print "\n"
'''
run = True
print "Welcome to the Mandelbrot Set \nEnter exit at anytime to quit."


while run:
    s = 0
    con = 0
    goFunct = True
    startX = raw_input("Enter start X point (or exit):")
    if startX == "exit":
        break
    stopX = raw_input("Enter stop X point (or exit):")
    if stopX == "exit":
        break
    startY = raw_input("Enter start Y point (or exit):")
    if startY == "exit":
        break
    stopY = raw_input("Enter stop Y point (or exit):")
    if stopY == "exit":
        break
    step = raw_input("Enter step size (or exit):")
    if step == "exit":
        break
    if startX > stopX or \
            startY > stopY or \
            step <= 0:
        goFunct = False
        print "Bad inputs. Could not render."
    else:
        s = float(step)
        if s == 1:
            con = 1
    if goFunct:
        str_ = ""
        xx = np.arange(float(startX), float(stopX) + con, s)
        yy = np.arange(float(stopY),  float(startY) - con, s * -1)
        for y in yy:
            '''print y'''
            for x in xx:
                '''print x'''
                if accept_c(Complex(x, y)):
                    str_ += "X"
                else:
                    str_ += "_"
            str_ += "\n"
        print str_
