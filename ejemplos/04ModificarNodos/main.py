import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, sample
from math import sqrt, floor

N = 20

lado = floor(sqrt(20))

G = Grafo()
G.dirigido = True
G.nombre = "dirigido"

for i in range(N):
    n = Nodo()
    n.id = i
    n.radio = 0.08
    n.posicion = ((i % lado) / lado, int(i / lado) / lado)
    G.AgregarNodo(n)

for i in range(N - 1):
    if i % lado != lado - 1:
        G.ConectarNodos(G.nodos[i], G.nodos[i + 1])

    if int(i / lado) < lado:
        G.ConectarNodos(G.nodos[i], G.nodos[i + lado])

n = G.NodoConId(3)
n.Color(255, 0, 0)
n.posicion= (1, 0)

n = G.NodoConId(5)
n.Color(0, 255, 0)
G.EliminarVecindades(n)

n = G.NodoConId(14)
G.EliminarNodo(n)

n = G.NodoConId(4)
G.ModificarPesos(n, 3)

G.DibujarGrafo("Ejemplo 4.1 Manipulación de nodos en grafo dirigido")

G.dirigido = False
G.nombre = "noDirigido"

n = G.NodoConId(11)
G.ModificarPesos(n, 5)

G.DibujarGrafo("Ejemplo 4.2 Manipulación de nodos en grafo no dirigido", True)

G.DibujarGrafo("Ejemplo 4.2 Manipulación de nodos en grafo no dirigido")
