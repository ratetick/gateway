import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv, erf
y = np.linspace(0, 2, 200)
fig, ax = plt.subplots()
ax.plot(y, np.sqrt(y)*(2.6+.4*np.sqrt(y))*erfinv(-.3+np.exp(-y)))
ax.grid(True)
ax.set_xlabel('t')
ax.set_title('')
plt.show()
