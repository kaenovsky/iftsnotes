## Proyecto Final

Voy ampliando la idea del proyecto en base a lo planteado en el texto anterior (ver en `./07-clase-221.md`).
En función de lo propuesto en el pdf con los requisitos del sistema fui adaptando el proyecto para que tenga 3 apps, 10 urls y 3 ABM. También una parte del sistema estará restringido para usuario administrador.

<img src="https://upload.wikimedia.org/wikipedia/commons/6/61/Dajia-shuo-Putonghua-2817.jpg" alt="pared en hong kong con caracteres chinos y pinyin" width="420"/>

---

### chinobasico.ar 

El nombre del proyecto es Chino básico, ya que se trata de una web donde conoceremos algunas particularidades del idioma con más hablantes nativos del mundo.

 #### Rutas
 
 Páginas estáticas:
 
 - /home
 - /about
 - /stats
 - /docs

Estas páginas van a mostrar información estática. Paso a comentar cada una brevemente.

**Home**: Página principal donde se da la bienvenida al usuario y se linkea a las demás secciones.

**About**: Acerca del proyecto, cómo surgió y cómo planeo continuarlo.

**Stats**: Estadísticas actuales del sitio como ser cantidad de palabras cargadas en la BD, visitas del día, palabras anteriores.

**Docs**: Documentación del sitio explicando cómo acceder al panel de administrador y cargar palabras

Páginas dinámicas:

- /wod
- /last_words
- /pinyin
- /tones
- /han
- /nihao

Estas páginas van a tener información y al mismo tiempo el usuario va a poder interactuar con las páginas.

**Wod**: La palabra del día. Una vez por día, a las 00hs, se tomará una palabra de la BD y se mostrará en la url correspondiente junto con su traducción al español y su escritura en pinyin. Al cambiar la palabra al día siguiente, la palabra actual se guardará en la tabla de palabras pasadas.

**LastWords**: Las últimas 10 palabras que pasaron por "la palabra del día". A futuro se podría implementar un sistema de votación.

**Pinyin**: Esta página mostrará la escritura en Pinyin (una simplificación de los caracteres chinos para usar el abecedario latino) mediante un juego donde debemos elegir la opción correcta entre 3 opciones.

**Tones**: Explicación didáctica de los distintos tonos que tiene cada palabra, dependiendo de esto cambia el significado. Para mostrarlo se verá una palabra con distintos tonos, el audio estará alojado en un bucket s3 y la información se buscará de la BD.

**Han**: Explicación didáctica de los caracteres chinos, su historia y evolución. Los caracteres van a ser almacenados en la BD.

**Nihao**: Nihaho significa "Hola", y es donde empieza toda comunicación. Esta página es un formulario de contacto.

---

### ABM

El sistema va a contar con 3 páginas con la posibilidad de ejecutar Altas-Bajas-Modificaciones. Esto sólo será visible para el usuario administrador. Las vistas que permitirán esto son:

- Palabras
- Caracteres (han)
- Artículos de la documentación