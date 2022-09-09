# tarea: crear una clase Persona con atributos y metodos

class Persona(object):
    def __init__(self, nombre:str, edad:int, dni:str):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_edad(self) -> int:
        return self.edad
    
    def es_mayor_edad(self) -> bool:
        if self.edad >= 18:
            return True
        else:
            return False

# creamos objetos del tipo Persona

magno = Persona('Alejandro', 26, '29245680')
cesar = Persona('Julio', 15, '20245680')
polo = Persona('Marco', 41, '34556780')

# guardamos las personas en una List y la recorremos

users = [magno, cesar, polo]

for u in users:
    if u.es_mayor_edad():
        res = 'sí'
    else:
        res = 'no'
    print('{} de {} años, DNI n° {}: {} es mayor de edad'.format(u.nombre, u.mostrar_edad(), u.dni, res))