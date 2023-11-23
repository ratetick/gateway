# import math
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import math


n = 20
m = 20
N = 100000
bound = [0] * n
dist = [0] * n

for k in range(n):
    bound[k] = -1.15 * (k - 2)  # -0.1 * k * k + 0.8*k + 1
bound[0] = -0.4
bound[1] = -1.5
bound[2] = -1.8
bound[3] = -2

xpoints = np.array(range(n))
ypoints = np.array(bound)

plt.plot(xpoints, ypoints)
plt.show()

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
    print(f'{k}={dist[k]}')

xpoints = np.array(xp)
ypoints = np.array(yp)

plt.plot(xpoints, ypoints)
plt.show()
