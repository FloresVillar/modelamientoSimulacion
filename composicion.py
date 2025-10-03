import numpy as np 
import random as rd 

def max_entero(num):
    cadena =str(num)
    print(cadena)
    cadena = cadena.split(".")
    print(cadena)
    e = int(cadena[0])
    return e

def ejemplo4f(N = 5000):
    p =[0.05,0.05,0.05,0.05,0.05,0.15,0.15,0.15,0.15,0.15]
    # p1j = 0.1 para j 1→10
    #p2j = 0.3 para j 6→10    y  0 para j 1→5
    #multiplicando  con alpha= 0.5
    # pj = 0.1 * alpha + 0*0.3  = 0.05    para j 1→5
    # pj = 0.1*0.5 + 0.5*0.3 =0.15    para j 6→10
    n1 = 10 ; n2 = 5
    X =[]
    for i in range(N):
        U1 = rd.uniform(0,1)
        U2 = rd.uniform(0,1)
        if(U1<0.5):
            X1 = max_entero(n1*U2) + 1
            X.append(X1)
        else:
            X2 = max_entero(n2*U2) + 6 
            X.append(X2)
    print(X)
    X_cuenta =[0,0,0,0,0,0,0,0,0,0]
    for x in X:
        if (x==1): X_cuenta[0]+=1
        if (x==2): X_cuenta[1]+=1
        if (x==3): X_cuenta[2]+=1
        if (x==4): X_cuenta[3]+=1
        if (x==5): X_cuenta[4]+=1
        if (x==6): X_cuenta[5]+=1
        if (x==7): X_cuenta[6]+=1
        if (x==8): X_cuenta[7]+=1
        if (x==9): X_cuenta[8]+=1
        if (x==10): X_cuenta[9]+=1 
    X_f_relativa=[]
    for x in X_cuenta:
        X_f_relativa.append(x/len(X))
    print(f"p={p}")
    print(f"X_relativa={X_f_relativa}")
if __name__=='__main__':
    ejemplo4f()