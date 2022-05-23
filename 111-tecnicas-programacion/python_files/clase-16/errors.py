b = 0

while True:
	try:
		a = int(input("Ingrese valor: "))
		b = a / 10
	except ValueError:
		print("Debe ingresar un valor numerico")
	else:
		print("valor: ", b)

		if a == 0:
			break

print("saliendo del programa")