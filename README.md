#  pregunta 1
piden calcular la integral con limites 0 → infinito , para usar numeros aleatorios y calcular esa integral se necesita que los limites sean 0 → 1 , para luego aplicar la definicion usando una distribucion uniforme y usar U como los x's , de modo que integral = E(g(U))
y entonces aplica la ley fuerte de los grandes numeros que simplificando es : la media = ponderado de las variables aleatorias.
como se hizo en clase, para una integral 0→1 se generan los u se calcula el g(u) se suma y se divide entre n, y esa seria la integral.

para el caso de tener limites de 0 → infinito se hace la transformacion y= 1/(x+1) de modo que cuando x= 0  y =1

u cnado x→ infinito  y =1


# pregunta 2
# CASO DISCRETA
## Transformada inversa caso continuo
Tenemos la funcion de masa `
``P(X=xj) = pj ``osea la probabilidad que de que X sea xj para cada j  , y como P es funcion de masa funcion de probabilidad : SUMA pj = 1<br>

Se genera un numero aleatorio ``U(0,1)`` y se hace la CONSTRUCCION (es una construcción) <br>
-  X=x0 si U<p0
- X=x1 si p0<= U < p0 + p1
- X=xj si p0 +p1..pj-1<= U < p0 +p1+..pj-1 +pj
Es una construccion es asi como se define<br>

y del hecho que estamos usando una Uniforme en (0,1) podemos hacer ``P(a<U<b) = P(U<b) - P(U<a) = b - a ``
luego
```bash
P(p0 +p1 +  pj-1 <= U < p0 +p1 +pj-1 + pj)  = 
Usando la propiedad
P(U< p0 +p1 +..+ pj-1 +pj) - P(U<= p0+p1+..pj-1) =
como U es uniforme 
p0+p1 ..pj-1+pj     -     p0 +p1 +..pj-1 =  pj
Entonces 
P(p0 +p1 +  pj-1 <= U < p0 +p1 +pj-1 + pj) = pj 
Entonces X asi construida tiene la distribucion buscada
Además 
genrando un U si U< p0 +p1 ..pj  entonces X=xj
tenemos que p0+p1+..pj = SUMA pj = F(xj) Acumulada
entonces F(xj-1)<=U <F(xj)  entonces hacer X=xj
```
Entonces generamos un numero aleatorio U(0,1)
y luego determinamos el valor de x mediante
```bash
Si se cumple  F(xj-1)<=U<F(xj)  entonces hacer que X=xj
```
el intervalo en el que esta U . Pero porque se menciona la inversa?<br>
La intuicion es que tomando las inversas
```bash
F(xj-1) <=U  < F(xj)
xj-1 <= F-1(U) < xj    →  X=xj
pero en el caso discreto
F-1(u) =xj es el menor tal que F(xj)>= u
luego u cae en F(xj-1)<=u<F(xj)
```
O más simple X=xj si u cae en ese intervalo, es la versión discreta de la inversa<br>

Luego el algoritmo
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
Un caso en el que no es necesario buscar el intervalo donde se encuentra el número aleatorio es cuando la variable aleatorio de interes es la uniforme<br>
Queremos generar 
```bash
x´s  entre 1→n con p(X=j) = 1/n  j:1→n
Del resultado anterior 
Suma pj-1 <= U < Suma pj   →  X=xj
pero las probabilidades son 1/n
j-1/n <= U < j/n
X será igual a j si 
j-1 <= U*n < j
En otras palabras 
x = Ent(nU) + 1  
```

Esto ultimo no se entiende del todo <br>
Se tiene que si ``j-1/n <= U <j/n``   Entonces X=xj  = j en el caso uniforme 
pero se tenia que U(0,1) valores entre 0 y 1<br>
Entonces X deberia tomar valores en (0,1)? no , pues U y X no comparten dominio<br>
Son variables distintas, eso por una lado, por lo que x=j  perfectamente<br>

Pero luego como al multiplicar y tener ``j-1<=Un<j`` llegamos a la asignacion X=j con x= int[nU] +1<br>

```bash
X ~Unif{1,2,...n}
j-1/n <= U < j/n  → X=j
el intervalo[0,1] solo te da el indice 

j-1 <=Un < j
la variable 'Un' vive en [0,n] la desigualdad dice nU cayó en [j-1],j)
por ISNPECCION j = [nu] + 1 

