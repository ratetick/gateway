import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv, erf
import json
fr=open("expo.json",'r')
data_graph=json.load(fr)
a=2.6
b=.4
c=-.3
error=0
denom=1000
i=0
for y in data_graph:
    error+=(y- np.sqrt(i/denom)*(a+b*np.sqrt(i/denom))*erfinv(-.3+np.exp(-i/denom)))**2
    i+=1

print(np.sqrt(error/i))