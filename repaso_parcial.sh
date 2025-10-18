#!/usr/bin/env bash 
umask 027
set -o errexit 
set -o pipefail 

OPCION_1="$1"
OPCION_2="$2"
OPCION_3="$3"
OPCION_4="$4"
OPCION_5="$5"
OPCION_6="$6"
binomial(){
    echo -e "VARIABLE BINOMIAL\n
    P(X=i) = (n i) * p^i * (1- p)^(n-i)\n\
    Resultados importantes\n
    - (1,p) es una bernoulli p^x * (1-p)^1-x con x={0,1}\n\
    - X es variable binomial (n,p) representa el numero de exitos en n ensayos independientes\n\
      cada uno de los cuales tiene exito con probabilidad p,\n
      X = \U2211 Xi   ; Xi = { 0 , 1 exito}; i:1→n\n
      Ensayo-----------Xi\n
        1               1\n
        2               0\n
        3               1\n
        4               1\n
        X = 1 +0+1+1= 3\n
        Resultado particular de la variable aleatoria X"
}

poisson(){
    echo -e "POISSON\n\
    P(X=k) = e^-\U03BB* \U03BB ^i /i!\n \
    partir de la binominal y hacer \U03BB = n*p   p=\U03BB/n
    reemplazar en la funcion de masa de la binomial\n\
    considerar n →\U221D entonces (1-\U03BB/n)^n = e^-\U03BB \n
    y (1-\U03BB/n)^i = 1 y el coeficiente factorial /n^i = 1
    entonces se oobtendra la funcion de masa de poisson"
}

geometrica_esperanza(){
    echo -e "n intentos hasta conseguir el primer exito\n\
    p(x) = p (1-p)^n-1 , pues n-1 fracasos y 1 exito\n\
    la esperanza es \U2211 n * p*(1-p)^(n-1)  n:1→\U221D\n
    p \U2211 n *(1-p)^(n-1) n:1→\U221D \n\
    ver que el argumento de la sumatoria tiene la forma de una derivada 
    "
    echo -e "p \U2211 \U2202 (1-p)^(n) , respecto a 1-p, n:1→\U221D\n\
    p<1 , 1-p < 1 , la suma de los terminos de una progresion geometrica de razon <1 \n
    \U2211 (1-p)^n  = 1 /(1 -(1-p)) - 1  n:1→\U221D \n
    Ademas \U211 y \U2202 son operadores lineales entonces\n
    p \U2202 \U2211 (1-p)^n y aplicando lo anterior\n
    p \U2202 1 / (1 -(1- p)) - 1  ; \U2202 (1- p)"

    echo -e "si 1-p = m , entonces \n
    p \U2202 (1/1-m -1)   ; \U2202 (m)\n
    ahora si 1-m = l ; -dm = dl \n
    p -\U2202 (1/l -1) ; \U2202(l)\n
    p--1/l^2   =  p 1/l^2  = p/(l^2)\n"

    echo -e "como 1- m = l ; 1 -(1-p) =l = p\n
    p/(p^2) =  1/p \n
    por lo que la esperanza de la geometrica es 1/p"
}

uniforme(){
    echo -e "VARIABLE ALEATORIA UNIFORME\n\
    P(X=x) = 1/(b-a)  ; a<x<b\n
    P(X<=x) = x-a/(b-a)\n
    "
}

