import math
import numpy as np
from numpy.linalg import norm


def function(x: float):
    return 3 * math.sqrt(x + 1) - math.exp(x) - 0.5


def phi(x: float):
    return function(x) + x


def der(x: float):
    # return 1.5 / math.sqrt(x + 1) - math.exp(x) + function(x) + 1
    return 3 / (6 * (x + 1) - math.sqrt(x + 1))


def fun(x: float):
    return math.log(3 * math.sqrt(x + 1) - 0.5)


def runmultiple(fun, x: float, num: int) -> float:
    if num > 0:
        return runmultiple(fun, fun(x), num - 1)
    elif num == 0:
        return x


print('f(1.5)=', function(1.5))
print('f(1.25)=', function(1.25))
print('f(1.375)=', function(1.375))
print('d(1)=', der(1))
print('d(2)=', der(2))
print('phi(1.5)', phi(1.5))
print('root=', runmultiple(fun, 1.5, 5) - runmultiple(fun, 1.5, 4))

# from sympy import symbols, solve


# x = symbols('x')
# expr = 3 * math.sqrt(x + 1) - math.exp(x) - 0.5

# print(solve(expr))

a = np.array(
    [[28, 9, -3, -7], [-5, 21, -5, -3], [-8, 1, -16, -5], [0, -2, 5, 8]]
)
b = np.array([-159, 63, -45, 24])
x = np.linalg.solve(a, b)
print(x)

aitr = np.identity(4) - np.array([a[i] / a[i][i] for i in range(4)])

aitr_norm = norm(aitr, np.infty)

bprime = np.array([b[i] / a[i][i] for i in range(4)])
n = 4
approx = [0] * n
approx[0] = bprime
for i in range(n - 1):
    approx[i + 1] = bprime + np.dot(aitr, approx[i])
    print(
        i,
        norm(approx[i + 1] - x, np.infty),
        norm(approx[i + 1] - approx[i], np.infty),
        aitr_norm**i
        / (1 - aitr_norm)
        * norm(approx[i + 1] - approx[i], np.infty),
    )
