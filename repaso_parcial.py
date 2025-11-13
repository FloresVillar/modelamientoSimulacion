import sys
import numpy as np 
import random as rd 
import matplotlib.pyplot as plt 
import math 
from time import time_ns
def factorial(n=5)->int:
    if n < 0:
        return -1
    if n == 0:
        return 1
    prod = 1
    for i in range(1,n+1):
        prod = prod *i
    return prod
e = np.e

def poisson_recursivo(i=4,lam = 1):
    # Pj+1 = Pj \U03BB /(j+1)
    P = []
    P0 = e**(-lam)
    P.append(P0)
    if i == 0:
        return P
    for j in range(1,i+1):
        Pi=P[j-1]*lam/(j)
        P.append(Pi)
    return P[-1]
#no genera algo aceptable
def generador_aleatorio(a = 87,m = 17, N=50,semilla = 17):
    #xn = aXn-1 mod m
    X = []
    x1 = (a*semilla) % m
    print(x1)
    X.append(x1)
    for i in range(1,N):
        x = (a*X[-1])%m 
        X.append(x)
    print(X)  
#el libro menciona el valor de a y m , 
#para el valor de c,  condiciones de hull-dobell
#c y m coprimos
#a - 1 es multiplo de todos los factores de m
#si m es 4° → a-1 tambien lo es
def generador_aleatorio_grande(N=256, m=2**35 - 31,a=5**5,semilla = 23,c=100000007):
    X = []
    x1  = (a * semilla + c) % m 
    X.append(x1)
    #print(x1)
    for i in range(N):
        x = (a * X[-1] + c )%m
        #print(x)
        X.append(x)
    U = []
    for x in X:
        U.append(x/m)
    return U

def integral_aleatorio(n=256,g = lambda x: x**2):
    U = generador_aleatorio_grande(N=n,semilla=867)
    G = []
    for i in range(n):
        G.append(g(U[i]))
    print(G)
    SG = []
    for i in range(len(G)):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma+G[i])
    THETA = []
    for i in range(len(SG)):
        THETA.append(SG[i]/(i+1))
    x = range(len(G))
    plt.plot(x,THETA)
    plt.show()

def estimacion_pi(n=256):
    U1 = generador_aleatorio_grande(N=n,semilla=731)
    U2 = generador_aleatorio_grande(N=n,semilla=867)
    k = 0
    for i in range(n):
        a = (2*U1[i]-1)**2
        b = (2*U2[i]-1)**2
        if (a + b) <=1 :
            k = k + 1
    pi = 4*k/n
    return pi  

def ejercicio1_capitulo3():
    #x0 = 5 , xn = 3xn-1 mod 150 determinar x1,,x10
    x0 = 5
    X= []
    X.append(x0)
    for i in range(1,11):
        xn = 3*X[-1] % 150
        X.append(xn)
    print(X) 

def ejercicio2_capitulo3():
    #x0=3 xn=(5xn-1 +7 )mod200
    x0 = 3
    X=[]
    X.append(x0)
    for i in range(1,11):
        xn = (5*X[-1]+ 7) % 200
        X.append(xn)
    print(X)
e = np.e
def ejercicio3_capitulo3(n=500):
    #exp(e^x) x:0→1
    g = lambda x : e **(e**x)
    G = []
    U = generador_aleatorio_grande(N=n,semilla= 867)
    for i in range(n):
        gx = g(U[i])
        G.append(gx)
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma+G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    n_  = range(n)
    print(THETA[-1])
    plt.plot(n_,THETA,label='exp(e^x)')
    plt.title('exp(e^x)')
    plt.show()

