import random as rd 
import numpy as np 

def pregunta_1():
    #aceptacion rechazo 
    # se dispone de p=[] , q conocida (binomial) n= ? p = ? 
    # simulando Y 
    # U <= p(Y)/c*q(Y) → aceptacion X ← Y
    # P(X>=k) = 1 - P(X<=k) → 
    print()
    



def pregunta_2(N=50):
    #2...12
    # t. inversa
    # F(j-1) <=U<F(j)
    p = [1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10]
    #     2    3    4     5............................ 12 
    n = 11
    F=[] 
    X =[]
    for i in range(n):
        suma = 0
        for j in range(i):
            suma  = suma + p[j]
        F.append(suma+p[i])
    print(F)
    cont = 0
    while (cont<N):
        U = rd.uniform(0,1)
        for j in range(n):
            if (U<F[0]):
                X.append(2)
            if (F[j-1]<= U <F[j]):
               X.append(j+2) 
        cont = cont + 1
    print(X)
    f = [0,0,0,0,0,0,0,0,0,0,0,0]
    for e in X:
        if e==2: f[0]+=1;continue
        if e==3: f[1]+=1;continue
        if e==4: f[2]+=1;continue
        if e==5: f[3]+=1;continue
        if e==6: f[4]+=1;continue
        if e==7: f[5]+=1;continue
        if e==8: f[6]+=1;continue
        if e==9: f[7]+=1;continue
        if e==10: f[8]+=1;continue
        if e==11: f[9]+=1;continue
        if e==12: f[10]+=1;continue
    print(f)
    print(f"{len(X)}")
    for i in range(len(f)):
        f[i] = f[i]/len(X)
    print(f)
    #esperanza suma x.f(x)
    esperado = 0
    for i in range(n):
        esperado = esperado + X[i]*f[i]
    print(f"valor esperado: {esperado}")
    
def max_entero(f):
    cadena = str(f)
    num = f.split(".")[0]
    entero = int(num)
    return entero

def pregunta_3():
    # cartas del 1 → 100 , se voltea 1 a la vez
    # j-1/n <= U < j/n
    # j-1 <= n*U < j
    #max_entero(n*U)
    print()
    n = 100
    U = rd.uniform(0,1)
    i = max_entero(n*U) + 1

if __name__=='__main__':
    #pregunta_1()
    #pregunta_2()
    pregunta_3()
    #print(max_entero("23.333"))
