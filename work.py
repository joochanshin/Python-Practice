from math import *
from complex import Complex


c1 = Complex(-1, 1j)


def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n-1, c) ** 2 + c


def accept_c(c):
    for n in range(0,10):
        if abs(z(n, c)) > 2:
            return False
    return True


print accept_c(c1)
print z(5, c1)




