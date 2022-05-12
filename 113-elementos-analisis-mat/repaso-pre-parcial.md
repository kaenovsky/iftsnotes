### Repaso completo
Todos los temas del parcial, recopilados por un compañero (Demi)

Conjuntos: https://www.youtube.com/watch?v=YZRRUFG2UOY

Función Lineal: https://www.youtube.com/watch?v=09kcKGsSEbw

Función Cuadrática: https://www.youtube.com/watch?v=9Qu4fodFQG4

Función Polinomica: https://www.youtube.com/watch?v=co7E4VAHQR8

Función Exponencial: https://www.youtube.com/watch?v=gea1Wz-yMC0

Función Racional: https://www.youtube.com/watch?v=4PWf27vLNQs

Funciones Trigonométricas: https://www.youtube.com/watch?v=4tpi87_Y_y0

Función Inversa: https://www.youtube.com/watch?v=lfM_PBfIkvk

Vectores:

https://www.youtube.com/watch?v=xURTgxvG-3c (Suma Vectores en R2 y Gráfico)

https://www.youtube.com/watch?v=sqkni90xet0 (Suma Vectores en R3 Y Gráfico)

https://www.youtube.com/watch?v=vL8GIHsantM (Resta Vectores en R2 Y Gráfico)

https://www.youtube.com/watch?v=5Yj9EVLJXBM (Producto Escalar)

https://www.youtube.com/watch?v=fmAhi1N-uL8&t=361s (Producto Cruz de dos vectores)

---
#### Teoría de conjuntos:

[Simbolos a mano p/ copiar y pegar](https://www.disfrutalasmatematicas.com/conjuntos/simbolos.html)

intersección: ∩
unión: ∪

[Ejercicios primer video](https://www.youtube.com/watch?v=YZRRUFG2UOY)

Dado:

A = {1,2,3,4,5,6}
B = {2,4,6,8,10}
C = {5,6,7,8,9}

Encontrar

(A ∩ B) ∪ C 
[se lee A intersección B, unido con C]

(A ∩ B) = {2,4,6}
(A ∩ B) ∪ C = {2,4,5,6,7,8,9}

Encontrar

(A ∩ C) ∩ (B ∪ C) 
[se lee A intersección C, intersectado con B unión C]

(A ∩ C) = {5,6}
(B ∪ C) = {2,4,5,6,7,8,9,10}
(A ∩ C) ∩ (B ∪ C)  = {5,6}

2) Teoría de conjuntos / Operaciones combinadas:

[Ejercicios segundo video](https://www.youtube.com/watch?v=nOQ0Y0lfzwM)

Dado:

U = {a,b,c,d,e,f,g}
A = {a,b,c,d}
B = {a,c,e,g}
C = {b,e,f,g}

Aclaración: uso el símbolo ( ' ) para decir **complemento**, es decir los valores que le faltan a ese conjunto para completar el conjunto universal **(U)**. [En este link](https://www.disfrutalasmatematicas.com/conjuntos/venn-diagramas.html) lo llaman, "todo lo que **no** es" .

Encontrar

**Ejemplo 1:**

(B' ∪ C)'

B' = {b,d,f}
B' ∪ C = {b,d,e,f,g}
(B' ∪ C)' = {a,c}

**Ejemplo 2:**

(A ∪ B) ∩ (C' - A')

A' = {e,f,g}
C' = {a,c,d}
A ∪ B = {a,b,c,d,e,g}
C' - A' = {a,c,d}
(A ∪ B) ∩ (C' - A') = {a,c,d}

---

#### Función Lineal:
[Clase Mat CBC - Funciones](https://www.youtube.com/watch?v=09kcKGsSEbw)

`f(x) = m x + b`

![](113-assets/ppt-135-mat.png)

- Definición de función
- Definición de variable dependiente (y) e independiente (x)
- Pendiente (m)
- Ordenada al origen (b)

Pendiente me marca si la función es creciente, decreciente o constante (0)

m > 0 ---> Creciente
m < 0 ---> Decreciente
m = 0 ---> Constante

Graficar en el plano cartesiano una función lineal:

ejemplo con

`f(x) = 3/2 x - 1`

**Paso 1:** marco la ordenada al origen
**Paso 2:** me muevo con la  pendiente

La ordenada al origen me indica que la función va a cortar al eje Y en -1

![](113-assets/ppt-136-mat.png)

Con el método de este profe lo piensa así: me muevo 3 lugares hacia arriba y 2 hacia la derecha (porque la fracción es positiva, si fuera negativa, me muevo hacia la izquierda). El numerador me indica siempre ir hacia arriba y el denominador hacia los costados de acuerdo al signo de la pendiente.

![](113-assets/ppt-137-mat.png)

Explica los conceptos de Dominio, Imagen y Raices que aplica a todas las funciones:

- **Dominio:** Todos los valores que puede tomar X
En f(x) el dominio es R (todos los Números Reales)
- **Imagen:** Todos los valores de Y que tienen asociada a la función
- **Raíces:** (también llamado conjunto de 0) Intersección entre f(x) y el eje X

Cómo obtener la raíz de forma analítica? 
Llevando la función a 0 --> `f(x) = 0`

```
3/2 x - 1 = 0 
3/2 x = 1
x = 1 : 3/2

# dividir una fracción es lo mismo
# que multiplicar por su inverso
# entonces:

x = 1 . 2/3 

x = 2/3 (x es igual a 2 tercios)
```

En este caso "encontré el conjunto de ceros":
C 0 = { 2/3 }
