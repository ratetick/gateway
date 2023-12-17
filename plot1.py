import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv, erf
import json

y = np.linspace(0, 2, 200)
fig, ax = plt.subplots()
ax.plot(y, np.sqrt(y)*erfinv(np.exp(-y)-1))
ax.grid(True)
ax.set_xlabel('t')
ax.set_title('')
plt.show()
