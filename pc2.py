import random as rd 
import numpy as np 

def factorial(n):
    if (n==0 or n==1):
        return 1
    prod = 1 
    for i in range(1,n):
        prod = prod * i
    return prod * n
    
def comb(m,k):
    numerador = factorial(m)
    denominador = factorial(m-k)*factorial(k)
    print(f"{numerador} , {denominador}")
    return numerador/denominador

def max_entero(f):
    cadena = str(f)
    num = cadena.split(".")[0]
    entero = int(num)
    return entero

def binomial(k,n=10,p=0.12):
    return (comb(n,k) * (p**(k))*((1-p)**(n-k)))

"""def pregunta_1(N=50,n= 10, p=0.2,c=1.2):
    #aceptacion rechazo 
    # se dispone de p=[] , q conocida (binomial) n=10 p = 0.2
    #p = np.linalg.binm(2,n,p) ..
    #q = [bin(0),bin(1),bin(2),bin(3),bin(4),bin(5),bin(6),bin(7),bin(8),bin(9),bin(10)]
    p = [0.1,0.01,0.09,0.4,0.05,0.05,0.15,0.05,0.05,0.05,0]
    # simulando Y 
    # U <= p(Y)/c*q(Y) → aceptacion X ← Y
    # P(X>=k) = 1 - P(X<=k) → 
    X = []
    for i in range(N):
        for k in range(n):
            U1 = rd.uniform(0,1)
            Y = max_entero(n*U1) + 1
            U = rd.uniform(0,1)
            if (U <= p[k]/(c*q[k])):
                X.append(Y)
    print(X)
"""
def pregunta_1_corregido(n=10,N=15,k_min = 3):
    q = []
    for i in range(n+1):
        q.append(binomial(i,n,0.2))
    cond = 0
    for j in range(k_min,n+1):
        cond +=q[j]
    p_cond = []
    acumulado = 0
    for j in range(n+1):
        if j < k_min:
            p_cond.append(0)
        else:
            p_cond.append(q[j]/cond)
    c = 1/cond 
    X= []
    while len(X)<N:
        acumulado = 0
        Y = 0
        U1 = rd.uniform(0,1)
        for j in range(n+1):
            acumulado+=q[j]
            if U1 <= acumulado:
                Y = j
                break  
        U2 = rd.uniform(0,1)
        if U2 <= p_cond[Y]/c*q[Y]:
            X.append(Y)
    suma_X = 0
    for v in X:
        suma_X += v 
    THETA  = suma_X /len(X)
    print(f"esperanza = {THETA}")

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
    
def pregunta_2_corregido(N=100):
    lanzamientos = []
    for i in range(N):
        resultados_vistos = []
        lanza = 0
        while len(resultados_vistos)<11:
            U1 = rd.uniform(0,1)
            U2 = rd.uniform(0,1)
            dado1 = (U1*6)+1
            dado2 = (U2*6)+1
            flag = False
            for r in resultados_vistos:
                if r == (dado1 + dado2):
                    existe == True
                    break
            if not flag:
                resultados_vistos.append(dado1+dado2)
            lanza +=1
        lanzamientos.append(lanza)
    suma = 0
    for v in lanzamientos:
        suma+=v
    THETA = suma /N
    print(THETA)

def pregunta_3(N=1000):
    # cartas del 1 → 100 , se voltea 1 a la vez
    # j-1/n <= U < j/n
    # j-1 <= n*U < j
    #max_entero(n*U)
    #exito carta i es la i-ésima carta volteada,osea la geometrica 
    n = 100 
    for j in range(n):
        U = rd.uniform(0,1)
        i = max_entero(n*U) + 1
        if(i == j):
            print()



if __name__=='__main__':
    pregunta_2_corregido()
    #pregunta_2()
    #pregunta_3()
    #print(max_entero("23.333"))
