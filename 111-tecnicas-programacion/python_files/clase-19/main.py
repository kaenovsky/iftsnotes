from funciones import ganador, ultimo, participantes
from funciones import mujeres, edadPromedioH, disparoPromedio
from funciones import promedioMejDisparo

cantPart = 0
concurso = []

while True:
    
    nroPart = int(input('Nro de participante: '))
    if nroPart == 999:
        break
    
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    edad = int(input('Edad: '))
    sexo = input('Sexo (f/m): ')
    disp1 = float(input('Disparo 1: '))
    disp2 = float(input('Disparo 2: '))
 
    dato = {
        'nroPart': '',
        'nombre': '',
        'apellido': '',
        'edad': '',
        'sexo': '',
        'disp1': '',
        'disp2': '',
        'mejorDisp': ''
        }
    
    dato['nroPart'] = nroPart
    dato['nombre'] = nombre
    dato['apellido'] = apellido
    dato['edad'] = edad
    dato['sexo'] = sexo
    dato['disp1'] = disp1
    dato['disp2'] = disp2
    
    if disp1 < disp2:
        dato['mejorDisp'] = disp1
    else:
        dato['mejorDisp'] = disp2
        
    #voy agregando diccionarios a mi lista
    concurso.append(dato) 
    
    
print(concurso)
ganador(concurso)
ultimo(concurso)
participantes(concurso)
mujeres(concurso)
edadPromedioH(concurso)
disparoPromedio(concurso)
promedioMejDisparo(concurso)



