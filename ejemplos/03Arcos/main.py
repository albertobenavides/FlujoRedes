import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random, randint, sample
from math import cos, sin

N = 20
r = 0.5 # Radio de la circunferencia
P = 2 * 3.14 * r # Perímetro de la circunferencia
rNodo = P / N / 3 # Radio para cada nodo
theta = 2 * 3.14 / N # Fracción angular que ocupará cada nodo

pVecino = 0.3 # Probabilidad de hacer una vecindad

G = Grafo()
G.dirigido = True

for i in range(N):
    n = Nodo()
    n.id = i
    n.radio = rNodo
    n.Color(
        randint(0, 255), # rojo (R)
        randint(0, 255), # verde (G)
        randint(0, 255),  # azul (B)
        0, # alfa (A); transparencia
    )
    n.posicion = (
        0.5 + r * cos(theta * i), 0.5 + r * sin(theta * i)
    )
    G.AgregarNodo(n)

for n in G.nodos:
    for i in range(3):
        if random() < pVecino:
            candidatos = set(G.nodos) - set([n]) # https://stackoverflow.com/questions/41643862/create-random-number-excluding-numbers-in-a-list
            v = sample(candidatos, 1) # Devueve un arreglo
            G.ConectarNodos(n, v[0], random() * 2)

G.DibujarGrafo("Ejemplo 3. Arcos")
