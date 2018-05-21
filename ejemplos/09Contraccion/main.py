import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, sample, randint
from math import sqrt, floor
from os import system, remove
from copy import deepcopy
from time import clock

debug = False
k = 25
k = k ** 2
G = Grafo()
G.dirigido = False
for i in range(k):
    n = Nodo()
    n.id = ""
    G.AgregarNodo(n)
G.Cuadrado(G.nodos)

lado = floor(sqrt(k))
for i in range(k-1):
    if i % lado != lado - 1:
        G.ConectarNodos(G.nodos[i], G.nodos[i + 1], peso = 0.01 + random())
    if int(i / lado) < lado and i < lado ** 2 - lado:
        G.ConectarNodos(G.nodos[i], G.nodos[i + lado], peso = 0.01 + random())

r = sample(range(k), 2) # Elegir dos índices al azar entre los nodos
inicio = G.nodos[r[0]]
inicio.Color(0, 0, 255)
fin = G.nodos[r[1]]
fin.Color(255, 255, 0)
if debug:
    G.nombre = "img/t000"
    G.DibujarGrafo(titulo = "t = 0")

tiempoFord = clock()
ford = G.Ford_Fulkerson(inicio, fin)
tiempoFord = clock() - tiempoFord
print("Flujo Ford = {} \nTiempo Ford = {}\n".format(ford, tiempoFord))

GTemp = deepcopy(G)

tiempoTotal = 0
flujoTotal = ford * 1000
veces = 0
flujoMax = 0
with open('results/flujo.csv', 'w') as f:
    f.write("veces flujo tiempo\n")
    while flujoTotal > ford * 1.05:#tiempoTotal < tiempoFord:
        t = 1 # paso de la contracción
        G = deepcopy(GTemp)
        inicio = G.nodos[r[0]]
        fin = G.nodos[r[1]]

        tiempo = clock()
        while len(G.nodos) > 2:
            n = sample(G.nodos, 1)[0]
            if debug:
                color = n.color
                n.Color(255, 0, 0)
            candidatos = set(G.vecinos[n])
            if inicio in candidatos:
                candidatos.remove(inicio)
            if fin in candidatos:
                candidatos.remove(fin)
            if len(candidatos) > 0:
                v = sample(candidatos, 1)[0]
                for v1 in G.vecinos[v]:
                    if (n != v1):
                        if v1 in G.vecinos[n]:
                            G.pesos[(n, v1)] += G.pesos[v, v1]
                            G.pesos[(v1, n)] += G.pesos[v, n]
                        else:
                            G.ConectarNodos(n, v1, peso = G.pesos[(v, v1)])
                        n.radio *= 1.1
                G.EliminarNodo(v)
                if debug:
                    G.nombre = "img/t{0:03d}".format(t)
                    G.DibujarGrafo(titulo = "t = {}".format(t))
                    t = t + 1
            if debug:
                n.color = color
        tiempo = clock() - tiempo
        tiempoTotal += tiempo
        debug = False
        if  G.pesos[(inicio, fin)] < flujoTotal:
            veces += 1
            flujoTotal = G.pesos[(inicio, fin)]
            if flujoMax == 0:
                flujoMax = flujoTotal
            f.write("{} {} {}\n".format(veces, flujoTotal, tiempoTotal))

print("Flujo total = {} \nTiempo total = {}".format(flujoTotal, tiempoTotal))
if debug:
    system("magick -delay 20 img/t*.png ejemplo.gif")

xMax = tiempoFord
if xMax < tiempoTotal:
    xMax = tiempoTotal

with open('flujo.gnu', 'w') as f:
    f.write("set terminal png truecolor\n")
    f.write("set output 'flujo.png'\n")
    f.write("set key off\n")
    f.write("unset colorbox\n")
    f.write("set xlabel 'Tiempo (s)'\n")
    f.write("set ylabel 'Flujo máximo'\n")
    f.write("F(x) = {}\n".format(ford))
    f.write("set datafile separator ' '\n")
    f.write("set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5\n")
    f.write("set style line 2 lc rgb '#dd181f' lt 1 lw 2\n")
    f.write("set style line 3 lc rgb '#FFFF00' lt 1 lw 2\n")
    f.write("set arrow 1 from {0},{2} to {0},{1} lc rgb '#006400' lw 2 nohead\n".format(tiempoFord, flujoMax, ford / 2))
    f.write("plot [0:{0}][{1}:{2}] 'results/flujo.csv' using 3:2 title columnhead with linespoints ls 1, ".format(xMax + 1, ford / 2, flujoMax)) # https://stackoverflow.com/questions/13371449/reading-gnuplot-legend-from-csv?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    f.write("F(x) w lines ls 2") # http://www.gnuplotting.org/plotting-data/


system("gnuplot flujo.gnu")
remove('flujo.gnu')
