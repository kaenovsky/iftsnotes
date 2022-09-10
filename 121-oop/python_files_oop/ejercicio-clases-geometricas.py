import math

# Defino la clase Figura

class Figura():
	def __init__(self, color_fondo:str) --> Figura:
		self.color_fondo = color_fondo
		print('Inicializando la Figura')
		
	def area(self, base:float, altura:float) --> Float:
		base = self.base
		altura = self.altura
		return base * altura

class Circulo(Figura) --> Figura;
	
	def __init__(self, radio:float) -> Circulo:
		self.base = base
		
	def area(base,altura):
		print("soy el area")
		

class Rectangulo(Figura) -> Figura:
	def __init__(self, base:float, altura:float) -> Rectangulo:
		self.base = base
		self.altura = altura

class Triangulo(Figura) --> Figura:
	def __init__(self, base:float, altura:float) -> Triangulo:
		self.base = base
		self.altura = altura
		
def main():
	
