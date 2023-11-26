# import math
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import math


def cmu(t:float):
    return 1-math.exp(-t)
def plot_myfun(fun):
    xpoints=np.array(fun.lenth())
    ypoints=np.array(fun)
    plt.plot(xpoints, ypoints)
    plt.show()

def find_value(i, b):
        

n = 20
T=10
N = 1000
bound = [0] * (n*T)
 
for i in range(n*T):
    find_value(i,bound)
total = 0
for j in range(N):
    walk = 0
    for i in range(n):
        for j in range(m):
            val = random.normal(loc=0, scale=1)  # 1 if random.random() > 0.5 else -1
            walk += val / m
        if walk >= bound[i]:
            dist[i] += 1
            total += 1
            break
xp = [0] * n
yp = [0] * n
for k in range(n):
    xp[k] = k
    yp[k] = math.log(dist[k] / total)
    # yp[k]=dist[k]/total
    print(f"{k}={dist[k]}")

xpoints = np.array(xp)
ypoints = np.array(yp)

plt.plot(xpoints, ypoints)
plt.show()