def ejercicio4_capitulo3(n=256):
    U = generador_aleatorio_grande(N=n,semilla = 867)
    g = lambda x: (1-x**2)**1.5
    G=[]
    for i in range(n):
        G.append(g(U[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    n_ = range(n)
    print(THETA[-1])
    plt.subplot(2,1,1)
    plt.plot(n_,THETA,label='(1-x^2)^3/2')
    plt.title('(1-x^2)^3/2')
    plt.show()

def ejercicio5_capitulo3(n=256):
    U = generador_aleatorio_grande(N=n,semilla=113)
    a = -2 ; b = 2
    #g´(x) = g(x(b-a) + a)(b-a)
    #y = x*(b-a) + a
    g = lambda x : (b-a)*(e**((x*(b-a)+a)+(x*(b-a)+a)**2))
    G = []
    for i in range(n):
        G.append(g(U[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(G[i]/(i+1))
    print(THETA[-1])
    n_ = range(n)
    plt.subplot(2,1,1)
    plt.plot(n_,THETA)
    plt.title('e^(x+x**2)')
    plt.show()

def ejercicio6_capitulo3(n = 256):
    U = generador_aleatorio_grande(N=n,semilla= 867)
    # g = x(1+x**2)**-2
    # cambio y = 1/x+1  
    # g (1/y -1) /y**2 dy
    g = lambda y : ((1/y-1)*((1/y-1) + (1/y-1)**2)**(-2))/y**2
    G = []
    for i in range(n):
        G.append(g(U[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    n_ = range(n)
    plt.subplot(2,1,1)
    plt.plot(n_,THETA)
    plt.title('g = x(1+x**2)**-2')
    plt.show()

def ejercicio7_capitulo3(n=256):
    U = generador_aleatorio_grande(N=n,semilla=113)
    #g = e^(-x**2)
    #y = 1/(x+1)
    #g´ = g(1/y -1 )/y^2
    g = lambda y : (e**(-(1/y-1)**2))/y**2
    G = []
    for i in range(n):
        G.append(g(U[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(2*SG[i]/(i+1))
    n_ = range(n)
    print(f"la integral={THETA[-1]}")
    plt.subplot(1,2,1);plt.plot(n_,THETA)
    plt.title('e^(-x**2)')
    plt.show()

def ejercicio8_capitulo3(n=256):
    U1 = generador_aleatorio_grande(N=n,semilla = 867)
    U2 = generador_aleatorio_grande(N=n,semilla = 131)
    g = lambda x,y : e**((x + y ) **2)
    G = []
    for i in range(n):
        G.append(g(U1[i],U2[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    n_ = range(n)
    print(f"{THETA[-1]}")
    plt.plot(n_,THETA)
    plt.title('e**((x + y ) **2)')
    plt.show()

def ejercicio9_capitulo3(n=256):
    # g= e^-(x+y) dy dx ; limites 0 x  ,  0 inf
    # g = lambda x,y : e **-(x + yx ) xdy
    # g = lambda x,y : e **-(1/x-1 +y(1/x-1)) (1/x-1)/x**2dydx
    g = lambda x,y : (e **-(1/x-1 +y*(1/x-1))) * (1/x-1)/x**2
    U1 = generador_aleatorio_grande(N=n,semilla = 867)
    U2 = generador_aleatorio_grande(N=n,semilla = 131) 
    G = []
    for i in range(n):
        G.append(g(U1[i],U2[i]))
    SG = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G[j]
        SG.append(suma + G[i])
    THETA = []
    for i in range(n):
        THETA.append(SG[i]/(i+1))
    n_ = range(n)
    print(f"{THETA[-1]}")
    plt.plot(n_,THETA)
    plt.title(' e^-(x+y) dy dx ; limites 0 x  ,  0 inf')
    plt.show()

def ejercicio10_capitulo3(n=256):
    #cov(u,e^u) = E(u*e^u) - E(u)*E(e^u)
    g1 = lambda x: x*e**x 
    g2 = lambda x: x 
    g3 = lambda x: e**x
    U1 = generador_aleatorio_grande(N=n,semilla= 137)
    U2 = generador_aleatorio_grande(N=n,semilla=467)
    U3 = generador_aleatorio_grande(N=n,semilla = 671)
    G1 = []
    G2 = []
    G3 = []
    #
    for i in range(n):
        G1.append(g1(U1[i]))
    for i in range(n):
        G2.append(g2(U2[i]))
    for i in range(n):
        G3.append(g3(U3[i]))  
    #
    SG1 = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G1[j]
        SG1.append(suma + G1[i])
    THETA1 = []
    for i in range(n):
        THETA1.append(SG1[i]/(i+1))
    #
    SG2 = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G2[j]
        SG2.append(suma + G2[i])
    THETA2 = []
    for i in range(n):
        THETA2.append(SG2[i]/(i+1))
    #
    SG3 = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + G3[j]
        SG3.append(suma + G3[i])
    THETA3 = []
    for i in range(n):
        THETA3.append(SG3[i]/(i+1))
    COV = []
    for i in range(n):
        COV.append(THETA1[i] - THETA2[i]*THETA3[i])
    #
    n_ = range(n)
    print(f"{COV[-1]}")
    plt.plot(n_,COV)
    plt.title(' COV')
    plt.show()

def ejercicio12_capitulo3(secuencias = 100):
    # N = minimo {n : suma  ui >1}
    #U = generador_aleatorio_grande(N=n,semilla = 167)
    suma =0
    i = 0
    N = []
    cont  = 0
    while cont < secuencias:
        U = rd.uniform(0,1)
        suma = suma + U
        if suma > 1:
            N.append(i+1)
            i = 0
            suma = 0
            cont +=1
        i = i + 1
    suma = 0
    print(N)
    for j in range(len(N)):
        suma += N[j]
    THETA = suma /len(N)
    print(f"la esperanza={THETA}")

def generar_aleatorio(m = 2**35-31 , a = 5**5 , c = 100000007,semilla =167,N=100)->list:
    # u = (a*semilla + c)mod  m
    u  = (a * semilla + c) % m
    U = []
    U.append(u)
    for i in range(1,N):
        u = ( a * U[-1] + c) % m
        U.append(u)
    for i in range(len(U)):
        U[i] = U[i]/m
    #print(f"U  = {U}")
    return U 

def capitulo4_ejemplo4a(n=1000):
    p = [.2,.15,.25,.4]
    px = [1,2,3,4]
    F = []
    for i in range(len(p)):
        suma = 0
        for j in range(i):
            suma = suma + p[j]
        F.append(suma + p[i])
    print(f"F : {F}")
    X = []
    U = generar_aleatorio(N=n)
    print(f"U dentro de ejemplo4a {U}")
    for i in range(len(U)):
        if U[i] < F[0]:
            X.append(px[0])
        for j in range(1,len(F)):
            if(F[j-1] <= U[i] < F[j]):
                X.append(px[j])
    #print(f"X : {X}")
    h = {"uno":0,"dos":0,"tres":0,"cuatro":0}   
    for e in X:
        match e:
            case 1:
                h["uno"]=h["uno"]+1
            case 2:
                h["dos"]=h["dos"]+1
            case 3:
                h["tres"]=h["tres"]+1
            case 4:
                h["cuatro"]=h["cuatro"]+1
            case _:
                print()
    f = np.array(list(h.values()))
    plt.subplot(1,2,1);plt.bar(px,f)
    f = f/len(X)
    plt.subplot(1,2,2);plt.bar(px,f)
    plt.show()

def ejemplo4b(n=10):
    P = []
    for i in range(n):
        P.append(i+1)
    u = generar_aleatorio(semilla= 1007, N=n)
    for k in range(n-1,-1,-1):
        U = u[k] 
        I = math.floor(k*U) + 1 # indices
        tmp = P[k]
        P[k] = P[I]
        P[I] = tmp 
    print(f"P: {P}")
    # si queremos sibconjunto de r r<=n/2 generamos el subconjunto
    # si r>  n/2 geramos subconjunto de n-r y el buscado seria el complemento

def seleccion_subconjunto_prueba_medica(N=5,n=20):
    r = int(n/2)
    P = [i+1 for i in range(n)]
    for i in range(N):
        u = generar_aleatorio(semilla =123+i*1000003,N=n)
        SUB = []
        for k in range(n-1,-1,-1):
            U = u[k]
            I = math.floor(k*U) 
            tmp = P[k]
            P[k] = P[I]
            P[I] = tmp 
            SUB.append(P[k])
            if len(SUB) == r:
                break
        print(SUB)
# corregirr el hecho de que nunca se escoge a posicion 0(1)    

def ejemplo4c(n = 50):
    #Suma a(i)/n   n grande
    u = generar_aleatorio(semilla = 23467, N=n)
    a = lambda i :e**i
    suma = 0
    P = [i for i in range(n)]
    k = 35
    A = []
    for i in range(n-1,-1,-1):
        I = math.floor(n*u[i])
        tmp = P[i]
        P[i] = P[I]
        P[I] = tmp
        A.append(P[i])
        if len(A) == k: break 
    A = np.array(A)
    promedio = sum(A)/len(A)
    print(f"promedio: {promedio}")

def ejemplo4d(n=20):
    # generando una geometrica
    p = .2
    q = .8
    u = generar_aleatorio(semilla = 867, N=20)
    P = [i for i in range(n)]
    for k in range(n-1,-1,-1):
        I = math.floor(k*u[k])+ 1
        tmp = P[k]
        P[k] = P[I]
        P[I] = tmp
    ind = P[n-1]
    U = rd.uniform(0,1)
    j = math.floor(math.log(U)/math.log(q)) + 1 
    print(f"intentos hasta el primer exito: {j}")
    
def generar_un_aleatorio(m=2**35-31,a=5**5,c=100000007):
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
    """P = [i for i in range(N)]
    for k in range(N-1,-1,-1):   
        Y = math.floor(k*u[k])
        tmp = P[Y]
        P[Y] = P[k]
        P[k] = tmp    
    return u[P[-1]]"""

def generacion_poisson42():
    # Pi+1 = Pi lambda/(i+1) 
    X = []
    l = 3
    p = e**(-l)
    i = 0
    F = p
    while(True):
        U = generar_un_aleatorio()
        print(f"i: {i} ,U: {U} , F: {F}")
        if(U < F):
            X.append(i)
            break
        p = l*p/(i+1)
        F = F + p 
        i = i + 1
    print(X) 
# generrar 100 veces calcular las frecuencias relativas  y esa se aproxima a la p(X=xi)

def generacion_binomial43():
    # P(X=i+1) = n-i/(i+1)P(X=i)p/(1-p) 
    p = 0.2
    n = 10
    c = p/(1-p)
    pr =(1-p)**n
    F = pr
    X = []
    i = 0
    while(True):
        U = generar_un_aleatorio()
        print(f"i: {i} ,U: {U} , F: {F}")
        if U < F:
            X.append(i)
            break
        pr = c*pr*(n-i)/(i+1)
        F = F +pr 
        i = i + 1
    print(X)

def ejemplo4e_aceptacion_rechazo(N=5000):
    X = []
    p = [0.11 , 0.12, 0.09 , 0.08 , 0.12 , 0.10, 0.09, 0.09, 0.1 , 0.1]
    p = np.array(p)
    #print(sum(p))
    q = [1/10 for i in range(10)]
    print(q)
    c =  -1 
    for i in range(len(p)):
        if(p[i]/q[i] > c): 
            c = p[i]/q[i]
    print(c)
    for i in range(N):
        while True:
            U1 = generar_un_aleatorio()
            # F(j-1)< = U <F(j) → (j-1)/10<=U<F(j) → j-1 <= 100*U<j ent(10U) + 1
            Y = math.floor(10*U1) + 1
            U2 = generar_un_aleatorio()
            if U2 <=p[Y-1]/(c*q[Y-1]): 
                X.append(Y)
                break
    print(X)
    X = np.array(X)
    f = [0 for i in range(len(p))]
    for e in X:
        for i in range(1,11):
            if i == e:
                f[e-1] = f[e-1] + 1
                break
    f = np.array(f)
    f = f/N
    print(f"p: {p}")
    print(f"f: {f}")
    x = [i for i in range(1,11) ]
    plt.subplot(1,2,1);plt.bar(x,p)
    plt.subplot(1,2,2);plt.bar(x,f)
    plt.show()

def ejemplo4f_composicion(N=100000): 
    alpha = 0.5
    p = [0.05,0.05,0.05,0.05,0.05,0.15,0.15,0.15,0.15,0.15  ]
    p1 = [1/10 for i in range(len(p))] # j-1/10 <= U< j/10
    p2 = [0,0,0,0,0,.2,.2,.2,.2,.2]  # (j-1)/5 <=U < j/5
    #pj = 0.5*0.1 = 0.05....j:1→5    alpha =0.5  p1=0.1
    # pj = 0.5*0.1 + 0,5*0.2 = 0.15 j:6→10    p1=0.1   p2=0.2 
    #teniendo las composiciones y viendo que cada p sumple suma=1
    X = []
    for i in range(N):
        U1 = generar_un_aleatorio()
        U2 = generar_un_aleatorio()
        if U1 < alpha :
            Y = math.floor(10*U2) + 1
            X.append(Y)
        else:
            Y = math.floor(5*U2) + 6
            X.append(Y)
    print(X)
    X = np.array(X)
    f = [0 for i in range(len(p))]
    for e in X:
        for i in range(1,11):
            if i == e:
                f[e-1] = f[e-1] + 1
                break
    print(f)
    f = np.array(f)
    f = f/N
    print(f"p: {p}")
    print(f"f: {f}")
    x = [i for i in range(1,11) ]
    plt.subplot(1,2,1);plt.bar(x,p)
    plt.subplot(1,2,2);plt.bar(x,f)
    plt.show()

def ejercicio1_capitulo4(n=500): 
    p = [1/3 , 2/3]
    x = [1,2]
    F = []  
    for i in range(len(p)):
        suma = 0
        for j in range(i):
            suma = p[j]
        F.append(suma + p[i])
    X = []
    for i in range(n):
        U = generar_un_aleatorio()
        for j in range(len(F)):
            if U < F[0]:
                X.append(x[0])
                break
            if F[j-1]<= U < F[j]:
                X.append(x[j]) 
                break
    f = [0 for i in range(len(p))]
    for e in X:
        for j in range(len(x)): 
            if e == x[j]:
                f[j] = f[j] + 1
                break
    f = np.array(f)
    f = f/n
    print(f"p: {p}")
    print(f"f: {f}") 
    plt.subplot(1,2,1);plt.bar(x,p)
    plt.subplot(1,2,2);plt.bar(x,f)
    plt.show()

def ejercicio2_capitulo4_generarX(p,x,N= 20):
    if type(p) is not  list and type(x) is not list:
        return 
    F = []
    n = len(p)
    for i in range(n):
        suma = 0
        for j in range(i):
            suma = suma + p[j]
        F.append(suma + p[i])
    #print(f"F: {F}")
    #F son las acumuladas
    #ahora transformada inversa
    X = []
    for i in range(N):
        U = generar_un_aleatorio()
        #print(f"U: {U}")
        for j in range(n):
            if U < F[0]:
                X.append(x[0])
                break
            if F[j-1]<= U < F[j]:
                X.append(x[j])
                break
    #print(X)
    return X


def ejercicio3_capitulo4():
    p = [0.3 , 0.2 , 0.35 , 0.15 ]
    x = [ 1, 2, 3 , 4 ]
    X = ejercicio2_capitulo4_generarX(p,x)
    print(X)

def ejercicio4_capitulo4(n_experimentos=100):
    # cartas 1 → 100 , se elige una si  sacada es i exito 
    exitos = []
    for e in range(n_experimentos):
        P = [i + 1 for i in range (100)]
        #print(P)
        n = len(P)
        for k in range (n-1 , -1 , -1):
            # uniforme (j -1)/k <= U < j/k
            # ent(k*U) + 1
            U = generar_un_aleatorio()
            I = math.floor(U*(k+1)) # P(I=i)=1/(k+1) i:0→k i/(k+1) <= U < i+1/(k+1)
            P[k] , P[I] = P[I] , P[k] #Esto garantiza que: El valor 0 puede salir (cuando U ∈ [0, 1/(k+1))),El valor k también (cuando U ∈ [k/(k+1), 1)).Cada uno con probabilidad 1/(k+1)"""
        print(P)
        exits = 0
        for i in range(n):
            #print(f"P[i]: {P[i]}, i: {i + 1}")
            if P[i] == i+1:
                exits = exits + 1
        exitos.append(exits)
    exitos = np.array(exitos)
    u = sum(exitos)/len(exitos)
    var = 0
    for e in exitos:
        var+=((e - u)**2)
    var /=len(exitos)
    print(f"u: {u} , var: {var} ")

def ejercicio5_capitulo4():
    P = []
    # j/n+1<= U < j+1/n+1
    n = 100 
    for k in range(n):
        P.append(k+1)
        U = generar_un_aleatorio()
        I = math.floor((k+1)*U)
        P[k] , P[I] = P[I] , P[k]
    print(P)

def ejercicio6_capitulo4(n=100):
    N =10000
    a = lambda t : e**(t/N)
    suma = 0
    for i in range(n):
        U = generar_un_aleatorio()
        #j/n+1 <= U< j+1/n+1    j <= n+1 U < j+1
        x = math.floor(U*(n+1))
        suma = suma + a(x)
    print(f"suma aproximada: {suma}")
    s = [a(i) for i in range(n)]
    s = np.array(s)
    S = sum(s)
    print(f"suma real : {S}")

def ejercicio7_capitulo4(n_experimentos=500):
        x = [i+2 for i in range(11)]
        n = len(x)
        print(f"x: {x} , len(x): {len(x)}")
        lanz = []
        for exp in range(n_experimentos):
            cuentas = [0 for i in range(11)]
            lan = 0
            flag = True
            while(flag):
                lan +=1
                U1 = generar_un_aleatorio()
                U2 = generar_un_aleatorio()
                I1 = math.floor(U1*6) + 1
                I2 = math.floor(U2*6) + 1
                for e in x:
                    if(I1 + I2 == e):
                        cuentas[e-2]+=1            
                        break
                for e in cuentas:
                    if e != 0:
                        flag = False
                    else:
                        flag = True
                        break
            lanz.append(lan)
        lanz = np.array(lanz)
        u = sum(lanz)/len(lanz)
        print(f"u : {u}")            
def ejercicio8_capitulo4():
    #a  = []       
    print()

def ejemplo5a_capitulo5_exponencial(n=50,lam=1):
    F = lambda x,lam=lam: 1 -e**-(lam*x) 
    #U = F(X) = 1-e**x ,despejando x = -log(1-U) ~ -log(U) 
    X = []
    for i in range(n):
        U = generar_un_aleatorio()
        x = -np.log(U)/lam
        X.append(x)
    n_ = np.arange(0,n)
    plt.subplot(1,2,1);plt.plot(n_,X,'o-')
    plt.show()

def observacion_capitulo5_generacion_poisson(n=50,lam = 1,T=1):
    #N(1) = Max{suma Xi <= 1} los xi son exponenciales xi = -log(Ui)/lam
    #max suma log(Ui)>=-lam    ; ese 1 puede ser un T cualquiera
    #max log(U1....Un)>=-lam
    #max u1...un >= e**-lam
    # los n cumplen hasta que no cumple 
    #N = min {u1..un < e**-lam} - 1
    X = []
    for i in range(n):
        prod_U = 1 
        i = 0
        while True:
            Ui = generar_un_aleatorio()
            prod_U= prod_U * Ui
            i = i + 1
            if prod_U < e**-(lam*T):
                X.append(i - 1)
                break
    print(f"X: {X}")

def ejemplo5c_capitulo5_generar_gamma(n=50,lam=1):
     # gamma X = -log(u1 u2 u3...)/lambda
    prod_U = 1
    for i in range(n):
        Ui = generar_un_aleatorio()
        prod_U = prod_U * Ui
    X = -np.log(prod_U)/lam
    print(f"gamma X: {X}")
    return X

def ejemplo5c_capitulo5_generar_exponenciales(n=50,lam=1):
    U1 = generar_un_aleatorio()
    U2 = generar_un_aleatorio()
    t = -np.log(U1*U2)/lam
    U3 = generar_un_aleatorio()
    X = t*U3
    Y = t - X
    print(f"exponenciales X: {X}, Y: {Y}")

generar_gamma = ejemplo5c_capitulo5_generar_gamma

def ejemplo5c_capitulo5_generar_exponencial(n=100,lam=1):
    t = generar_gamma(n= n,lam = lam)
    U = []
    for i in range(n-1):
        u = generar_un_aleatorio()
        U.append(u)
    U.append(0)
    U.append(1)
    print(U)
    U = np.array(U)
    U.sort()
    print(U)
    X = []
    for i in range(1,n+1):
        x = t*(U[i] - U[i-1])
        X.append(float(x))
    print(f"X: {X}")
    n_ = np.arange(1,n+1)
    plt.subplot(1,2,1);plt.plot(n_,X)
    f = 1-e**(-lam*Xn)
    plt.show()

def ejemplo5d_capitulo5_aceptacion_rechazo(n=10):
    f = lambda x:20*x*(1-x)**3
    g = lambda x:1
    #f/g = 20*x*(1-x)**3 ; 20*(1-x)**3 - 20*x*3*(1-x)**2 ; 20*(1-x)**2(1-x-3*x) , es 0 en x=1/4
    #f/g (1/4) = 135/64
    c = f(1/4)/g(1/4)
    X = []
    for i in range(n):
        U1 = generar_un_aleatorio()
        U2 = generar_un_aleatorio()
        if U2 <= f(U1)/(c*g(U1)):
            X.append(U1)
    print(f"X: {X}")   
    X = np.array(X)
    X_ord = np.sort(X)
    F_emp = np.arange(1,len(X_ord)+1)/len(X_ord) #1/n 2/n 3/n  .. 1  cada (Xi,i/n) Femp(Xi)=P(X<=Xi)~i/n es la acumulada
    n_ = np.linspace(0,1,100)
    F = np.cumsum(f(n_))
    F = F/F[-1]  
    plt.subplot(1,2,1);plt.plot(X_ord,F_emp)
    plt.subplot(1,2,2);plt.plot(n_,F)
    plt.show() 

def ejemplo5d_capitulo5_aceptacion_rechazo_g2x(n=100):
    f = lambda x:20*x*(1-x)**3
    g = lambda x: 2*x
    # f/g  = 10*(1-x)**3   derivando -30(1-x)**2  xcritico= 1 c =f/g(1) =  0, pero el maximo seria en 0 c=10
    c = 10
    G = lambda x: x**2
    # u = x**2    x=u**1/2
    X = []
    for i in range(n):
        U1 = generar_un_aleatorio()
        Y = U1**.5
        U2 = generar_un_aleatorio()
        if U2 <= f(Y)/(c*g(Y)):
            X.append(Y)
    print(X)

def ejemplo5e_capitulo5_generar_gamma(n=10):
    print("operativo")

def generacion_poisson_homogeneo_capitulo5(n = 10,lam = 1,T = 10):
    for i in range(n):
        t = 0; I = 0
        S = []
        while True:
            U = generar_un_aleatorio()
            t = t -float(np.log(U))/lam 
            if t > T :
                break
            I = I + 1 ; S.append(t)
        print(S[1:len(S)-1])
        print(I-1)

def proceso_poisson_y_gamma_capitulo2():
    #ocurren eventos en tiempos aleatorios y sea N(t) el numero de eventos que ocurren en [0,t]
    #Estos eventos constituyen un proceso de poisson si 
    #a) N(0) = 0
    #b) en intervalos distintos el numero de eventos son independientes
    #c) la distribucion del numero de eventos depende de la longitud del intervalo no de la posicioon 
    #d) la probabilidad P(N(h) = 1 )  = lambda* h cuando h (longitud del intervalo ) decrece 
    #e) la probabilidad P(N(h) >= 2) = 0  que ocurra mas de 1 evento es nulo
    """explicacion detallada:
    teneemos el intervalo de tiempo [0,t] lo dividimos en subintervalos 
        Δt = T/n   y hay un promedio de ocurrencia de λ ..
        la condicion (b) incremento independiente establece que N(t) es independiente N(t+s)-N(t)
         (c) el incremento estacionario establece que N(t+s) -N(t) es el mismo para todos los t
         (d) en pequeños intervalos un evento ocurre con probabilidad λt, (e) mientras a probabilidad de 2 o mas es 0
    Entonces dividimos el intervalo  la probabilidad de que ocurra 1 es λt/n no ocurra 1 - λt/n
    la probabilidad de que suceda dos o mas es 0 entonces podemos modelarlo mediante bernoulli
            1 si ocurre un evento en interval i
    Xi = { 
            0 si no ocurre 
    P(Xi = 1) = λt/n
    El numero total de eventos hasta t es N(t) = X1 +X2...Xn , una bernoulli con p=λt/n
    n bernoullis independientes hacen una binomial
    ahora cuando  n aumenta B(n,λt/n) → Poisson(λam = np = nλt/n = λt)
    Si P(N(t)>=2) no fuera 0 , no los Xi = ocurrencia de evento en el intervalo i no podria modelarse como
            1 , si ocurre
    Xi = {
            0   si no ocurre, luego estas son bernoullis , la suma de bernoullis → binomial → poisson cuando n grande
     """
def proceso_poisson_no_homogeneo_capitulo2():
    # una de las debilidades del proceso de poisson homogeneo es que los eventos tienen la misma probabilidad 
    # en todos los intervalos del mismo tamaño, eliminar el incremento estacionario N(t+s) -N(t) ya no es la misma en todos los intervalos
    # Si los eventos ocurren de manera aleatoria N(t) eventos, entonces se constituye un proceso de poisson 
    # con funcion de intensidad   λ(t) si :
    #a) N(0) = 0
    #b) los numero de eventos en intervalos distintos es independiente
    #c) lim h→0 P(exactamente 1 evento entre t y t+h)/h = λ(t)
    #d) lim h→0 P(dos o mas en t t+h )/h  = 0 
    """ con m(t) = integral λ(t)dt
    N(t+s) - N(t) es una poisson con media m(t+s) - m(t)
    
    Los eventos ocurren de acuerdo con un proceso poisson homogeneo con tasa  λ
    en t,t+h el numero de eventos N(t+h) - N(t) es una poisson con media λh

    se introduce p(t) , cada evento que ocurre en el instante t se cuenta o no con p(t)
    
    en un intervalo pequeño  t,t+h la probabilidad de que ocurra un evento es λh
    si cada evento se cuenta con p(t)
    la probabilidad de que ocurra y ademas sea contado es 
    P(1 evento contado [t,t+h]) = λp(t)
    
    la nueva intensidad es u(t) = λp(t) 

    m(t) = numero esperado de eventos contados hasta t
    integral λ p(s)ds  0 → t

    si p(t) = 1       u(t) = λ  tenemos el poisson homogeneo

    """
def lambda_(t):
    if 0 <= t <=5:
        return t/5
    else:
        if 5<t<=10:
            return 1 + 5*(t-5)

def generacion_poisson_no_homogeneo_captitulo5(n=10,lam=1,T=10):
    #queremos simular las primeras  T unidades de tiempo de un proceso de poisson
    #con funcion de intensidad  λ(t) , en el metodo de adelgazamiento se elige  λ 
    # tal que  λ(t) <=  λ   para t<=T
    # como en el caso del homogeno se genera el tiempo  de razon  λ  , y la aceptasmo con probabilidad
    #  λ(t)/ λ =p(t) se reduce la tasa de eventos dividiendo entre la tasa maxima  λ
    l_max = lambda_(10)
    for i in range(n):
        t = 0 ; I = 0
        S = []
        while True:
            U1 = generar_un_aleatorio()
            t = t -float(np.log(U1))/lam
            if t > T:
                break
            U2 = generar_un_aleatorio()
            if U2 <= (lambda_(t)/l_max):
                I = I + 1
                S.append(t) 
        print(f"simulacion: {i+1}")
        print(f"I : {I}")
        print(f"tiempos: {S}\n\n")

"""
la generacion de un modelo probabilistico 
se requiere la generacion de mecanismos estocasticos
para ver el flujo del modelo en el tiempo
hay ciertas cantidades que se quieren estudiar
pero como el modelo se vuelve compleja no hay una forma segura de calcular esas cantidades
De modo que se elabora un "marco general" , formulado en torno a "eventos discretos"
Metodo de simulacion  con eventos discretos

los elementos fundamentales para simulacion por eventos discretos son 
variables y eventos, se tendra un seguimientosde de ciertas variables
-variable tiempo , tiempo que ha transcurrido
-vatriable de conteo , numero de veces que ciertos eventos han ocurrido
-variable de estado del sistema , estado del sistema en el instante t
En todos los modelos de cola los clientes llegan de acuerdo a un poisson no homogeneo
con una funcion de intensidad l(t)
aplicamos la subrutina vista para generar el valor de Ts
 Ts definida como el tiempo 
de la primera llegada despues del instante s
    t = s
    U1
    t = t -log(U)/l
    si U2 <= l(t)/l_max   Ts = t fin
    generar U1....
"""
#PROBLEMA DE REPARACION

""" un sistema de n maquinas esta funcionando , se tienen algunas maquinas de respuestos
si una se descompone se reemplaza  y se envia al taller, donde solo una persona repara una a una
una vez reparada queda disponible como repuesto lista para cuando surja la necesidad
todos los tiempos de reparacion tienen distribucion comun G
Desde que empieza a trabajar el tiempo que funciona hasta descomponerse es una variable aleatoria
independiente de las anteriores, con una funcion de distribucion F

el sistema falla cuando una maquina se descompone y no hay repuestos
si al inicio hay n + s maquinas en buen estado
n se ponen a trabajar y s quedan como repuestos
queremos simular el sistema para aproximar E(T) donde T es el tiempo en que falla
se usara
variable de tiempo t
variable de sistema r:el numero de maquinas descompuestas en el instante t

OCURRE UN EVENTO si una maquina se descompone
cuando una maquina es reparada
para saber cuando ocurre el siguiente evento se necesita llevar un registro 
de los instantes en los cuales fallan las maquinas que estan en uso y el instante 
en que son reparadas
Lista de eventos t1<=t2<=....<=tn,t*
t son los tiempos de descompostura de las n maquinas y t* es el tiempo en que
la maquina en reparacion vuelve a funcionar, si no hay maquinas en reparacion t* = inf
para comenzar 
Inicializacion
    t = 0 
    r = 0
    t* = inf
    X1,X2...variables aleatorias independientes con distribucion F.ordenamos 
    estos valores para que ti sea el i-esimo menor i=1...n
    sea t1,...tn,t*
Actualizacion
caso 1 t1 < t*
    t = t1
    r = r + 1 (pues ha fallado otra maquina)
    si r = s + 1 , detener y reunir datos T=t (s + 1 descompuestas no hya repuesto)
    si r < s + 1 , generar X con distribucion F,esta variable representa el tiempo
                    de trabajo del repuesto que entrara en funciones 
    ahora reordenamos t2,t3...t + X sea ti el i-esimo menor de ellos i:1→n
    si d= 1 generar Y con funcion G  
    y hacer t* = t + Y ,pues la maquina que acaba de fallar es la unica descompuesta y se
    comienza a reparar de inmediato, Y sera su tiempo de reparacion y su reparacion
    concluye en el tiempo t + Y

caso 2 t*<=t1
    t = t*
    r = r - 1
    si r>0 generar Y con funcion G , es el tiempo de reparacion de la que acaba
    de entrar a servicio  y
    t* = t + Y
    si r = 0 t* =inf

cada vez que nos detenemos (r = s + 1) concluye la ejecucion , la salida es 
el tiempo de fallo T, reiniciamos y simulamos de nuevo
una k simulaciones de modo que las salidas sean T1 T2 ...Tk , con k variables independientes
cada una representa el tiempo de fallo, su promedio es la estimacion de E(T)
"""
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

def problema_de_reparacion(N=500,lam_de=1,lam_re=0.25):
    T = [] 
    Tsimulaciones = []
    for i in range(N):
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

"""n = int(sys.argv[1])
    print(f"fac({n}) = {factorial(n)}")
    i = int(sys.argv[2])
    print(f"poission({i}) = {poisson_recursivo(i)}")
    generador_aleatorio()
    n = int(sys.argv[3])
    print(f"aleatorio grande \n= {generador_aleatorio_grande(n)}")
    n = int(sys.argv[4])
    integral_aleatorio(n)
    n = int(sys.argv[5])
    print(f"pi = {estimacion_pi(n)}")
    ejercicio1_capitulo3()
    ejercicio2_capitulo3()
    ejercicio3_capitulo3(n)
    ejercicio4_capitulo3(n)
    ejercicio5_capitulo3(n)
    ejercicio6_capitulo3(n)
    ejercicio7_capitulo3(n)
    ejercicio8_capitulo3(n)
    ejercicio9_capitulo3(n)"""
    #n = int(sys.argv[1])
    #ejercicio10_capitulo3(n)
    #ejercicio12_capitulo3(n)
    #print(f"en main U  = {generar_aleatorio()}")
    #capitulo4_ejemplo4a()
    #ejemplo4b()
    #seleccion_subconjunto_prueba_medica()
    #ejemplo4c()
    #ejemplo4d() 
    #generacion_poisson42()
    #generacion_binomial43()
    #ejemplo4e_aceptacion_rechazo()
    #print(generar_un_aleatorio())+
    #ejemplo4f_composicion()
    #ejercicio1_capitulo4()
    #p = [0.3 , 0.2 , 0.35 , 0.05 , 0.10 ]
    #x = [2 , 3 , 6 , 7 , 9 ]
    #ejercicio2_capitulo4_generarX(p,x,N=30)
    #ejercicio3_capitulo4()
    #ejercicio4_capitulo4()  
    #ejercicio5_capitulo4()
    #ejercicio6_capitulo4()
    #ejercicio7_capitulo4()
    #ejemplo5a_capitulo5_exponencial()
    #observacion_capitulo5_generacion_poisson()
    #ejemplo5c_capitulo5_generar_gamma()
    #ejemplo5c_capitulo5_generar_exponencial()
    #ejemplo5d_capitulo5_aceptacion_rechazo()
    #ejemplo5d_capitulo5_aceptacion_rechazo_g2x()
    #generacion_poisson_homogeneo_capitulo5()
    #generacion_poisson_no_homogeneo_captitulo5()