## ingresar notas de n examenes y obtener promedio

print("~~~~~ inicio del programa ~~~~~")
print()

i = 0
nota = 0
totalNotas = 0
cond = True

while(cond):

    nota = float(input("Ingrese nota nro {}: ".format(i+1)))

    ## validar que la nota no sea mayor a 10 ni menor a 0   

    while(nota > 10 or nota <= 0):        
        print("(!) error: ingrese notas entre 1 y 10")
        print()
        nota = float(input("Ingrese nota nro {}: ".format(i+1)))
    
    totalNotas = totalNotas + nota
    i = i + 1  # contador de ingresos  

    rta = input("Desea agregar otra nota (S/n): ")

    ## while para validar respuesta s/n

    while(rta != "n" and rta != "N" and rta != "s" and rta != "S"):
        print("(!) error: ingrese como respuesta Sí (s/S) o No (N/n)")
        print()
        rta = input("Desea agregar otra nota (S/n): ")

    if(rta == "n" or rta == "N"):
        print("#################################")        
        print("No se ingresan más notas.")
        print("#################################")
        cond = False

    ## si la respuesta es sí, continua el while loop

## fuera del loop, muestro resultado:

promedio = totalNotas / i
print("El promedio es: ", promedio)

print()
print("~~~~~ fin del programa ~~~~~")