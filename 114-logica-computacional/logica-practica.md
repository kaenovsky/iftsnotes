## tabla de verdad

operadores lógicos (compartieron en grupo wpp)

![](114-assets/ppt-3-logic.png)

---

#### Guia actividades parte 2
Ejercicio 1

a) Complete la tabla de verdad de un multiplicador por 2 de números enteros positivos de 2 bits. 

b) Obtenga las funciones lógicas de P2, P1 y P0.


Resolviendo en clase con el profe:
[Ver en clase grabada](https://classroom.google.com/c/NDcxNzIwNTQ4MzY2/m/NDg2NzA2OTAwNjc2/details)

Resolvemos todos los números enteros (en sistema decimal) necesarios para la operación. Luego hace una explicación de cómo pasarlos a sistema binario.

![](114-assets/ppt-43-logic.png)


| A1 | A0 | P2 | P1 | P0 |  
|----|----|----|----|----| 
| 0  | 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 0  | 
| 1  | 0  | 1  | 0  | 0  |
| 1  | 1  | 1  | 1  | 0  |

Estaba ok :D

![](114-assets/ppt-42-logic.png)

#### Ejercicio 2 
Ejercicio 2 de guía de actividades - comprobando que funciona por maxiter y minter de ambas formas (minuto 56:00 clase 3 de mayo [https://classroom.google.com/c/NDcxNzIwNTQ4MzY2/m/NDg2NzA2OTAwNjc2/details](https://classroom.google.com/c/NDcxNzIwNTQ4MzY2/m/NDg2NzA2OTAwNjc2/details "https://classroom.google.com/c/NDcxNzIwNTQ4MzY2/m/NDg2NzA2OTAwNjc2/details")) 

**Comprobando por maxitérminos** 

```
P1 = ¬A1 x A0 + A1 x A0 

P1 = 1 x 1 + 0 x 1 

P1 = 1 + 0 

P1 = 1
```

**Comprobando por minitérminos** 

```
P1 = ¬A1 x A0 + A1 x A0 

P1 = 0 x 0 + 1 x 0 P1 = 0 + 0 

P1 = 0
```

#### Tabla de Karnaugh

(...)

#### Ejercicio 5
` f = ¬C . A + C . B `

![](114-assets/ppt-44-logic.png)

Necesitamos aplicar la propiedad distributiva, por eso usamos los 1 en forma de ` A + ¬A  ` y  ` B + ¬B `

Propiedad distributiva:

f = (¬C . B + ¬C . ¬B) . A + C . (B . A + B ¬A)

![](114-assets/ppt-45-logic.png)

Finalmente tiene que quedar:

` f = ¬C . B . A + ¬C . ¬B . A + C . B . A + C . B . ¬A `

