# tarea: crear una clase Persona con atributos y metodos

class Persona:
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_edad(self):
        return self.edad
    
    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

magno = Persona('Alejandro', 37, '29245680')
cesar = Persona('Julio', 21, '20245680')

print('La edad de {} es {}. Su DNI es {}'.format(magno.nombre,magno.mostrar_edad(),magno.dni))
print('La edad de {} es {}. Su DNI es {}'.format(cesar.nombre,cesar.mostrar_edad(),cesar.dni))