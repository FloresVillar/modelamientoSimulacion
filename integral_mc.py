import random as rd
import numpy as np
import matplotlib.pyplot as plt

############## Calculo de probabilidad exito Lanz Moneda #########
n=100
y=[int(rd.random()>0.5) for i in range(n)]
n_=range(1,n+1)
yy=np.cumsum(y)/n_
print(yy[n-1]) # imprime utlimo valor estimado
value_exp=np.repeat(0.5,n)
plt.plot(n_,yy)
plt.plot(value_exp)
plt.show()

############## Calculo integral exp(x) de 0 a 1 ###################
n=250
y=[np.exp(rd.random()) for i in range(n)]
n_=range(1,n+1)
yy=np.cumsum(y)/n_
print(yy[n-1]) # imprime utlimo valor estimado
value_exp=np.repeat(np.exp(1)-1,n)
plt.plot(n_,yy)
plt.plot(value_exp)
plt.show()

############## Calculo integral exp(x**2 +x) de -2 a 2 ###################
n=500
y=[4*(np.exp((4*rd.random()-2)**2+(4*rd.random()-2))) for i in range(n)]
n_=range(1,n+1)
yy=np.cumsum(y)/n_
print(yy[n-1]) # imprime utlimo valor estimado
plt.plot(n_,yy)
plt.show()
 