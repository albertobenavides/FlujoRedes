from random import random

alumnosTotales = 20
clasesTotales = 8
horariosTotales = 6
horarioProb = 0.2

clasesInteres = list()
alumnosClases = list()
clasesHorarios = list()

print("set terminal png")
print("set output 'horarios.png'")
print("set key off")
print("unset colorbox")

for c in range(clasesTotales):
    clasesInteres.append(random()) # Lo interesante que es una clase

alumnosInscritos = 0
while alumnosInscritos < alumnosTotales:
    alumnosInscritos = 0
    for a in range(alumnosTotales):
        for c in range(clasesTotales):
            if random() < clasesInteres[c] and (a, c) not in alumnosClases: # Si un alumno se logra interesar en una clase; y no está inscrito en esa clase
                alumnosClases.append((a, c)) # se inscribe

    for a in range(alumnosTotales):
        if a in (i[0] for i in alumnosClases): # Si a alumno ha inscrito al menos una clase; https://mail.python.org/pipermail/tutor/2005-June/039149.html
            alumnosInscritos = alumnosInscritos + 1 # Se suma al total de alumnos inscritos

for a in range(len(alumnosClases)):
    print("set arrow " + str(a + 1) + " from " + str(alumnosClases[a][0]) + ",0 to " + str(alumnosClases[a][1]) + ",2 nohead")

clasesAsignadas = 0
while clasesAsignadas < clasesTotales:
    clasesAsignadas = 0
    for c in range(clasesTotales):
        for h in range(horariosTotales):
            if random() < horarioProb and c not in (i[0] for i in clasesHorarios):
                clasesHorarios.append((c, h))

    for c in range(clasesTotales):
        if c in (i[0] for i in clasesHorarios):
            clasesAsignadas = clasesAsignadas + 1

t = len(alumnosClases) + 1
for c in range(len(clasesHorarios)):
    clase = clasesHorarios[c][0]
    horario = clasesHorarios[c][1]
    size = [fila[1] for fila in alumnosClases].count(clase)
    size = size / len(alumnosClases) * 1.0 + 0.1
    print("set arrow " + str(t + c) + " from " + str(clase) + ",2 to " + str(horario) + ",4 nohead")
    print("set object circle at " + str(clase) + ",2 fillcolor palette frac " + str(0.1 + horario / horariosTotales * 1.0) + " fillstyle solid noborder size " + str(size))
print("show arrow")

for a in range(alumnosTotales):
    print("set object circle at " + str(a) + ",0 fillcolor rgb 'black' fillstyle solid noborder size 0.3")

for h in range(horariosTotales):
    size = [fila[1] for fila in clasesHorarios].count(h)# Contar elementos por columna https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
    size = size / len(clasesHorarios) * 1.0 + 0.1
    print("set object circle at " + str(h) + ",4 fillcolor palette frac " + str(0.1 + h / horariosTotales * 1.0) + " fillstyle solid noborder size " + str(size) ) # http://gnuplot.sourceforge.net/docs_4.2/node62.html

print("plot [-1:" + str(alumnosTotales) + "][-1:5] NaN t''") # http://gnuplot-surprising.blogspot.mx/2011/11/how-to-plot-nothing-using-gnuplot.html
