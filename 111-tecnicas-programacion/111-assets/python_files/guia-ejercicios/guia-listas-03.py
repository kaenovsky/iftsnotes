"""
Escribir una función que, dado un número de DNI, 
retorne True si el número es válido y False si no lo 
es. Para que un número de DNI sea válido debe tener 
entre 7 y 8 dígitos.
"""

dniInput = int(input("Por favor ingrese su número de DNI: "))
dni = str(dniInput)
lenDni = len(dni)
print("Cantidad de digitos del DNI: {}".format(lenDni))

def validate(dni):
    if(lenDni != 7 and lenDni != 8 ):
        return False
    else:
        return True

isValid = validate(dni)

if(isValid):
    print("Este DNI es válido :) {}".format(dni))
else:
    print("(!) error: el DNI debe tener 7 u 8 dígitos")