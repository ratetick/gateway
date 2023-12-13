# import math
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import math
import json 


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


def find_value(i, bound, Path, Term,Step):

    for k in range(int(math.exp(-i / Step) * (1 - math.exp(-1 / Step)) * NPATH)):
        bound[i] = find_max(Path, Term)


NPATH = 100000
INT = 1000
sec=2
bound = [0] * (sec*INT)
Path = [0] * NPATH
Terminated = [0] * NPATH

sigma=1/np.sqrt(1000)

for i in range(sec*INT):
    for j in range(NPATH):
        if Terminated[j] == 0:
            Path[j] += random.normal(loc=0, scale=sigma)

    find_value(i, bound, Path, Terminated,INT)

jbound=json.loads(bound)
wfile=open("expo.json","w")
print(json.dumps(jbound,indent=2),wfile)
plot_myfun(bound)
