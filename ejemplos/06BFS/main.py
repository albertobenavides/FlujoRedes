import sys
sys.path.append('../../fuente/')
from os import system, remove
from math import floor

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()

niveles = 5
hijos = 2
maxNodosX = hijos ** niveles
radioNodo = 1 / maxNodosX / 3
yDesp = 1 / niveles

nodo = Nodo()
nodo.id = ""
nodo.posicion = (0.5, 1)
nodo.radio = radioNodo
G.AgregarNodo(nodo)

for nivel in range(1, niveles + 1):
    hijosNivel = hijos ** nivel
    xInicial = 1 / (hijosNivel * 2)
    for hijo in range(0, hijosNivel):
        n = Nodo()
        n.id = ""
        n.posicion = (xInicial + 1 / (hijosNivel) * hijo, 1 - yDesp * nivel)
        n.radio = radioNodo
        G.ConectarNodos(G.nodos[hijos ** (nivel - 1) - 1 + floor(hijo / hijos)], n)

#G.DibujarGrafo()

G.BreadthFirst(nodo, 0, True)
system("magick -delay 10 0*.png p.gif")
