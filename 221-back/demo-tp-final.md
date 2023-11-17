## Demo funcional

Muestro hasta donde llegué a hacer el proyecto. Falta un montón pero al menos tengo una estructura armada y dockerizada.

Temas a mostrar:

1. Repositorio
2. Árbol de directorios
3. Dockerización
4. Correr contenedor en la terminal
5. Entrar a vistas estáticas (basada en funciones)
6. Entrar a vista words (basada en clase)
7. Iniciar sesión (error y correcto) con `/accounts/login`
8. Cerrar sesión con `/accounts/logout`
9. Entrar por consola a Container
	1. Entrar a Shell
	2. Mostrar listado de palabras con `Word.objects.all()`
	3. Crear una nueva palabra
		1. Importar modelo con `from apps.words.models import Word`
		2. Crear palabra con `word3 = Word(en="water", es="agua", zw="水", pinyin="shui", pronun="demobucket.s3.linodeobjects.com")`
		3. Guardar palabra con `word3.save()`
	4. Mostrar palabras actualizadas en BD
 10. Mostrar código