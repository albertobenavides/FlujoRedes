from random import random, randint, sample
from math import sin, cos, sqrt
from os import system

alumnosTotales = 50
materiasTotales = 10
horariosTotales = 5
horarioProb = 0.2
distanciaTotal = 0.0

def Distancia (x1, y1, x2, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

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
with open("horario.gnu", "w") as f:
    print("set terminal png", file = f)
    print("set output 'img/h000000.png'", file = f)
    print("set key off", file = f)
    print("set size square", file = f)
    print("unset colorbox", file = f)

    for c in range(materiasTotales):
        materiasInteres.append(random()) # Se agregan intereses para cada materia

    alumnosInscritos = 0
    while alumnosInscritos < alumnosTotales: # Mientras no se hayan inscrito todos los alumnos a una materia
        alumnosInscritos = 0
        for a in range(alumnosTotales):
            for c in range(materiasTotales):
                if random() < materiasInteres[c] and (a, c) not in alumnosMaterias: # Si un alumno se logra interesar en una materia; y no está inscrito en esa materia
                    alumnosMaterias.append((a, c)) # se inscribe

        for a in range(alumnosTotales):
            if a in (i[0] for i in alumnosMaterias): # Si a alumno ha inscrito al menos una materia; https://mail.python.org/pipermail/tutor/2005-June/039149.html
                alumnosInscritos = alumnosInscritos + 1 # Se suma al total de alumnos inscritos

    materiasAsignadas = 0
    while materiasAsignadas < materiasTotales: # Mientras no estén asignados todas las materias
        materiasAsignadas = 0
        for c in range(materiasTotales):
            for h in range(horariosTotales):
                if random() < horarioProb and c not in (i[0] for i in materiasHorarios): # si se pasa la probabilidad de que se asigne un horario en una materia Y la materia no tenga asignado un horiario
                    materiasHorarios.append((c, h)) # Se inscribe la materia

        for c in range(materiasTotales):
            if c in (i[0] for i in materiasHorarios):
                materiasAsignadas = materiasAsignadas + 1

    for a in range(alumnosTotales):
        print("set object circle at " + str(alumnosPos[a][0]) + "," + str(alumnosPos[a][1]) + " fillcolor rgb 'black' fillstyle solid noborder size 0.3", file = f) # Se dibujan los alumnos

    for a in range(len(alumnosMaterias)): # Por cada alumno interesado en una materia
        alumno = alumnosMaterias[a][0]
        materia = alumnosMaterias[a][1]
        x1 = alumnosPos[alumno][0] # alumnoPos x
        y1 = alumnosPos[alumno][1] # alumnoPos y
        x2 = materiasPos[materia][0] # materiaPos y
        y2 = materiasPos[materia][1] # materiaPos y
        distanciaTotal = distanciaTotal + Distancia(x1, y1, x2, y2)
        print("set arrow " + str(a + 1) +
            " from " + str(x1) + "," + str(y1) +
            " to " + str(x2) + "," + str(y2)
            + " nohead", file = f) # se dibuja un arco entre dicho alumno y dicha materia

    t = len(alumnosMaterias) + 1
    for c in range(len(materiasHorarios)):
        materia = materiasHorarios[c][0]
        horario = materiasHorarios[c][1]
        size = [fila[1] for fila in alumnosMaterias].count(materia) * 2 # por cada materia que haya sido elegida por un alumno, se tiene un tamaño de materia; mientras más alumnos, más grande
        size = size / len(alumnosMaterias) + 0.2
        size = size * rAlumnos / 5
        x1 = materiasPos[materia][0] # materiaPos x
        y1 = materiasPos[materia][1] # materiaPos y
        x2 = horariosPos[horario][0] # horarioPos x
        y2 = horariosPos[horario][0] # horarioPos y
        distanciaTotal = distanciaTotal + Distancia(x1, y1, x2, y2)
        print("set object circle at " + str(x1) + "," + str(y1) + " fillcolor palette frac " + str(horario / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size), file = f)
        print("set arrow " + str(t + c) +
        " from " + str(x1) + "," + str(y1) +
        " to " + str(x2) + "," + str(y2) + " nohead", file = f)
    print("show arrow", file = f)

    for h in range(horariosTotales):
        size = [fila[1] for fila in materiasHorarios].count(h)# Contar elementos por columna https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
        size = size / len(materiasHorarios) + 0.2
        size = size * rAlumnos / 5
        print("set object circle at " + str(horariosPos[h][0]) + "," + str(horariosPos[h][1]) + " fillcolor palette frac " + str(h / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size), file = f) # http://gnuplot.sourceforge.net/docs_4.2/node62.html

    print("set title 'Paso 0 - Distancia " + str(distanciaTotal) + "'", file = f)
    print("plot [-{}:{}][-{}:{}] NaN t''".format(rAlumnos + 1, rAlumnos + 1, rAlumnos + 1, rAlumnos + 1), file = f) # http://gnuplot-surprising.blogspot.mx/2011/11/how-to-plot-nothing-using-gnuplot.html
    print("quit", file = f)

system("gnuplot horario.gnu") # Generación de imagen por gnuplot


# MUTACIÓN
generacion = 100000
indiceImagen = 1
alumnosPosTemp = list(alumnosPos) # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
materiasPosTemp = list(materiasPos)
horariosPosTemp = list(horariosPos)
for g in range(generacion):
    distanciaTemp = 0.0
    for a in range(alumnosTotales): #se intercambia un 10% de los alumnos
        r = randint(0, alumnosTotales - 1)
        tPos = alumnosPosTemp[a]
        alumnosPosTemp[a] = alumnosPosTemp[r]
        alumnosPosTemp[r] = tPos

    for m in range(materiasTotales): #se intercambia un 10% de las materias
        r = randint(0, materiasTotales - 1)
        tPos = materiasPosTemp[m]
        materiasPosTemp[m] = materiasPosTemp[r]
        materiasPosTemp[r] = tPos

    for h in range(horariosTotales): #se intercambia un 10% de las horarios
        r = randint(0, horariosTotales - 1)
        tPos = horariosPosTemp[h]
        horariosPosTemp[h] = horariosPosTemp[r]
        horariosPosTemp[r] = tPos

    for a in range(len(alumnosMaterias)): # Por cada alumno interesado en una materia
        alumno = alumnosMaterias[a][0]
        materia = alumnosMaterias[a][1]
        x1 = alumnosPosTemp[alumno][0] # alumnoPos x
        y1 = alumnosPosTemp[alumno][1] # alumnoPos y
        x2 = materiasPosTemp[materia][0] # materiaPos y
        y2 = materiasPosTemp[materia][1] # materiaPos y
        distanciaTemp = distanciaTemp + Distancia(x1, y1, x2, y2)

    for c in range(len(materiasHorarios)):
        materia = materiasHorarios[c][0]
        horario = materiasHorarios[c][1]
        x1 = materiasPosTemp[materia][0] # materiaPos x
        y1 = materiasPosTemp[materia][1] # materiaPos y
        x2 = horariosPosTemp[horario][0] # horarioPos x
        y2 = horariosPosTemp[horario][0] # horarioPos y
        distanciaTemp = distanciaTemp + Distancia(x1, y1, x2, y2)

    if distanciaTemp < distanciaTotal:
        distanciaTotal = distanciaTemp
        alumnosPos = list(alumnosPosTemp)
        materiasPos = list(materiasPosTemp)
        horariosPos = list(horariosPosTemp)
        with open("horario.gnu", "w") as f:
            print("set terminal png", file = f)
            print("set title 'Paso " + str(indiceImagen) + " - Distancia " + str(distanciaTotal) + "'", file = f)
            print("set output 'img/h" + str(g + 1).zfill(6) + ".png'", file = f)
            print("set key off", file = f)
            print("set size square", file = f)
            print("unset colorbox", file = f)

            for a in range(alumnosTotales):
                print("set object circle at " + str(alumnosPos[a][0]) + "," + str(alumnosPos[a][1]) + " fillcolor rgb 'black' fillstyle solid noborder size 0.3", file = f)

            for a in range(len(alumnosMaterias)):
                alumno = alumnosMaterias[a][0]
                materia = alumnosMaterias[a][1]
                x1 = alumnosPos[alumno][0] # alumnoPos x
                y1 = alumnosPos[alumno][1] # alumnoPos y
                x2 = materiasPos[materia][0] # materiaPos y
                y2 = materiasPos[materia][1] # materiaPos y
                print("set arrow " + str(a + 1) +
                    " from " + str(x1) + "," + str(y1) +
                    " to " + str(x2) + "," + str(y2)
                    + " nohead", file = f) # se dibuja un arco entre dicho alumno y dicha materia

            t = len(alumnosMaterias) + 1
            for c in range(len(materiasHorarios)):
                materia = materiasHorarios[c][0]
                horario = materiasHorarios[c][1]
                size = [fila[1] for fila in alumnosMaterias].count(materia) * 2
                size = size / len(alumnosMaterias) + 0.2
                size = size * rAlumnos / 5
                x1 = materiasPos[materia][0] # materiaPos x
                y1 = materiasPos[materia][1] # materiaPos y
                x2 = horariosPos[horario][0] # horarioPos x
                y2 = horariosPos[horario][0] # horarioPos y
                print("set arrow " + str(t + c) +
                " from " + str(x1) + "," + str(y1) +
                " to " + str(x2) + "," + str(y2) + " nohead", file = f)
                print("set object circle at " + str(x1) + "," + str(y1) + " fillcolor palette frac " + str(horario / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size), file = f)
            print("show arrow", file = f)

            for h in range(horariosTotales):
                size = [fila[1] for fila in materiasHorarios].count(h)
                size = size / len(materiasHorarios) + 0.2
                size = size * rAlumnos / 5
                print("set object circle at " + str(horariosPos[h][0]) + "," + str(horariosPos[h][1]) + " fillcolor palette frac " + str(h / horariosTotales * 0.8 + 0.2) + " fillstyle solid noborder size " + str(size), file = f)

            print("plot [-{}:{}][-{}:{}] NaN t''".format(rAlumnos + 1, rAlumnos + 1, rAlumnos + 1, rAlumnos + 1), file = f)
            print("quit", file = f)

        indiceImagen = indiceImagen + 1
        system("gnuplot horario.gnu")

system("magick -delay 50 img/h*.png horarios.gif") # Creación de gif a partir de las imágenes generadas en cada paso de la iteración
