### Práctica mysql
Usando BD sakila.sql -> [Descargar acá](https://dev.mysql.com/doc/sakila/en/)
  
Realizar los siguietes Ejercicios:

1. Traer el actor_id, first_name, last_name de la tabla actor.

```
SELECT actor_id, first_name, last_name FROM actor;
```

2. Asignar alias en el atributo actor_id de la tabla actor.

```
SELECT actor_id AS 'id del actor' FROM actor;
```

3. Traer los distintos id de las tiendas.  

```
SELECT DISTINCT store_id FROM store;
```

4. traer los distintos nombres de las tiendas.

```
SELECT DISTINCT * FROM store;
```

5. Ordenar de manera ascendente por country en la tabla country

```
SELECT country FROM country ORDER BY country ASC;
```

5-b. Ordenar de manera descendente por country en la tabla 

```
SELECT country FROM country ORDER BY country DESC;
```

6. Consulta store_id, first_name y last_name de la tabla customer de la base de datos sakila.  

```
SELECT store_id, first_name, last_name FROM customer;
```

7. Cambia el nombre de las columnas store_id, first_name y last_name a Tienda, Nombre y Apellido respectivamente de la tabla customer  

```
SELECT
store_id AS 'Tienda',
first_name AS 'Nombre',
last_name AS 'Apellido'
FROM customer;
```

8. Ordena de manera descendente la columna Apellido en la consulta 7

```
SELECT
store_id AS 'Tienda',
first_name AS 'Nombre',
last_name AS 'Apellido'
FROM customer
ORDER BY last_name DESC;
```

9. ¿Cuál es la cantidad más baja y más alta de la columna amount de la tabla payment?

```
SELECT
MIN(amount) AS 'Cantidad mínima',
MAX(amount) AS 'Cantidad máxima'
FROM payment;
```

10. traer los distintos precios y ordenarlo de manera Ascendente por amount  en la tabla payment

```
SELECT DISTINCT
amount AS 'precios'
FROM payment 
ORDER BY amount ASC;
```

11. Traer. todos los registros en la tabla actor donde el nombre es igual a ED  

```
SELECT * FROM actor WHERE first_name = 'ED';
```

12. Traer todos los registros  en la tabla city donde la city es igual a london  

```
SELECT * FROM city WHERE city = 'london';
```

13. Traer todos los registros en la tabla city donde country_id = 102  

```
SELECT * FROM city WHERE country_id = 102;
```

14. Traer todos los registros  en la tabla inventory donde film_id sea mayor o igual a 50  

```
SELECT * FROM inventory WHERE film_id >= 50;
```

15. traer solo los precios distintos de la tabla payment donde el amount sea menor a 3 y ordernarlos de manera descendente por el amount

```
SELECT DISTINCT amount
FROM payment
WHERE amount < 3
ORDER BY amount DESC;
```

16. traer todos los datos del staff donde el staff_id sea distinto de 2  

```
SELECT * FROM staff WHERE staff_id != 2;
```

17. traer todos los idiomas que sean distintos de German en la tabla language  

```
SELECT name AS 'idiomas'
FROM `language`
WHERE language_id != 6;
```

18. traer description, release_year de la tabla film y Filtrar la información donde title sea IMPACT ALADDIN*/    

```
SELECT description, release_year
FROM film
WHERE title = 'IMPACT ALADDIN';
```

19. Consulta la tabla payment de la base de datos sakila.  
Filtra la información donde amount sea mayor a 0.99 y ordenarlo de manera desc

```
SELECT * FROM payment 
WHERE amount > 0.99 
ORDER BY amount DESC;
```

20. Traer todos los registros en la tabla country donde el country sea igual a Algeria y ademas el country_id = 2 

```
SELECT * FROM country 
WHERE country_id = 2 
AND country = 'Algeria';
```

21. Traer todos los registros en la tabla country donde el country sea igual a Algeria o el country_id = 12  

```
SELECT * FROM country 
WHERE country_id = 12 
OR country = 'Algeria';
```

22. Traer todos los registro en la tabla language  donde el language_id sea igual a 1 o el name = german  

```
SELECT *
FROM `language`
WHERE language_id = 1
OR name = 'German';
```

23. traer todos los registros en la tabla category donde no se encuentren el name Action  

```
SELECT * FROM category WHERE name != 'Action';
```
 
24. traer todos los registros en la tabla film donde el rating no sea PG  

```
SELECT * FROM film WHERE rating != 'PG';
```

25. traer todos los distintos tipos de rating y que no este contemplado el 'PG'  

```
SELECT DISTINCT rating 
FROM film 
WHERE rating != 'PG';
```

26. Filtra la información en la tabla payment  donde customer_id sea igual a 36, amount sea mayor a 0.99 y staff_id sea igual a 1 ordenarlos de manera ascendente por amount.

```
SELECT * 
FROM payment 
WHERE customer_id = 36
AND staff_id = 1
ORDER BY amount ASC;
```

27. Traer todos los nombres donde sean Mary y Patricia de la tabla customer

```
SELECT first_name AS 'nombre' 
FROM customer 
WHERE first_name = 'Mary'
OR first_name = 'Patricia';
```

28. Traer todos los registros de la tabla film donde las caracteristicas especiales sea Trailer y Trailer,Deleted Scenes, ademas el rating tiene que ser G y R y el tiempo de duracion tieneque ser mayor a 50. Ordenarlos de manera ascendete por tiempo  

```
SELECT * 
FROM film
WHERE special_features
IN ('Trailers','Trailers,Deleted Scenes')
AND rating IN ('G','R')
AND `length` > 50
ORDER BY `length` ASC;
```

29. Traer todos los registros menos Action , Children , Animation de la tabla category

```
SELECT * 
FROM category 
WHERE name 
NOT IN('Action','Children','Animation');
```
  
30. Consulta la tabla film_text de la base de datos sakila. Filtra la información donde title  sea ZORRO ARK, VIRGIN DAISY, UNITED PILOT

```
SELECT *
FROM film_text
WHERE title IN('ZORRO ARK','VIRGIN DAISY','UNITED PILOT');
```

31. Consulta la tabla city de la base de datos sakila. Filtra la información donde city sea Chiayi, Dongying, Fukuyama y Kilis  

```
SELECT * 
FROM city 
WHERE city 
IN('Chiayi','Dongying','Fukuyama','Kilis');
```

32. BETWEEN: lo utilizamos para seleccionar valores dentro de un determinado rango. TRAER TODOS LAS RENTAS DONDE el customer_id SEAN DEL 300 AL 500, Y ADEMAS SEAN DEL STAFF_ID = 1. Ordenarlo de manera ASC por customer_id

```
SELECT * 
FROM rental
WHERE customer_id 
BETWEEN 300 AND 500
AND staff_id = 1
ORDER BY customer_id ASC;
```

33. Traer todos los registros de la tabla payment donde el monto sea entre 3 y 5 ordenar por amount de manera DESC  

```
SELECT * 
FROM payment
WHERE amount 
BETWEEN 3 AND 5
ORDER BY amount DESC;
```

34. Traer todos los registros de la tabla payment donde el monto no sea entre 3 y 5 ordenar por amount de manera DESC  

```
SELECT * 
FROM payment
WHERE amount 
NOT BETWEEN 3 AND 5
ORDER BY amount DESC;
```

35. Consulta la tabla payment de la base de datos sakila. Filtra la información donde amount esté entre 2.99 y 4.99, staff_id sea igual a 2 y customer_id sea 1 y 2.

```
SELECT * 
FROM payment
WHERE amount
BETWEEN 2.99 AND 4.99
AND staff_id = 2
AND customer_id IN(1,2);
```

36. Consulta la tabla address de la base de datos sakila. Filtra la información donde city_id esté entre 300 y 350

```
SELECT * 
FROM address
WHERE city_id
BETWEEN 300 AND 350;
```

37. Consulta la tabla film de la base de datos sakila. Filtra la información donde rental_rate esté entre 0.99 y 2.99, length sea menor igual de 50  y replacement_cost sea menor de 20.

```
SELECT * 
FROM film
WHERE rental_rate
BETWEEN 0.99 AND 2.99
AND `length` <= 50
AND replacement_cost < 20;
```

38. TRAER TODOS LOS REGISTROS  EN LA TABLA ACTOR, LOS NOMBRES QUE EMPIENCEN CON LA LETRA "A" Y EL APELLIDO EMPIECE CON LA LETRA "B"  

```
SELECT * 
FROM actor
WHERE first_name LIKE 'A%'
AND last_name LIKE 'B%';
```

39. TRAER TODOS LOS REGISTROS DONDE LOS NOMBRES TERMINEN CON LA LETRA "A" Y ADEMAS LOS APELLIDOS TERMINEN CON LA LETRA 'N'  

```
SELECT * 
FROM actor
WHERE first_name LIKE '%A'
AND last_name LIKE '%N';
```

40. TRAER TODOS LOS REGISTROS DONDE EL NOMBRE CONTIENE LA PALABRA "NE" EN CUALQUIERA DE SUS POSICIONES Y ADEMAS QUE TENGA EL APELLIDO LA PALABRA "RO".

```
SELECT * 
FROM actor
WHERE first_name LIKE '%NE%'
AND last_name LIKE '%RO%';
```

41. TRAER TODOS LOS REGISTROS DONDE TODOS LOS NOMBRES EMPIECEN CON "A" Y TERMINEN CON "E"  

```
SELECT * 
FROM actor
WHERE first_name LIKE 'A%E';
```

42. TRAER TODOS LOS REGISTROS DONDE LOS NOMBRES EMPIECEN CON LA LETRA "C" Y TERMINEN CON "N" Y ADEMAS QUE EL APELLIDO EMPIECE CON LA LETRA "g" 

```
SELECT * 
FROM actor
WHERE first_name LIKE 'C%N'
AND last_name LIKE 'G%';
```

43. Consulta la tabla film de la base de datos sakila. Filtra la información donde release_year sea igual a 2006  y title empiece con ALI.

```
SELECT * 
FROM film
WHERE release_year = 2006
AND title LIKE 'ALI%';
```