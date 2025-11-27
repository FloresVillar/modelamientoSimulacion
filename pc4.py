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

generar_u_aleatorio = lambda : rd.uniform(0,1)  #los resultados son similares

def problema_de_reparacion(N=500,lam_de=1,lam_re=0.25):
    X = [] 
    Tsimulaciones = []
    media = [] ; media.append(0)
    S_2 = [] ; S_2.append(0)

    for i in range(N):
        #print(f"\nsimulacion: {i+1}")
        t = 0  
        des = 0 
        t_re =  float('inf') 
        re = 4
        n = 10
        T_f = []
        for i in range(n):
            U = generar_u_aleatorio() 
            x = -float(np.log(U))/lam_de
            T_f.append(x)    
        T_f = np.array(T_f) 
        t_ord = np.sort(T_f)
        T_f = T_f.tolist() 
        t_ord = t_ord.tolist()
        #print(",".join(f"{x:.4f}" for x in t_ord))
        while True:
            t1 = t_ord[0]
            if t1 < t_re : # caso 1
                t = t1 ; des = des + 1
                t_ord.pop(0)
                if des == re + 1: # porque cuando hay descompostura sale 1 inmediatamente de respuestos
                    X.append(t)
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
        for i in range(len(X)):
            suma = 0
            for j in range(i+1):
                suma = suma + X[j]
            falla.append(suma/(i+1))
        Tsimulaciones.append(falla[-1])
        I = np.arange(len(X))
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
        # llamar a parar_ahora()
        if(i>0):  # se modifica los i de las divisiones para guardar relacion con el algoritmo, los indices de media[ ] y Var[] no son relevantes en cuanto al algoritmo mas que para acceder de acuerdo a la indexacion
            mediai = media[i-1] + (X[i] - media[i-1])/(i+2) # en la formula se va desde 2 entonces como estamos en 1 añadimos 2, mismo analisis abajo 
            media.append(mediai)
            S_i = (1-1/(i+1))*(S_2[i-1])**2 + (i+2)*(media[i]-media[i-1])**2
            S_2.append(S_i)
            d = 0.001
            if (S_2[i]**0.5)/i**0.5 < d and i > 29:
                print(f"la media de fallo es : {media[i]} en la i-esima simulacion {i+1}")
                break
    print(f"i-esimo tiempo de falla promedio del sistema hasta la i-esima simulacion:")
    print(",".join(f"{e:.4f}" for e in Tsimulaciones))
    plt.bar(np.arange(len(Tsimulaciones)),Tsimulaciones,width=0.5,color="green")
    plt.xlabel("n-ésima simulacion")
    plt.ylabel("media T-falla")
    plt.title(f"{i+1} simulaciones")
    plt.show()

e = np.e

def fact(n):
    if n == 0:
        return 1
    prod = 1 
    for i in range(1,n+1):
        prod = prod *i
    return prod

def ejercicio2():
    lam = 0.3 # por hora → h =4  y lam = lam * h = 1.2
    lam = lam * 4
    f = lambda x : ((e**-lam) * lam**x )/ fact(x)
    # 10 → 2  ;  0 → T=4   | 0 | 0 | 0 | 0 |
    # en los t=1 t=2 t=3 t= 4 ocurren cero eventos y  
    p = f(0)
    print(f"la probabilidad de que no ocurra ningun evento es: {p}")

def ejercicio3(N=50):
    A = []
    for i in range(N):
        A.append(rd.uniform())
    for i in range(1,len(A)):
        if A[i-1]>A[i]:
            M = i
    


if __name__=='__main__':
    #problema_de_reparacion()
    ejercicio2()