Si nU esta en [0,1) → [nu] =0   → j=1
si nU esta en [1,2) → [nu] =1   → j=2
.....
```
### Ejemplo 4b
Generacion de permutacion aleatorio
Se va a generar una permutacion aleatoria de n numeros, 1→n. <br>
- elegir uno de los n numeros y se coloca en la posicion n
- elegir uno de los n-1 restantes y colocarlos en la posicion n-1 
....

Pero en lugar de usar los numeros , lo que se hace es usar el indice de la lista donde estan guardados.<br>

- Se comienza con P1,P2, ...Pn INICIAL
- luego se elige una de las n posiciones al azar, ej k e intercambiar Pk←→ Pn <br>
- Escoger otro indice e intercambiar con Pn-1
......

```bash
1. P1, P2 ...inicial ej Pj=j
2. k ← n
3. generar i = Ent(kU) + 1
4 .Pi←→Pk
5  k ← k-1  si k>1 ir a paso 3
6. permutacion deseada1 
```



## Metodo aceptacion-rechazo
Que se busca?<br>
Se tiene una distribucion de probabilidad,con sus propiedades , sus funciones de masa, suma *p=[p1,p 2,...] = 1 * <br>
Y se quiere  obtener(simular) la variable aleatoria que corresponda a esa distribucion.<br>
Pero usualmente la distribucion que tenemos es dificil , entonces como generamos esos valores?

1. Nos valemos de una conocida , q(x) de modo que este "cubra" a p(x) para todo x.Esto es que existirá c de modo que : ``p(x) <= c * q(x)``  por que asi ?
pues si vemos las barras de p son dificiles , pero las barras de q son faciles , conocidas, entonces c*g(x) esta por encima de las barras de p , conteniendola por completo entonces<br>
Osea tenemos una variable aleatoria y su distribucion de probabilidad contendiendo a conteniendo a p de modo que podemos trabajar para hallar sus x.

2. Lo anterior fue el prerequisito  o la condicion matematica, por decirlo de algun modo 
- Simular Y, es decir, obtener de forma aleatoria ese Y, del conjunto de valores de la variable aleatoria, Y ~ q.<br>
Esto es que,tenemos la condicion y generamos un Y , ahora usaremos ese Y y un MECANISMO DE ACEPTACION ("moneda") para decidir si ese Y corresponde a Y~p  o no<br>
como ??? <br>
-  La regla de aceptacion es ``U <= a(Y)`` entonces aceptas y haces X=Y
A ver esta regla tambien es una "propuesta" similar a la constuccion hecha para la transformada inversa.<br>
La regla es a(x)= ?  debe funcionar de modo que P(salida=x) DP p(x)<br>
Ver que el evento de que el algoritmo devuelva x es :<br>
Ex = {Y=x} y {U<=a(x)}<br>
tomando la probabilidad conjunta y como  Y y U son independientes<br>
P(salida = x) = P(Y=x y U<=a(x))<br> 
P(salida = x) = P(Y=x) P(U<=a(x))<br>
P(salida = x) = q(x) a(x)   ↑ U es uniforme
→ entonce necesitamos un a() de modo que P(salida =x) sea proporcional p()<br>
si hacemos a() = p()/cq() y reemplazamos<br>
P(Salida=x) = q(x) p(x) / c q(x)
            = p(x)/c <br>
Entonces ``U<= p(Y)/c q(Y)`` es la regla buscada.




## Metodo de composicion
Supongamos que tenemos un metodo eficiente para generar (simular) el valor de una variable aleatoria con una de las dos funciones de masa de probabilidad 
```bash
{p1j, j>= 0}  {p2j, j>=0}
```
y queremos simular el valor de la variable aleatoria X con funcion de masa 
```bash
P(X=j) = alphap1j + (1 - alpha)p2j   j>=0
```
Entonces si X1 tiene funcion de masa p1j y X2 tiene funcion de masa p2j<br>
Definimos :
```bash
   X1 con probabilidad alpha
X =
   X2 con probabilidad 1 - alpha
```
tendra su funcion de masa ``P(X=j) = alphap1j + (1 - alpha)p2j``
Esto implica que para generar el valor de tal variable aleatorio<br>
Primero generamos generamos una U y luego <br>
un valor de X1 si U < alpha <br>
y de X2 si U > alpha


# CASO CONTINUO
## Transformada inversa
Sea una variable aleatorio uniforme en (0,1) . Para cualquier funcion de distribucion continua F , es invertible, la variable aleatoria  X <br>
X = F^-1(U) tiene distribucion F <br>
F^-1 se define como el valor de x tal que F(x) =u

