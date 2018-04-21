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
with open('results.csv', 'w') as f:
    f.write('p,k,DistanciaPromedio,tDistancia,DensidadPromedio,tDensidad\n')
    for p in range(-10, 0):
        p = 2 ** p # Probabilidad de que se conecten con vecinos con los que aún no se han conectado por k
        for k in range(1, Ka + 1):
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
            if k == 1:
                dMax = dist

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



if debug:
    system("magick -delay 10 0*.png p.gif")
