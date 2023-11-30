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


def find_max(Path, Term):
    max = -10000
    index = 0
    for j in range(NPATH):
        if Term[j] == 0:
            if max < Path[j]:
                max = Path[j]
                index = j
    Term[index] = 1
    return max


def find_value(i, bound, Path, Term):
    # print(int(math.exp(-i / n) * (1 - math.exp(-1 / n)) * NPATH))

    for k in range(int(math.exp(-i / n) * (1 - math.exp(-1 / n)) * NPATH)):
        bound[i] = find_max(Path, Term)


n = 500
T = 2
NPATH = 100000
INT = n * T
bound = [0] * (INT)
Path = [0] * NPATH
Terminated = [0] * NPATH


for i in range(INT):
    for j in range(NPATH):
        if Terminated[j] == 0:
            Path[j] += random.normal(loc=0, scale=1)

    find_value(i, bound, Path, Terminated)
print("0=", bound[0])
print("1=", bound[1])
plot_myfun(bound)
