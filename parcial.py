import numpy as np 
import random as rd 
import sys
import matplotlib.pyplot as plt

e = np.e

def ejercicio_3(N= 10000,n = 100):
    # suma e^i/N ~~ integral de e ^ x en 0,1 pues  i(1-0)/N ~~ x
    g = lambda x : e**x 
    G = []
    for i in range(n):
        U = rd.uniform(0,1)
        G.append(g(U))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    print(THETA[-1])    
#Transformada inversa

pi = np.pi


def e_1(n=10,N=100):
    # f = e^-x   F= 1-e^-x
    q = lambda x : 1 - e**(-x)
    p = lambda x : (e**(-x**2)/2)/(2*pi)**0.5 
    c = 2
    X = []
    for cont in range(N):
        U1 = rd.uniform(0,1)
        Y = 0
        for i in range(n):
            if U1 <= q(i):
                Y = i 
                break
        U2 = rd.uniform(0,1)
        if U2 <= p(Y)/(c*q(Y)):
            X.append(Y)
    print(X)

def e_3(n = 100 , N =10000):
    #U = F(x) = e**(x/N)
    X = []
    for i in range(n):
        U = rd.uniform(0,1)
        x = -N*np.log(U)
        X.append(x)
    print(X)

def e_4():
    print()
def e_2():
    print()
    # alpha P(x1) +(1-alpha)P(x2)
    # p (1-p)^n-1
if __name__=='__main__': 
    #ejercicio_3()
    e_1()
    e_3()
