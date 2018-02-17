from random import random
from math import sin, cos

alumnosTotales = 20
materiasTotales = 10
horariosTotales = 5
horarioProb = 0.2

rAlumnos = alumnosTotales / (2 * 3.14) * 3 # Radio para alumnos
aAlumnos = 2 * 3.14 / alumnosTotales

alumnosPos = list()
for a in range(alumnosTotales):
    alumnosPos.append(
        (rAlumnos * cos(aAlumnos * a), rAlumnos * sin(aAlumnos * a))
    )

rMaterias = alumnosTotales / (2 * 3.14) * 2 # Radio para materias (a partir del diámetro de alumnos)
aMaterias = 2 * 3.14 / materiasTotales

materiasPos = list()
for c in range(materiasTotales):
    materiasPos.append(
        (rMaterias * cos(aMaterias * c), rMaterias * sin(aMaterias * c))
    )

rHorarios = alumnosTotales / (2 * 3.14) / 1.5 # Radio para materias (a partir del diámetro de alumnos)
aHorarios = 2 * 3.14 / horariosTotales

horariosPos = list()
for h in range(horariosTotales):
    horariosPos.append(
        (rHorarios * cos(aHorarios * h), rHorarios * sin(aHorarios * h))
    )

materiasInteres = list()
alumnosMaterias = list()
materiasHorarios = list()

print("set terminal png")
print("set output 'img/horarios.png'")
print("set key off")
print("set size square")
print("unset colorbox")

for c in range(materiasTotales):
    materiasInteres.append(random()) # Se agregan intereses para cada clase

alumnosInscritos = 0
while alumnosInscritos < alumnosTotales: # Mientras no se hayan inscrito todos los alumnos a una clase
    alumnosInscritos = 0
    for a in range(alumnosTotales):
        for c in range(materiasTotales):
            if random() < materiasInteres[c] and (a, c) not in alumnosMaterias: # Si un alumno se logra interesar en una clase; y no está inscrito en esa clase
                alumnosMaterias.append((a, c)) # se inscribe

    for a in range(alumnosTotales):
        if a in (i[0] for i in alumnosMaterias): # Si a alumno ha inscrito al menos una clase; https://mail.python.org/pipermail/tutor/2005-June/039149.html
            alumnosInscritos = alumnosInscritos + 1 # Se suma al total de alumnos inscritos

for a in range(len(alumnosMaterias)): # Por cada alumno interesado en una clase
    alumno = alumnosMaterias[a][0]
    clase = alumnosMaterias[a][1]
    print("set arrow " + str(a + 1) +
        " from " + str(alumnosPos[alumno][0]) + "," + str(alumnosPos[alumno][1]) +
        " to " + str(materiasPos[clase][0]) + "," + str(materiasPos[clase][1])
        + " nohead") # se dibuja un arco entre dicho alumno y dicha clase

materiasAsignadas = 0
while materiasAsignadas < materiasTotales: # Mientras no estén asignados todas las materias
    materiasAsignadas = 0
    for c in range(materiasTotales):
        for h in range(horariosTotales):
            if random() < horarioProb and c not in (i[0] for i in materiasHorarios): # si se pasa la probabilidad de que se asigne un horario en una clase Y la clase no tenga asignado un horiario
                materiasHorarios.append((c, h)) # Se inscribe la clase

    for c in range(materiasTotales):
        if c in (i[0] for i in materiasHorarios):
            materiasAsignadas = materiasAsignadas + 1

t = len(alumnosMaterias) + 1
for c in range(len(materiasHorarios)):
    clase = materiasHorarios[c][0]
    horario = materiasHorarios[c][1]
    size = [fila[1] for fila in alumnosMaterias].count(clase) * 2 # por cada clase que haya sido elegida por un alumno, se tiene un tamaño de clase; mientras más alumnos, más grande
    size = size / len(alumnosMaterias) + 0.2
    size = size * rAlumnos / 5
    print("set arrow " + str(t + c) +
    " from " + str(materiasPos[clase][0]) + "," + str(materiasPos[clase][1]) +
    " to " + str(horariosPos[horario][0]) + "," + str(horariosPos[horario][1]) + " nohead")
    print("set object circle at " + str(materiasPos[clase][0]) + "," + str(materiasPos[clase][1]) + " fillcolor palette frac " + str(horario / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size))
print("show arrow")

for a in range(alumnosTotales):
    print("set object circle at " + str(alumnosPos[a][0]) + "," + str(alumnosPos[a][1]) + " fillcolor rgb 'black' fillstyle solid noborder size 0.3")

for h in range(horariosTotales):
    size = [fila[1] for fila in materiasHorarios].count(h)# Contar elementos por columna https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
    size = size / len(materiasHorarios) + 0.2
    size = size * rAlumnos / 5
    print("set object circle at " + str(horariosPos[h][0]) + "," + str(horariosPos[h][1]) + " fillcolor palette frac " + str(h / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size) ) # http://gnuplot.sourceforge.net/docs_4.2/node62.html

print("plot [-{}:{}][-{}:{}] NaN t''".format(rAlumnos + 1, rAlumnos + 1, rAlumnos + 1, rAlumnos + 1)) # http://gnuplot-surprising.blogspot.mx/2011/11/how-to-plot-nothing-using-gnuplot.html
