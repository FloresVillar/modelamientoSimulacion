#  pregunta 1
piden calcular la integral con limites 0 → infinito , para usar numeros aleatorios y calcular esa integral se necesita que los limites sean 0 → 1 , para luego aplicar la definicion usando una distribucion uniforme y usar U como los x's , de modo que integral = E(g(U))
y entonces aplica la ley fuerte de los grandes numeros que simplificando es : la media = ponderado de las variables aleatorias.
como se hizo en clase, para una integral 0→1 se generan los u se calcula el g(u) se suma y se divide entre n, y esa seria la integral.

para el caso de tener limites de 0 → infinito se hace la transformacion y= 1/(x+1) de modo que cuando x= 0  y =1

u cnado x→ infinito  y =1


# pregunta 2
tenemos la funcion de masa P(X=xj) = pj osea la probabilidad que de que X sea xj para cada j  , y como es funcion de masa funcion de probabilidad SUMA pj = 1

Se genera un numero aleatorio ``U(0,1)`` y se hace la construccion 
-  X=x0 si U<p0
- X=x1 si p0<= U < p0 + p1
- X=xj si p0 +p1..pj-1<= U < p0 +p1+..pj-1 +pj
Es una construccion es asi como se define

y del hecho que estamos usando una Uniforme en (0,1) podemos hacer ``P(a<U<b) = P(U<b) - P(U<a) = b - a ``
luego
```bash
P(p0 +p1 +  pj-1 <= U < p0 +p1 +pj-1 + pj)  = pj
ademas 
de U< p0 +p1 ..pj  hacer X=xj
tenemos que p0+p1+..pj = SUMApj = F(xj) Acumulada
entonces F(xj-1)<=U <F(xj)  entonces hacer X=xj
```
Entonces generamos un numero aleatorio U(0,1)
y luego determinamos el valor de x mediante
```bash
F(xj-1)<=U<F(xj) X=xj
```
en el que esta U . Pero porque se menciona la inversa?
la intuicion es que tomando las inversas
```bash
xj-1<= F-1(U)<xj  X=xj
pero en el caso discreto
F-1(u) =xj es el menor tal que F(xj)>= u
luego u cae en F(xj-1)<=u<F(xj)
```
o mas simple X=xj si u cae en ese intervalo, es la version discreta de la inversa

luego el algoritmo
```bash
Generar U~ u(0,1)
if U<p0 then 
    X←xo
end
if p0 <U<p0+p1 then
    X←x1
end
if p0+p1<U<p0+p1+p2 then
    X←x2
end
.....
```

## Transformada inversa caso continuo

## Metodo aceptacion-rechazo
que se busca? se tiene una distribucion de probabilidad,con sus propiedades , sus funciones de masa, suma <br>
*p=[p1,p 2,...]* <br>
y se quiere  obtener(simular) la variable aleatoria que corresponda a esa distribucion .
<br>Pero usualmente la distribucion es dificil , entonces como generamos esos valores: 
1. nos valemos de una conocida , q(x) de modo que este "cubra" a p(x) para todo x.Esto es que existirá c de modo que :
    ``p(x) <= c * q(x)``  por que asi ?
    pues si vemos las barras de p son dificiles , pero las barras de q son faciles , conocidas, entonces c*g(x) esta por encima de las barras de p , conteniendola por completo entonces , osea tenemos una variable aleatoria y su distribucion de probabilidad contendiendo a conteniendo a p de modo que podemos trabajar para hallar sus x
2. 
    lo anterior fue el prerequisito  o la condicion matematica, por decirlo de algun modo 
    -simular Y es decir obtner de forma aleatoria ese Y, del conjutno de valores de la variable aleatoria, Y ~ q  
    - ahora ,tenemos la condicion y generamos un Y , ahora usaremos ese Y y un MECANISMO DE ACEPTACION "moneda" para decidir si ese Y corresponde a y~p como ? ? 
    generamos un U uniforme,
    y queremos un algoritmo que produzca valores con distribucion p(x),el algoritmo devuelve x con una probabilidad p(x)

    entonces se genera Y  q(x) entonces podemos aceptar o rechazar Y con probabilidad a(Y) 
    P(salida = x) = q(x) a(x)
    porque esta formula ? pues para que la salida sea x debe cumplirse
    Ex = {Y=x} {U<=a(x)}





