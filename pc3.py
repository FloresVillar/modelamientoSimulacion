import sys
import numpy as np 
import random as rd 
import matplotlib.pyplot as plt 
import math 
from time import time_ns

def generar_u_aleatorio(m=2**35-31,a=5**5,c=100000007):
    N = 1000
    seed = (time_ns()*104729)%m
    U = (a * seed + c ) % m
    u = []
    u.append(U)
    for i in range(N):
        Ui = (u[-1] * a + c) % m
        u.append(Ui)
    u = np.array(u)
    u = u/m
    return float(u[-1])

#generar_u_aleatorio = lambda : rd.uniform(0,1)  #los resultados son similares

def problema_de_reparacion(N=500,lam_de=1,lam_re=0.25):
    T = [] 
    Tsimulaciones = []
    for i in range(500):
        #print(f"\nsimulacion: {i+1}")
        t = 0  
        des = 0 
        t_re =  float('inf') 
        re = 4
        n = 10
        X = []
        for i in range(n):
            U = generar_u_aleatorio() 
            x = -float(np.log(U))/lam_de
            X.append(x)    
        X = np.array(X) 
        t_ord = np.sort(X)
        X = X.tolist() 
        t_ord = t_ord.tolist()
        #print(",".join(f"{x:.4f}" for x in t_ord))
        while True:
            t1 = t_ord[0]
            if t1 < t_re : # caso 1
                t = t1 ; des = des + 1
                t_ord.pop(0)
                if des == re + 1: # porque cuando hay descompostura sale 1 inmediatamente de respuestos
                    T.append(t)
                    break
                if des < re + 1:
                    U = generar_u_aleatorio()
                    x = -float(np.log(U))/lam_de
                    t_ord.append(t + x) # porque en el futuro fallará
                    t_ord = np.array(t_ord)
                    t_ord = np.sort(t_ord)
                    t_ord = t_ord.tolist()
                if des == 1 : 
                    U = generar_u_aleatorio()
                    Y = -float(np.log(U))/lam_re
                    t_re = t + Y 
            elif t_re <= t1: #caso 2
                t = t_re ; des = des - 1
                if des > 0 :
                    U = generar_u_aleatorio()
                    Y = -float(np.log(U))/lam_re
                    t_re = t + Y
                if des == 0:
                    t_re = float('inf')
        falla = []
        for i in range(len(T)):
            suma = 0
            for j in range(i+1):
                suma = suma + T[j]
            falla.append(suma/(i+1))
        Tsimulaciones.append(falla[-1])
        I = np.arange(len(T))
        I = np.array(I)
        I = I + 1
        if i==0 or (i+1)%50==0:
            plt.figure()
            plt.bar(I,falla,width= 0.5,color='green') 
            plt.xlabel("n-ésima simulacion")
            plt.ylabel("media T-falla")
            plt.title(f"{i+1} simulaciones") 
            plt.pause(1.5)
            plt.close()
    print(f"i-esimo tiempo de falla promedio del sistema hasta la i-esima simulacion:")
    print(",".join(f"{e:.4f}" for e in Tsimulaciones))
    plt.bar(np.arange(len(Tsimulaciones)),Tsimulaciones,width=0.5,color="green")
    plt.xlabel("n-ésima simulacion")
    plt.ylabel("media T-falla")
    plt.title(f"{i+1} simulaciones")
    plt.show()

if __name__=='__main__':
    problema_de_reparacion()