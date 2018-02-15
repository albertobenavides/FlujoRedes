from random import random
from math import sin, cos

alumnosTotales = 20
clasesTotales = 8
horariosTotales = 6
horarioProb = 0.2

rAlumnos = alumnosTotales / (2 * 3.14) * 3 # Radio para alumnos
aAlumnos = 2 * 3.14 / alumnosTotales

alumnosPos = list()
for a in range(alumnosTotales):
    alumnosPos.append(
        (rAlumnos * cos(aAlumnos * a), rAlumnos * sin(aAlumnos * a))
    )

rClases = alumnosTotales / (2 * 3.14) * 2 # Radio para clases (a partir del diámetro de alumnos)
aClases = 2 * 3.14 / clasesTotales

clasesPos = list()
for c in range(clasesTotales):
    clasesPos.append(
        (rClases * cos(aClases * c), rClases * sin(aClases * c))
    )

rHorarios = alumnosTotales / (2 * 3.14) # Radio para clases (a partir del diámetro de alumnos)
aHorarios = 2 * 3.14 / horariosTotales

horariosPos = list()
for h in range(horariosTotales):
    horariosPos.append(
        (rHorarios * cos(aHorarios * h), rHorarios * sin(aHorarios * h))
    )

clasesInteres = list()
alumnosClases = list()
clasesHorarios = list()

print("set terminal png")
print("set output 'horarios.png'")
print("set key off")
print("set size square")
print("unset colorbox")

for c in range(clasesTotales):
    clasesInteres.append(random()) # Se agregan intereses para cada clase

alumnosInscritos = 0
while alumnosInscritos < alumnosTotales: # Mientras no se hayan inscrito todos los alumnos a una clase
    alumnosInscritos = 0
    for a in range(alumnosTotales):
        for c in range(clasesTotales):
            if random() < clasesInteres[c] and (a, c) not in alumnosClases: # Si un alumno se logra interesar en una clase; y no está inscrito en esa clase
                alumnosClases.append((a, c)) # se inscribe

    for a in range(alumnosTotales):
        if a in (i[0] for i in alumnosClases): # Si a alumno ha inscrito al menos una clase; https://mail.python.org/pipermail/tutor/2005-June/039149.html
            alumnosInscritos = alumnosInscritos + 1 # Se suma al total de alumnos inscritos

for a in range(len(alumnosClases)): # Por cada alumno interesado en una clase
    alumno = alumnosClases[a][0]
    clase = alumnosClases[a][1]
    print("set arrow " + str(a + 1) +
        " from " + str(alumnosPos[alumno][0]) + "," + str(alumnosPos[alumno][1]) +
        " to " + str(clasesPos[clase][0]) + "," + str(clasesPos[clase][1])
        + " nohead") # se dibuja un arco entre dicho alumno y dicha clase

clasesAsignadas = 0
while clasesAsignadas < clasesTotales: # Mientras no estén asignados todas las clases
    clasesAsignadas = 0
    for c in range(clasesTotales):
        for h in range(horariosTotales):
            if random() < horarioProb and c not in (i[0] for i in clasesHorarios): # si se pasa la probabilidad de que se asigne un horario en una clase Y la clase no tenga asignado un horiario
                clasesHorarios.append((c, h)) # Se inscribe la clase

    for c in range(clasesTotales):
        if c in (i[0] for i in clasesHorarios):
            clasesAsignadas = clasesAsignadas + 1

t = len(alumnosClases) + 1
for c in range(len(clasesHorarios)):
    clase = clasesHorarios[c][0]
    horario = clasesHorarios[c][1]
    size = [fila[1] for fila in alumnosClases].count(clase) * 2
    size = size / len(alumnosClases) * 1.0 + 0.1
    print("set arrow " + str(t + c) +
    " from " + str(clasesPos[clase][0]) + "," + str(clasesPos[clase][1]) +
    " to " + str(horariosPos[horario][0]) + "," + str(horariosPos[horario][1]) + " nohead")
    print("set object circle at " + str(clasesPos[clase][0]) + "," + str(clasesPos[clase][1]) + " fillcolor palette frac " + str(0.1 + horario / horariosTotales * 1.0) + " fillstyle solid noborder size " + str(size))
print("show arrow")

for a in range(alumnosTotales):
    print("set object circle at " + str(alumnosPos[a][0]) + "," + str(alumnosPos[a][1]) + " fillcolor rgb 'black' fillstyle solid noborder size 0.3")

for h in range(horariosTotales):
    size = [fila[1] for fila in clasesHorarios].count(h)# Contar elementos por columna https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
    size = size / len(clasesHorarios) * 1.0 + 0.1
    print("set object circle at " + str(horariosPos[h][0]) + "," + str(horariosPos[h][1]) + " fillcolor palette frac " + str(0.1 + h / horariosTotales * 1.0) + " fillstyle solid noborder size " + str(size) ) # http://gnuplot.sourceforge.net/docs_4.2/node62.html

print("plot [-{}:{}][-{}:{}] NaN t''".format(rAlumnos + 1, rAlumnos + 1, rAlumnos + 1, rAlumnos + 1)) # http://gnuplot-surprising.blogspot.mx/2011/11/how-to-plot-nothing-using-gnuplot.html
