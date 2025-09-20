 
import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt

def generador_matriz(a=7, c=3, m=10, n=10):
  z = np.zeros((n, n))
  z[:,0] = np.arange(n)
  for j in range(n-1):
      for i in range(n):
          z[i,j+1] = (a*z[i,j] + c) % m
  return z

def generador_basico(a=137, c=0, m=256, semilla=87, N=256):
  x = np.zeros(N)
  x[0] = semilla
  for j in range(N-1):
      x[j+1] = (a*x[j] + c) % m
  u = x / m
  plt.hist(u, bins=20)
  plt.show()
  plt.plot(np.arange(N), x)
  plt.show()
  plt.plot(u[1:], u[:-1])
  plt.show()
  return x, u

def generador_grande(a=314159269, c=453806245, m=2**31-1, semilla=87, N=256):
  x = np.zeros(N)
  x[0] = semilla
  for j in range(N-1):
      x[j+1] = (a*x[j] + c) % m
  uu = x / m
  plt.plot(uu[1:], uu[:-1])
  plt.show()
  return x, uu
if __name__ == "__main__":
  #print(generador_matriz())
  #x, u = generador_basico()
  x2, uu = generador_grande()
 
