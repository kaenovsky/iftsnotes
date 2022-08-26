# Obtener los resultados de suma, resta, multiplicación y división
# a partir de dos números

print('~~~~~~~~~~')
print('Ingrese dos números para obtener los resultados')

num1 = float(input('Ingrese número 1: '))
num2 = float(input('Ingrese número 2: '))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2 

print('~~~~~~~~~~')
print('A continuación verá los resultados: ')
print()
print('la suma de {} + {} es igual a: {}'.format(num1,num2,suma))
print('la resta de {} + {} es igual a: {}'.format(num1,num2,resta))
print('la multiplicación de {} + {} es igual a: {}'.format(num1,num2,multi))
print('la división de {} + {} es igual a: {}'.format(num1,num2,divi))
print()
print('Fin del programa')