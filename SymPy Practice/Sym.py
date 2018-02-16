from sympy import *

x = symbols('x')
a = Integral(cos(x)*exp(x), x)
Eq(a, a.doit())