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
k = 10
k = k ** 2
G = Grafo()
G.dirigido = False
for i in range(k):
    n = Nodo()
    n.id = ""
    G.AgregarNodo(n)
G.Cuadrado(G.nodos)

lado = floor(sqrt(100))
for i in range(99):
    if i % lado != lado - 1:
        G.ConectarNodos(G.nodos[i], G.nodos[i + 1])#, peso = 1 + random() * 4)
    if int(i / lado) < lado and i < lado ** 2 - lado:
        G.ConectarNodos(G.nodos[i], G.nodos[i + lado])#, peso = 1 + random() * 4)
G.DibujarGrafo()

GTemp = deepcopy(G)

t = 0
while len(G.nodos) > 2:
    n = sample(set(G.nodos), 1)[0]
    n.Color(255, 0, 0)
    candidatos = set(G.vecinos[n])
    if len(candidatos) > 0:
        v = sample(set(G.vecinos[n]), 1)[0]
        if v:
            for v1 in G.vecinos[v]:
                if (n != v1):
                    G.ConectarNodos(n, v1)#, peso = G.pesos[(v, v1)])
            G.EliminarNodo(v)
    if debug:
        G.nombre = "img/t{0:03d}".format(t)
        G.DibujarGrafo(titulo = "t = {}".format(t))
        t = t + 1

print(G.pesos[(G.nodos[0], G.nodos[1])])

if debug:
    system("magick -delay 15 img/t*.png ejemplo.gif")
