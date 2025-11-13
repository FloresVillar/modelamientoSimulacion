import numpy as np
import matplotlib.pyplot as plt
from numpy import random

x_media=np.array([],dtype=np.float64);s2_var=np.array([],dtype=np.float64)
x_media=np.append(x_media,np.exp(np.random.rand()));x_media=np.append(x_media,x_media + (np.exp(np.random.rand()) - x_media)/(1+1))
s2_var=np.append(s2_var,0); s2_var=np.append(s2_var, (1-1/1)*s2_var+(1+1)*(x_media[1] - x_media[0])**2)
j=1
while (np.sqrt(s2_var[j]/j) >= 0.02):
  x_media=np.append(x_media, x_media[j] + (np.exp(np.random.rand()) - x_media[j])/(j+1))
  s2_var=np.append(s2_var, (1-1/j)*s2_var[j]+(j+1)*(x_media[j+1] - x_media[j])**2)
  j = j + 1

n=len(x_media)
print(n)
n_=range(1,n+1)
print(x_media[n-1]) # imprime utlimo valor estimado
value_exp=np.repeat(1.7182,n)
plt.plot(n_,x_media)
plt.plot(value_exp)
plt.show()
