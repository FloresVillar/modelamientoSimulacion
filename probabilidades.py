import random as rd
import numpy as np
import matplotlib.pyplot as plt

############## Calculo de probabilidad exito Lanz Moneda #########
def lanzar_moneda():
    n=100
    y =[]
    for i in range(n):
        if rd.random()>0.5:
            y.append(1)
        else:
            y.append(0) 
    n_=range(1,n+1)
    suma_acumulada = []
    suma = 0
    for i in range(len(y)):
        suma+=y[i]
        suma_acumulada.append(suma)
    promedio_acumulado=[]
    for i in range(len(y)):
        promedio_acumulado.append(suma_acumulada[i]/(i+1))
    yy=promedio_acumulado
    print(yy[n-1]) # imprime utlimo valor estimado
    value_exp=np.repeat(0.5,n)
    plt.plot(n_,yy)
    plt.plot(value_exp)
    plt.show()
############## Calculo integral exp(x) de 0 a 1 ###################
def monte_carlo_integral_exp(n=250): 
    U = []
    for i in range(n):
        U_i = rd.random()  # U_i ~ U(0,1)
        U.append(U_i)   
    g_U = []
    for i in range(n):
        g_U_i = np.exp(U[i])  # g(U_i)
        g_U.append(g_U_i) 
    S = []
    suma = 0
    for i in range(n):
        suma += g_U[i]
        S.append(suma)   
    theta = []
    for k in range(n):
        theta.append(S[k] / (k+1))
    # Valor final:θ_n
    print("Estimación final de la integral:", theta[-1])
    # convergencia
    n_index = range(1, n+1)  # 1,2,...,n
    theta_exacta = np.repeat(np.exp(1)-1, n)
    
    plt.plot(n_index, theta, label="Promedio acumulado")
    plt.plot(n_index, theta_exacta, label="Valor exacto")
    plt.xlabel("Número de muestras")
    plt.ylabel("Estimación de la integral")
    plt.title("Convergencia Monte Carlo")
    plt.legend()
    plt.show()
############## Calculo integral exp(x**2 +x) de -2 a 2 ###################
def monte_carlo_exp2(n=500):
    y = []
    for i in range(n):
        U_i = 4*rd.random() - 2
        g_U_i = 4 * np.exp(U_i**2 + U_i)
        y.append(g_U_i)
    n_ = range(1, n+1)
    S = []
    suma = 0
    for i in range(n):
        suma += y[i]
        S.append(suma)
    yy = []
    for k in range(n):
        yy.append(S[k] / (k+1))
    print("Estimación final de la integral:", yy[n-1])
    plt.plot(n_, yy, label="Promedio acumulado")
    plt.xlabel("Número de muestras")
    plt.ylabel("Promedio acumulado / estimación")
    plt.title("Convergencia Monte Carlo")
    plt.legend()
    plt.show()
def integral_otroo():
    y=[np.exp(np.random.rand()) for i in np.arange(n)]
    n_=np.arange(1,n+1)
    y_=np.cumsum(y)/n_
    print(y_[n-1]) # imprime utlimo valor estimado
    value_exp=np.repeat(1.7172,n)
    plt.plot(n_,y_)
    plt.plot(value_exp)
    plt.show()
#####
def integral_exp(n=10000):
    y = []
    for i in range(n):
        u = rd.random()
        g = np.exp(u)
        y.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += y[i]
        promedio_acumulado.append(suma/(i+1))
    print("Estimación final integral e^x:", promedio_acumulado[-1])
    return promedio_acumulado[-1]

# 4. Integral ∫ (1 - x^2)^(3/2) dx de 0 a 1
def integral_1_minus_x2_32(n=10000):
    y = []
    for i in range(n):
        u = rd.random()
        g = (1 - u**2)**(3/2)
        y.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += y[i]
        promedio_acumulado.append(suma/(i+1))
    print("Estimación final integral (1-x^2)^(3/2):", promedio_acumulado[-1])
    return promedio_acumulado[-1]

# 5. Integral ∫ x e^(x^2) dx de 0 a 2
def integral_x_exp_x2(n=10000):
    y = []
    for i in range(n):
        u = rd.random()
        x = 2*u
        g = x * np.exp(x**2)
        y.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += y[i]
        promedio_acumulado.append(suma/(i+1))
    print("Estimación final integral x e^(x^2):", promedio_acumulado[-1])
    return promedio_acumulado[-1]

# 6. Integral ∫ x / (1+x^2)^2 dx de 0 a ∞
def integral_x_1_x2_2(n=10000):
    y = []
    for i in range(n):
        u = rd.random()
        x = np.tan(np.pi*u/2)
        g = x / (1 + x**2)**2
        y.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += y[i]
        promedio_acumulado.append(suma/(i+1))
    print("Estimación final integral x/(1+x^2)^2:", promedio_acumulado[-1])
    return promedio_acumulado[-1]

# 8. Integral ∫∫ e^(x+y) dydx de 0 a 1
def integral_e_x_y(n=10000):
    y = []
    for i in range(n):
        u1 = rd.random()
        u2 = rd.random()
        g = np.exp(u1 + u2)
        y.append(g)
    suma = 0
    promedio_acumulado = []
    for i in range(n):
        suma += y[i]
        promedio_acumulado.append(suma/(i+1))
    print("Estimación final integral  e^(x+y):", promedio_acumulado[-1])
    return promedio_acumulado[-1]

# 10. Cov(U, e^U) con U uniforme (0,1)
def cov_U_expU(n=10000):
    U = []
    expU = []
    for i in range(n):
        u = rd.random()
        U.append(u)
        expU.append(np.exp(u))
    mean_U = sum(U)/n
    mean_expU = sum(expU)/n
    cov = sum((U[i]-mean_U)*(expU[i]-mean_expU) for i in range(n)) / (n-1)
    print("Cov(U, e^U):", cov)
    return cov

# 11. E[√(1-U^2)] y E[U*√(1-U^2)]
def integral_11(n=10000):
    U = []
    for i in range(n):
        u = rd.random()
        U.append(u)
    a = sum(np.sqrt(1 - u**2) for u in U)/n
    b = sum(u*np.sqrt(1 - u**2) for u in U)/n
    print("E[√(1-U^2)]:", a)
    print("E[U√(1-U^2)]:", b)
    return a, b

# 12. N = mínimo n tal que sum(U_i) > 1
def simulacion_12(reps=1000):
    resultados = []
    for _ in range(reps):
        s = 0
        n = 0
        while s <= 1:
            s += rd.random()
            n += 1
        resultados.append(n)
    E_N = sum(resultados)/len(resultados)
    print(f"E[N] con {reps} repeticiones:", E_N)
    return E_N

# 13. N = máximo n tal que sum(U_i) <= 3
def simulacion_13(reps=10000):
    resultados = []
    for _ in range(reps):
        s = 0
        n = 0
        while s <= 3:
            s += rd.random()
            n += 1
        resultados.append(n)
    E_N = sum(resultados)/len(resultados)
    probs = [resultados.count(i)/reps for i in range(7)]
    print("E[N]:", E_N)
    print("P{N=i} para i=0..6:", probs)
    return E_N, probs

if __name__=='__main__':
    #lanzar_moneda()
    #monte_carlo_integral_exp()
    #monte_carlo_exp2()
    integral_exp()
    integral_1_minus_x2_32()
    integral_x_exp_x2()
    integral_x_1_x2_2()
    integral_e_x_y()
    cov_U_expU()
    integral_11()
    simulacion_12(100)
    simulacion_12(1000)
    simulacion_12(10000)
    simulacion_13(10000)

