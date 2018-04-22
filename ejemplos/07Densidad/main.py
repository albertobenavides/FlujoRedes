import sys
sys.path.append('../../fuente/')
from math import floor, pi
from os import system, remove
from time import clock
from random import random, sample

from Grafo import Grafo
from Nodo import Nodo

debug = False
N = 128
Ka = floor(N / 2) # Cantidad de vecinos laterales con los que se conectará cada nodo

veces = 0 # Cantidad de veces que se conectan los vecinos en total; sin repeticiones
dMax = 0
for k in range(1, Ka + 1):
    with open('results/k{0:03d}.csv'.format(k), 'w') as f:
        f.write('p,k,DistanciaPromedio,tDistancia,DensidadPromedio,tDensidad\n')
        G = Grafo()
        for i in range(0, N):
            n = Nodo()
            n.id = ""
            G.AgregarNodo(n)
            if k > i: # Si la k es mayor al número en que se va
                t = i # Se conectará con i anteriores
            else: # Si no,
                t = k # Se conectará con k anteriores; así se evita salir del rango
            for j in range(0, t): # Se conecta con tantos nodos anteriores como k haya
                G.ConectarNodos(G.nodos[i], G.nodos[i - j - 1])
                veces += 1
            if k + i >= N: # Si hace falta conectarse con nodos siguientes, se conecta exactamente con el excedente de nodos faltantes
                for extra in range(0, k + i - N + 1):
                    G.ConectarNodos(G.nodos[i], G.nodos[extra])
                    veces += 1

        if k == 1:
            dMax = G.DistanciaPromedio()
        for p in range(1, 520, 20):
            p = p / 1000
            for nodo in G.nodos:
                if random() < p:
                    candidatos = set(G.nodos) - set([n]) - set(G.vecinos[n])
                    if len(candidatos) > 0:
                        v = sample(candidatos, 1)[0]
                        G.ConectarNodos(n, v)

            #print(veces)
            tDistancia = clock()
            dist = G.DistanciaPromedio()
            tDistancia = clock() - tDistancia

            dist = dist / dMax

            tDensidad = clock()
            densi = G.DensidadPromedio()
            tDensidad = clock() - tDensidad
            f.write("{}, {}, {}, {}, {}, {} \n".format(p, k, dist, tDistancia, densi, tDensidad))
            if debug:
                G.Circular(G.nodos)
                G.nombre = "{:03d}".format(k)
                G.DibujarGrafo()
                remove('{:03d}.gnu'.format(k))
    with open('plot.gnu', 'w') as f:
        print("set terminal png truecolor", file = f)
        print("set output 'img/k{0:03d}.png'".format(k), file = f)
        print("set key off", file = f)

        print("set title 'k = {}'".format(k), file = f)
        print("set xlabel 'Probabilidad'", file = f)
        print("set ylabel 'Distancia promedio normalizada (azul)'", file = f)
        print("set y2label 'Densidad promedio (rojo)'", file = f)
        print("set style line 1 lc rgb '#0000ff' lt 1 lw 1", file = f)
        print("set style line 2 lc rgb '#ff0000' lt 1 lw 1", file = f)

        print("plot[0:0.5][0:1] 'results/k{0:03d}.csv' using 1:3 w lines ls 1, 'results/k{0:03d}.csv' using 1:5 w lines ls 2".format(k, k), file = f)
    system("gnuplot plot.gnu")
remove('plot.gnu')

if debug:
    system("magick -delay 10 0*.png p.gif")
