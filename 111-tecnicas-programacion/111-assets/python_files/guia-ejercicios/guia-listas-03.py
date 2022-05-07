"""
Escribir una función que, dado un número de DNI, 
retorne True si el número es válido y False si no lo 
es. Para que un número de DNI sea válido debe tener 
entre 7 y 8 dígitos.
"""

dniInput = int(input("Por favor ingrese su número de DNI: "))
dni = str(dniInput)
print("Cantidad de digitos del DNI: {}".format(len(dni)))

def validate(dni):
    if(len(dni) != 7 and len(dni) != 8 ):
        print("(!) error: el DNI debe tener 7 u 8 dígitos")
        return False
    else:
        print("Este DNI es válido :) {}".format(dni))
        return True

validate(dni)    