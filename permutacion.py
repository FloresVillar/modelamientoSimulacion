import numpy as np 
import random as rd 

def max_entero(num):
    cadena =str(num)
    print(cadena)
    cadena = cadena.split(".")
    print(cadena)
    e = int(cadena[0])
    return e
def permutacion(n=10):
    """
    seguir los pasos del algoritmo
    """
    P = []
    for i in range(n):
        P.append(i)
    #print(P)
    k = n-1
    while(k>1):
        U = rd.uniform(0,1)
        print(U)
        print(U*k)
        i = max_entero(U*k) + 1
        aux = P[i]
        P[i] = P[k]
        P[k] = aux
        k = k - 1 
    print(P) 

if __name__=='__main__':
    permutacion()