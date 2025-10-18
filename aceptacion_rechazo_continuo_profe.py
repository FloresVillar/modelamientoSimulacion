#### Metodo A-R
k=1000
x=np.zeros(k); c=np.zeros(k)
for i in np.arange(k):
  y=-(3/2)*np.log(np.random.rand(1))
  u=np.random.rand(1);c[i]=1
  while u>(((2*np.exp(1)*y/3)**(1/2))*(np.exp(1)**(-y/3))):
    y=-(3/2)*np.log(np.random.rand(1))
    u=np.random.rand(1);c[i]=c[i]+1
  x[i]=y
plt.hist(x,bins=None,range=None,density=True)
plt.show()

np.mean(c)