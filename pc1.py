import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math 
def pregunta_1(n=1000):
    yy= []
    for i in range(n):
        u = rd.random()  # U(0,1)
        #para que los limites 0 → 1 ,y usar dis uniform y ley de grandes numeros:suma ponderada~ media(integral) , g(1/y-1 )/y^2 en este caso  1/u - 1
        g = (1/u-1) / (1 + (1/u-1)**2)**2 * (1/u**2)
        yy.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += yy[i]                        #↓ ley fuerte de grandes numeros
        promedio_acumulado.append(suma/(i+1)) #media aprox = suma_actual/k  k:1→n
    print("Estimación final :", promedio_acumulado[-1])
    n_index = range(1,n+1)
    plt.plot(n_index, promedio_acumulado, label="Promedio acumulado")
    plt.xlabel("muestras ")
    plt.ylabel("Estimación")
    plt.title("usando  y=1/(1+x) que esta en el libro")
    plt.legend()
    plt.show()

def pregunta_2(reps=1000):                                     
    # p2= u1*u2   p3=u1*u2*u3    u1*u2*u3*u4  ...*ui mientras se cumpla p>= cte, y para calcular E  como u es uniforme usamos la ley fuerte; osea la ponderada se aproxima E con seguridad  
    resultados = []
    for r in range(reps):
        prod = 1         
        n = 0     
        while prod >= math.exp(-3):
            u = rd.random()        
            prod *= u             
            n += 1 
        N = n - 1                  
        resultados.append(N) 
    E_N = sum(resultados)/len(resultados)
    # Estimación d P{N=i} para i=0→6
    P_N = [resultados.count(i)/reps for i in range(7)]
    print("a) Estimación de E[N]:", E_N)
    print("b) Probabilidades P{N=i} para i=0..6:", P_N)
    return E_N, P_N

if __name__=='__main__':
    pregunta_1()
    pregunta_2()
