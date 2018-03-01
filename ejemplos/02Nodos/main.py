import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, randint

N = 20 # Nodos totales

G = Grafo()

for i in range(N):
    n = Nodo()
    n.id = i
    n.posicion = (random(), random())
    n.radio = 0.05 + 0.05 * random()
    n.Color(
        randint(0, 255), # rojo (R)
        randint(0, 255), # verde (G)
        randint(0, 255),  # azul (B)
        128, # alfa (A); transparencia
    )
    G.AgregarNodo(n)

G.DibujarGrafo("Ejemplo 2. Nodos")
