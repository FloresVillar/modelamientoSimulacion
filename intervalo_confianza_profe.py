from scipy.stats import norm
import statistics as st
import numpy as np 
import matplotlib.pyplot as plt

l=0.03      ##  Longitud mínima requerida del I.C al 100(1-alpha)%
alpha=0.05 ##  error muestral máximo permitido en la estimación del I.C
x_media=np.array([],dtype=np.float64);s2_var=np.array([],dtype=np.float64)
longIC=np.array([],dtype=np.float64)
x_media=np.append(x_media,np.random.normal(0,1))
x_media=np.append(x_media,x_media + (np.random.normal(0,1) - x_media)/(1+1))
s2_var=np.append(s2_var,0)
s2_var=np.append(s2_var, (1-1/1)*s2_var+(1+1)*(x_media[1] - x_media[0])**2)
longIC=np.append(longIC,2*st.NormalDist(0,1).inv_cdf(1-alpha/2)*np.sqrt(s2_var[1]/2))

j=1
while (2*st.NormalDist(0,1).inv_cdf(1-alpha/2)*np.sqrt(s2_var[j]/j) >= l):
  x_media=np.append(x_media, x_media[j] + (np.random.normal(0,1) - x_media[j])/(j+1))
  s2_var=np.append(s2_var, (1-1/j)*s2_var[j]+(j+1)*(x_media[j+1] - x_media[j])**2)
  longIC=np.append(longIC,2*st.NormalDist(0,1).inv_cdf(1-alpha/2)*np.sqrt(s2_var[j]/2))
  j = j + 1

n_=np.arange(1,len(longIC)+1)
plt.plot(n_,longIC)
plt.show()

IC=[x_media[j]+st.NormalDist(0,1).inv_cdf(alpha/2)*np.sqrt(s2_var[j]/j),x_media[j]+st.NormalDist(0,1).inv_cdf(1-alpha/2)*np.sqrt(s2_var[j]/j)]
IC[1]-IC[0]   