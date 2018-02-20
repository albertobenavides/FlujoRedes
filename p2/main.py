from Grafo import Grafo
from Nodo import Nodo
from random import random

nodosTotales = 10

grafo = Grafo()
for i in range(nodosTotales):
    n = Nodo()
    n.posicion = (random(), random())
    grafo.AgregarNodo(n)

grafo.DibujarGrafo("hola")
