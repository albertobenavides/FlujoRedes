import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, sample, randint
from math import sqrt, floor
from os import system, remove

debug = False
k = 25
k = k ** 2
G = Grafo()
G.dirigido = True
for i in range(k):
    n = Nodo()
    n.id = ""
    G.AgregarNodo(n)
G.Cuadrado(G.nodos)

r = sample(range(k), 1)
inicio = G.nodos[r[0]]
inicio.Color(0, 0, 255)
# fin = G.nodos[r[1]]
# fin.Color(255, 255, 0)
if debug:
    G.nombre = "t000"
    G.DibujarGrafo(titulo = "t = 0")

def NoCiclo(inicio, posibles):
    fin = False
    while not fin:
        n = sample(posibles, 1)[0]
        candidatos = set(posibles[n])
        v = sample(candidatos, 1)[0]
        for v1 in G.vecinos[v]:
            G.ConectarNodos(inicio, v1)
            inicio.radio *= 1.1
        G.EliminarNodo(v)

    print("Flujo total = {} \nTiempo total = {}".format(flujoTotal, tiempoTotal))
    if debug:
        system("magick -delay 20 img/t*.png ejemplo.gif")
