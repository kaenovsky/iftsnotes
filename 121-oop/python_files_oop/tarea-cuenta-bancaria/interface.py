from abc import ABC, abstractmethod

class Dao(ABC):
	
	# metodos de la clase abstracta DAO
	
    @abstractmethod    
    conectar_bd(nombre_bd):
		pass
	
	@abstractmethod		
	crear_tabla(nombre_tabla):
		pass
			
	@abstractmethod
	insertar_objeto(objeto):
		pass
		
	@abstractmethod
	seleccionar_objeto(id):
		pass
		
	@abstractmethod
	eliminar_objeto(objeto)
		pass
		
	@abstractmethod
	modificar_objeto(objeto, valores):
		pass
