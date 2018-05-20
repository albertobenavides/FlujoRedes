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
k = 10
k = k ** 2
G = Grafo()
G.dirigido = False
for i in range(k):
    n = Nodo()
    n.id = ""
    G.AgregarNodo(n)
G.Cuadrado(G.nodos)

r = sample(range(k), 2) # Elegir dos índices al azar entre los nodos
inicio = G.nodos[r[0]]
inicio.Color(0, 0, 255)
inicio.radio *= 2
fin = G.nodos[r[1]]
fin.Color(255, 255, 0)
fin.radio *= 2

lado = floor(sqrt(k))
for i in range(k-1):
    if i % lado != lado - 1:
        G.ConectarNodos(G.nodos[i], G.nodos[i + 1])#, peso = 1 + random() * 4)
    if int(i / lado) < lado and i < lado ** 2 - lado:
        G.ConectarNodos(G.nodos[i], G.nodos[i + lado])#, peso = 1 + random() * 4)
G.DibujarGrafo()

tiempo = clock()
print(G.Ford_Fulkerson(inicio, fin))
tiempo = clock() - tiempo
print(tiempo)

#GTemp = deepcopy(G)

t = 0
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
                    G.pesos[(v1, n)] += G.pesos[v1, v]
                else:
                    G.ConectarNodos(n, v1)#, peso = G.pesos[(v, v1)])
        G.EliminarNodo(v)
        if debug:
            G.nombre = "img/t{0:03d}".format(t)
            G.DibujarGrafo(titulo = "t = {}".format(t))
            t = t + 1
    if debug:
        n.color = color
tiempo = clock() - tiempo
print(G.pesos[(inicio, fin)])
print(tiempo)

if debug:
    system("magick -delay 20 img/t*.png ejemplo.gif")
