'''
En un registro de 10 cursos
de 30 alumnos cada uno, obtener:

- Promedio de cada curso
- El curso que mayor promedio tiene
- El nombre del alumno que mayor nota obtuvo
y a qué curso pertenece
'''

import json
data = json.load(open('students.json', 'r'))

print("~~~~~ inicio del programa ~~~~~")

classroom = 1
avgDict = {}
topScoreStudents = {}
topScore = 0 

while(classroom < 11):
    
    avg = 0
    total = 0   

    for i in data['ctRoot']:
        
        if i['classroom'] == str(classroom):
            total = total + int(i['grade'])
        
        if int(i['grade']) > topScore:
            topScore = int(i['grade'])

    avg = total / 30
    avgDict.update({classroom : avg})
    print('La nota promedio del curso n° {} es {:.2f}'.format(classroom,avg))

    classroom = classroom + 1

topAvgGrade = max(avgDict.values())
topAvgClass = max(avgDict,key=avgDict.get)

print('El mejor promedio es {:.2f} (curso n° {})'.format(topAvgGrade,topAvgClass))
print()
print('~~~~~~~~~~~~')
print()

for i in data['ctRoot']:
    if int(i['grade']) == topScore:
        topScoreStudents.update({i['name'] : i['classroom']})

print('La mayor nota obtenida fue: ',topScore)
print('Quienes obtuvieron esa nota y sus cursos son: ',json.dumps(topScoreStudents, indent=4))

print("~~~~~ fin del programa ~~~~~")