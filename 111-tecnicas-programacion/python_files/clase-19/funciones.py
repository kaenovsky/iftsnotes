
def ganador(concurso):
    
    mejorDisparo = 1000
    ganadorId = ''
    
    for item in concurso:
        if item['mejorDisp'] < mejorDisparo:
            mejorDisparo = item['mejorDisp']
            ganadorId = item['nroPart']
    
    for item in concurso:
        if item['nroPart'] == ganadorId:
            print("\nEl ganador es: ")
            print(item)
            break
        
    return


def ultimo(concurso):
    
    perdedor = 0
    perdedorId = ''
    
    for item in concurso:
        if item['mejorDisp'] > perdedor:
            perdedor = item['mejorDisp']
            perdedorId = item['nroPart']
    
    for item in concurso:
        if item['nroPart'] == perdedorId:
            print("\nEl perdedor es: ")
            print(item)
            break
        
    return


def participantes(concurso):
        
    cont = 0
    for item in concurso:
        cont = cont + 1
    
    print('Cantidad de participantes: ', cont)
    
    return
    

def mujeres(concurso):
    
    contF = 0
    for item in concurso:
        if item['sexo'] == 'f':
            contF = contF + 1
    
    print('Cantidad de mujeres: ', contF)
    
    return
    

def edadPromedioH(concurso):
    
    acum = 0
    contH = 0
    for item in concurso:
        if item['sexo'] == 'm':
            acum = acum + item['edad']
            contH = contH + 1
            
    print('Edad promedio de Hombres: {}'.format(acum/contH))
    
    return
    
    
def disparoPromedio(concurso):
    
    acum = 0
    cont = 0
    for item in concurso:
        acum = acum + item['disp1'] + item['disp2']
        cont = cont + 2
        
        
    print('Promedio de Disparos: {}'.format(acum/cont))
    
    return
        
        
def promedioMejDisparo(concurso):
    
    acum = 0
    cont = 0
    for item in concurso:
        acum = acum + item['mejorDisp']
        cont = cont + 1
        
    print('Promedio de mejores Disparos: {}'.format(acum/cont))
    
    return