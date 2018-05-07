import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, sample
from math import sqrt, floor
from os import system, remove
from copy import deepcopy
from time import clock

debug = False
veces = 20

for k in range(3, 11): # Hasta k = 10 nodos por lado
    k = k ** 2
    lado = floor(sqrt(k))
    for l in range(1, int(sqrt(k)) + 1): #Distancia Manhattan de conexiones entre vecinos; conexiones simétricas;
        if l > 3: # RECOMENDADO: Hacer entre l = [1, 3] con valores enteros
            break

        with open('results/k{0:03d}l{1:03d}.csv'.format(k, l), 'a') as f:
            f.write('a p ford tiempo\n')

        for p in range(0, 120, 20):
            p = p / 1000
            G = Grafo()

            for i in range(k):
                n = Nodo()
                n.id = ""
                if i == 0:
                    n.Color(255, 0, 0) # inicio
                elif i == k-1:
                    n.Color(0, 0, 255) # fin

                G.AgregarNodo(n)

            G.Cuadrado(G.nodos)


            # Se conectan todos en l 1 hasta Manhattan
            for i in range(k - 1):
                if i % lado != lado - 1:
                    G.ConectarNodos(G.nodos[i], G.nodos[i + 1])

                if int(i / lado) < lado and i < lado ** 2 - lado:
                    G.ConectarNodos(G.nodos[i], G.nodos[i + lado])

        # Se conectan tantos vecinos a distancia Manhattan desde cada nodo como l especifique
            if l > 1:
                a = [] # Nuevas vecindades
                for n in G.nodos:
                    for v in G.vecinos[n]:
                        a = G.PasoManhattan(n, v, l - 1, a)
                for par in a:
                    G.ConectarNodos(par[0], par[1])

            G.dirigido = True
            for n in G.nodos: # se agregan saltos cuánticos dada una probabilidad p
                if random() < p: # Hacer esto una función que conecte un nodo con alguno disponible
                    candidatos = set(G.nodos) - set([n]) - set(G.vecinos[n])
                    if len(candidatos) > 0:
                        v = sample(candidatos, 1)[0]
                        G.ConectarNodos(n, v, c = (255, 0, 0))

            if debug:
                G.nombre = "img/k{2:03d}l{0:03d}p{1:03d}".format(l, int(p * 1000), k)
                G.DibujarGrafo("k = {2}; l = {0}; p = {1}".format(l, p, int(sqrt(k))))
                remove("img/k{2:03d}l{0:03d}p{1:03d}.gnu".format(l, int(p * 1000), k))

            GTemp = deepcopy(G) # Copia del grafo para poder utilizarlo después de borrarle - https://docs.python.org/3/library/copy.html#copy.deepcopy

            with open('results/k{0:03d}l{1:03d}.csv'.format(k, l), 'a') as f:
                for vez in range(veces):
                    G = deepcopy(GTemp)
                    llega = True
                    a = 0 # Cantidad de arcos eliminados
                    while llega:
                        tiempo = clock()
                        ford = G.Ford_Fulkerson(G.nodos[0], G.nodos[k - 1])
                        tiempo = clock() - tiempo
                        f.write('{0} {1} {2} {3}\n'.format(a, p, ford, tiempo))
                        if ford == 0:
                            llega = False

                        n = sample(set(G.nodos), 1)[0]
                        candidatos = set(G.vecinos[n])
                        if len(candidatos) > 0:
                            v = sample(set(G.vecinos[n]), 1)[0]
                            if v:
                                del(G.pesos[(n, v)])
                                G.vecinos[n].remove(v)
                                if n in G.vecinos[v]:
                                    del(G.pesos[(v, n)])
                                    G.vecinos[v].remove(n)
                                a = a + 1
        with open('plot.gnu', 'w') as f:
            f.write("set terminal png truecolor\n")
            f.write("set output 'img/k{0:03d}l{1:03d}.png'\n".format(k, l)
            f.write("set key off\n")

            f.write("set title 'k = {}; l = {}'\n".format(k, l))
            f.write("set xlabel 'Probabilidad'\n")
            f.write("set ylabel 'Ford-Fulkerson'\n")
            f.write("set style fill solid 0.25 border -1\n")
            f.write("set style boxplot outliers pointtype 7\n")
            f.write("set style data boxplot\n")
            f.write("plot 'results/k{0:03d}l{1:03d}.csv' using 1:3:(0.5):2".format(k, l)

        system("gnuplot plot.gnu")
        remove('plot.gnu')
system("magick -delay 15 img/k*.png ejemplo.gif")

if debug:
    system("magick -delay 15 img/k*.png ejemplo.gif")
