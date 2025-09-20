import numpy as np 
import random
p=[.1,.1,.2,.02,.08,.1,.05,.05,.15,.15]
def q(x):
    return .1
def a_r():
    cocientes = []
    for i in range(10):
        cocientes.append(p[i]/q(i))
    c = max(cocientes)
    # pj/qj<=c  ó  f(x)<cg(x)
    X=[]
    i = 1
    while i<10:
        Y=  int(random.random()*10)+1#simular valor de Y con masa qj?
        u = random.random() #U(0,1)generara numero aleatorio
        if(u <= p[Y-1]/(c*q(Y))):
            X.append(Y)#aceptar...
            i = i + 1
    return X
if __name__=='__main__':
    X=a_r()
    print(X)