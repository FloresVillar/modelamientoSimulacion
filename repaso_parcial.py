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
    seed = time_ns()
    U = (a * seed + c ) % m
    u = []
    u.append(U)
    for i in range(N):
        Ui = (u[-1] * a + c) % m
        u.append(Ui)
    u = np.array(u)
    u = u/m
    P = [i for i in range(N)]
    for k in range(N-1,-1,-1):   
        Y = math.floor(k*u[k])
        tmp = P[Y]
        P[Y] = P[k]
        P[k] = tmp    
    return u[P[-1]]

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

def ejemplo4f_composicion(N=20): 
    alpha = 0.5
    p = [0.05,0.05,0.05,0.05,0.05,0.15,0.15,0.15,0.15,0.15]
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
            Y = math.floor(10*U1) + 1
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
    f = np.array(f)
    f = f/N
    print(f"p: {p}")
    print(f"f: {f}")
    x = [i for i in range(1,11) ]
    plt.subplot(1,2,1);plt.bar(x,p)
    plt.subplot(1,2,2);plt.bar(x,f)
    plt.show()

if __name__=='__main__':
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
    ejemplo4f_composicion()