from abc import ABC, abstractmethod

class Dao(ABC):
	
	# metodos de la clase abstracta DAO
	
    @abstractmethod    
    def conectar_bd(nombre_bd):
	    pass
	
    @abstractmethod		
    def crear_tabla(nombre_tabla):
        pass
			
    @abstractmethod
    def insertar_objeto(objeto):
        pass
		
    @abstractmethod
    def seleccionar_objeto(id):
        pass
		
    @abstractmethod
    def eliminar_objeto(objeto):
        pass
		
    @abstractmethod
    def modificar_objeto(objeto, valores):
        pass
