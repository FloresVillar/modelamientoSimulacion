##### Metodo Composicion
import numpy as np
import matplotlib.pyplot as plt
import random

k=10000
x=np.zeros(k)
for j in np.arange(len(x)):
  u=np.random.rand(1) 
  if u<=0.5:
    x[j]=np.floor(10*np.random.rand())+1
  else:
    x[j]=np.floor(5*np.random.rand())+1+5

pesos_=np.zeros(10)
for j in np.arange(len(pesos_)):
  pesos_[j]=x.tolist().count(j+1)

plt.bar(np.arange(10)+1,pesos_/len(x),width = 0.4)
print(pesos_/len(x))