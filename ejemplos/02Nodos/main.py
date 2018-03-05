import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, randint

N = 20 # Nodos totales

G = Grafo()

n = Nodo()
n.id = ""
n.posicion = (0, 0)
n.radio = 0.2
n.Color(255, 0, 0, 0)
G.AgregarNodo(n)

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

G.DibujarGrafo("Ejemplo 2. Nodos", True)