exponencial(){
    echo -e "EXPONENCIAL\nf(x) = \U03BB e^-(\U03BB x)\n
    P(X<=x) = F(x) = 1 - e^-(\U03BB)x\n
    E(X)= 1/\U03BB \n
    P(X>s+t| X>s) = P(X>t)\n
    P(X>s \U002B t )= P(X>s)P(X>t)\n
    P(cX<x) = P(X<x/c) = 1 - e^(-\U03BB x/c)"
}
proceso_poisson(){
    echo -e "PROCESO DE POISSON\n
    1)Que esta modelando\n
    Imaginamos que observamos eventos aleatorios\n
    que ocurren en el tiempo :\n
    - llamadas a un call center\n
    - clientes entrando a una tienda\n
    - fallas en una maquina\n
    Lo que el proceso hace es contar cuantos eventos han ocurrido hasta el instante t\n
    N(t) = numero de eventos ocurridos en [0,t]\n
    2)Cuando decimos que es un proceso de poisson\n
    N(t) se llama poisson de tasa \U03BB >0 si\n
        - N(0) = 0\n
        - Incrementos independientes, lo que pasa en [0,1] no afecta a lo que pasa en [1,2]\n
        - incrementos estacionarios,la probabilidad de ver 2 eventos(ej)en 3 minutos es la misma \
        sin importar donde empieze el intervalo, solo depende de la longitud\n 
        - En un intervalo pequeño de longitud h la probabilidad es \U03BB h\n
        - En ese mismo intervalo la probabilidad de 2 o mas eventos es 0\n
    3) Con estas 5 propiedades N(t) ~ Poisson(\U03BB t)
    4) que significan los tiempos X1,X2....\n
        X1, X2, son las longitudes entre las ocurrencias de los eventos\n
    5) Como se deduce que esos tiempos son exponenciales\n
        la clave esta en \n
        X1 > t , significa que no ocurrio nigun evento en [0,t]\n
        P(X1 > t) = P(N(t) = 0) \n
        Pero sabemos N(t)~Poisson(\U03BB t)\n
        P(N(t)=0) = e^(-\U03BB t)\n
        esto es la funcion de supervivencia de la variable exponencial con parametro \U03BB\n
    6) y los siguientes tiempos?\n
        luego se usa b,c incrementos independientes y estacionarios\n
        - lo que ocurre despues del primer evento no depende de lo que paso antes\n
        - el proceso reinicia con la misma \U03BB\n
        por lo que X2,X3 ... tambien son exponenciales\n
        y desde luego independientes entre si
    7) Resultado importante\n
        eL proceso de poisson se puede describir de dos formas equivalentes\n
         enfoque        variable                distribucion
        - por conteo   N(t)= # de eventos hasta t   Poisson(\U03BB t)\n
        - por tiempos   Xi = tiempos entre llegadas    Exponencial(\U03BB)\n
        Y ambos enfoques estan conectados \n
        . Si sumamos las n exponenciales\n
         Tn = X1+ X2...Xn\n
         Tn ~ Gamma(n,\U03BB)
    "
}

integrales_aleatorias(){
    echo -e "\U04E9 = \U222B g(x) dx  ; x:0→1\n
    usamos la defincion de la esperanza \n
    \U222B g(x) fu(x) dx ; pero f = 1/b-a ; pero b=1 a=0 , f= 1\n
    E(g(x)) = \U222B g(x) ; ojo x es siempre la variable aleatoria. esta es la version extendida de la esperanza\n
    entonces tenemos \U04E9 = E(g(x))\n
    Ahora bien , solo se hace una especie de reinterpretacion \n
    \U04E9 = E(g(U))\n
    Y como sabemos que si U es V.A entonces g(x)\n
    tambien es VA de modo que entonces usamos la ley fuerte de los grandes numeros\n
    \U2211 G(Ui)/k → E(g(U)) = \U04E9   ; i:1→k" 
}

cambio_de_variables(){
    echo -e "CAMBIO a,b\n
    \U04E9 = \U222B g(x) , x:a→b\n
    transformando la variable muda\n
    restamos a  y dividimos entre b-a, las operaciones inversas al operando\n
    \U222B g(x(b-a) + a) (b-a) dx ; x:0→1\n
    "
    echo -e "CAMBIO \U221D\n
    \U222B g(x)dx  x:0→\U221D\n
    y = 1/(x+1) ; cuando x= 0  y = 1\n
                         x= \U221D  y = 0\n
    dy = -dx/(x+1)^2      despejando x= 1/y -1\n
    dx = -dy (x+1)^2 \n
    dx = -dy/y^2 \n
    reemplazando todo \U04E9 = \U222B -g(1/y -1)dy/y^2  y:1 → 0\n
    invertiendo el orden \n
    \U04E9 = \U222B g(1/y -1)dy/y^2  y:0 → 1\n
    "
}
if [ "$capitulo" -eq 2 ];then
    if [[ "$OPCION_1" == "binomial" ]];then 
        binomial     
    fi
    if [[ "$OPCION_2" == "poisson" ]];then
        poisson
    fi
    if [[ "$OPCION_3" == "esperanza de la geometrica" ]];then    
        geometrica_esperanza
    fi
    if [[ "$OPCION_4" == "uniforme" ]];then 
        echo ""
    if [[ "$OPCION_5" == "exponencial" ]];then
        exponencial 
    fi
    if [[ "$OPCION_6" == "proceso poisson" ]];then
        proceso_poisson
    fi
    else
        echo ""
    fi
fi

if [ "$capitulo" -eq 3 ];then      
    if [[ "$1" == "integrales aleatorias" ]];then
        integrales_aleatorias
    fi
    if [[ "$2" == "cambio de variable" ]];then
        cambio_de_variables
    fi
else    
    echo " "
fi