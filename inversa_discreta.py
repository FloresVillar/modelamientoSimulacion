import numpy as np 
import matplotlib.pyplot as plt
import random as rd
#transformada inversa discreta
# F(xj-1)<=U<F(xj)
"""
tenemos por ejemplo P(X=xj)= pj SUMApj=1
p={p1=0.2,p2=0.15,p3=0.25,p4=0.40}   
generamos u ~U(0,1)
si p0+p1+...+pj-1<=u<p0+p1+...+pj entonces x=xj
"""
def inversa_discreta(n=10):
    p=[0.2,0.15,0.25,0.40]
    F=[]
    X=[]
    print(f"lenp={len(p)}")
    for j in range(len(p)):
        print(f"j={j}")
        suma = 0
        for k in range(j):
            print(f"k={k}\t")
            suma+=p[k]
        F.append(suma+p[j])
    print(f"acumuladas listas") 
    i = 0
    while (i<n):
        u = rd.random()
        if(u<F[0]):
            X.append(0+1)        
        for j in range(1,len(p)):
            if(F[j-1]<=u<F[j]):
                X.append(j+1)
        i+=1 
    print(f"X={X}")
    X_cuenta =[0,0,0,0]
    for x in X:
        if (x==1): X_cuenta[0]+=1
        if (x==2): X_cuenta[1]+=1
        if (x==3): X_cuenta[2]+=1
        if (x==4): X_cuenta[3]+=1
    X_f_relativa=[]
    for x in X_cuenta:
        X_f_relativa.append(x/len(X))
    print(f"p={p}")
    print(f"X_relativa={X_f_relativa}")
if __name__=='__main__':
    inversa_discreta(10000)