import sys
import numpy as np 
import random as rd 
import matplotlib.pyplot as plt 
import math 
from time import time_ns
import math

normal = lambda : np.random.normal(0,1)
def ejercicio1():
    x = []
    x.append(normal())
    print(f"inciso a) S/n**.5 < 0.1 como S ~ 1 → 1/n**.5 < 0.1  → 1/.1**2 < n → 99.99<n  n es minimo 100")
    while True:
        x.append(normal())
        _x_sum = 0
        for e in x:
            _x_sum += e
        k = len(x)
        _x = _x_sum/k
        var = 0
        for e in x:
            var +=(e - _x)**2
        var = var /(k-1)
        S = var**0.5
        if(k>= 30 and S/k**.5<0.1):
            print(f"inciso b) genero: {k} normales inciso c) media _x : {_x} inciso d) var:{var}")
            print(f"comentarios c) y d) los resultados son cercanos a tanto las media y varianza teoricas")
            break
def ejercicio1_b():
    x = []
    x.append(normal())
    print(f"inciso a) S/n**.5 < 0.1 como S ~ 1 → 1/n**.5 < 0.1  → 1/.1**2 < n → 99.99<n  n es minimo 100")
    while True:
        x.append(normal())
        _x_sum = 0
        for e in x:
            _x_sum += e
        k = len(x)
        _x = _x_sum/k
        var = 0
        for e in x:
            var +=(e - _x)**2
        var = var /(k-1)
        S = var**0.5
        if(k>= 30 and S/k**.5<0.01):
            print(f" media _x : {_x}  ,var:{var}, k:{k} normales")
            break

aleatorio = lambda: rd.uniform(0,1) 

def ejercicio2():
    g = lambda u : math.exp(u**2)
    # como los limtes son 0→1 integral(G(U)) ~ E(g(U)) 
    G = []
    G.append(g(aleatorio()))
    d = 0.01
    while True:
        G.append(g(aleatorio()))
        _x_sum = 0
        for e in G:
            _x_sum+=e
        k = len(G)
        _x = _x_sum/k
        var = 0
        for e in G:
            var+=(e- _x)**2
        var = var/(k -1)
        S = var**.5
        if ( k>=100 and S/k**.5 < d):
            print(f"media :{_x} , {k} valores")
            break

def ejercicio3():
    #d = H/alpha/2   dato H = .5   1 - alpha = .99  → alpha = 0.01 → alpha/2 = 0.005 
    #de la tabla normal estandar Zalpha/2 = 2.575 CORREGIR DE SER EL CASO 
    H = 0.5 
    Zalpha_2 = 2.575
    d = H/Zalpha_2
    x = [102,112,131,107,114,95,133,145,139,117,93,111,124,122,136,141,119,122,151,143]
    # S /k**.5 < .5/2.575
    x = np.array(x) 
    _x = np.average(x)
    var = 0
    for e in x:
        var +=(e - _x)**2
    k = len(x)
    var = var /(k - 1) # estimador 
    print(f"media muestral :{_x} y estimador : {var}")
    S = var**.5
    #S = (np.var(x)) **.5 
    print(f"S/n*.5 < .5/2.575 → (S*2.575/.5)**2<n :" )
    cota_inferior = (S*2.575/.5)**2
    print(f"{cota_inferior} < n    →  aumentar{int(cota_inferior) -20}")
    #contrastando...
    x_ord = np.sort(x)
    x_min = x_ord[0]
    x_max = x_ord[-1]
    generar = lambda : int(rd.uniform(0,1)*(x_max - x_min) + x_min)
    x= x.tolist()
    while True:
        x.append(generar())
        _x_sum =0
        for e in x:
            _x_sum +=e
        k = len(x)
        _x_ = _x_sum /k
        var = 0
        for e in x:
            var +=(e -_x_)**2
        var = var /(k - 1)
        S = var **.5
        if (S/k**.5 < d):
            print(f"theta : {_x_} k : {len(x)} , diferencia:{len(x)- 20}")
            break
    print(f"la contrastacion indica que la cantidad a generar bordea los 7300-7500 nuevos valores")
if __name__=='__main__':
    #ejercicio1()
    #ejercicio1_b()
    #ejercicio2()
    ejercicio3()