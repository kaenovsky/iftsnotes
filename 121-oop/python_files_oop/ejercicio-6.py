from getSeconds.time import getSeconds

def askTime():
    hours = int(input('Ingrese horas: '))
    minutes = int(input('Ingrese minutos: '))
    seconds = int(input('Ingrese segundos: '))
    print('~~~~~~')
    answer = getSeconds(hours,minutes,seconds)
    return(answer)

def makeHour(totalSeconds):
    seconds = totalSeconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print('El total es {} horas, {} minutos y {} segundos'.format(hour,minutes,seconds))

i = 0
total = 0

while(i < 2):
    total = total + askTime()
    i = i + 1

print('El total en segundos es: ',total)

makeHour(total)