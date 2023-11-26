# import math
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import math


def cmu(t: float):
    return 1 - math.exp(-t)


def plot_myfun(fun: list):
    plt.plot(range(len(fun)), fun)
    plt.show()


def find_max(i, Win, Term):
    max = -10000
    index = 0
    for j in range(NPATH):
        if Term[j] == 0:
            if max < Win[j][i]:
                max = Win[j][i]
                index = j
    Term[index] = 1
    return max


def find_value(i, bound, Win, Term):
    # print(int(math.exp(-i / n) * (1 - math.exp(-1 / n)) * NPATH))

    for k in range(int(math.exp(-i / n) * (1 - math.exp(-1 / n)) * NPATH)):
        bound[i] = find_max(i, Win, Term)


n = 200
T = 2
NPATH = 100000
INT = n * T
bound = [0] * (INT)
# generating Winner passes

Winner = []
Terminated = []
for i in range(NPATH):
    path = []
    for j in range(INT):
        if j > 0:
            path.append(path[j - 1] + random.normal(loc=0, scale=1))
        else:
            path.append(random.normal(loc=0, scale=1))
    Winner.append(path)
    Terminated.append(0)

for i in range(INT):
    find_value(i, bound, Winner, Terminated)

plot_myfun(bound)
print(bound)
