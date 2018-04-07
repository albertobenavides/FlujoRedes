from Grafo import Grafo
from Nodo import Nodo
from random import random, randint, sample
from time import time

nodosTotales = 10

G = Grafo()
G.dirigido = True

for i in range(nodosTotales):
    n = Nodo()
    n.id = i
    n.radio = 0.05
    n.posicion = (random(), random())
    n.Color(
        randint(0, 255), # r
        randint(0, 255), # g
        randint(0, 255), # b
        128 # a
    )
    G.AgregarNodo(n)


arcosTotales = 0
for n in G.nodos:
    arcos =  randint(1, 2) # arcos desde nodo i
    vecinos = sample(G.nodos, arcos)
    if n in vecinos:
        vecinos.remove(n)
    for v in vecinos:
        arcosTotales = arcosTotales + 1
        G.ConectarNodos(n, v, random() * 2)

#Estados
#no visitado    0
#visitado       1
#terminado      2

for n in G.nodos:
    n.estado = 0
t = 0

def Tiempo(tiempo):
  global t
  #print("tLocal = " +str(tiempo) + "tGlobal = " + str(t))
  t = t + tiempo
  return t

def Visitar(vecinos, n, tiempo):
    n.estado = 1 # visitado
    Tiempo(tiempo + 1)
    for v in vecinos:
        if v.estado == 0: # si no está visitado o terminado
            Visitar(G.vecinos[v], v, tiempo)
        n.estado = 2 # terminado
        Tiempo(tiempo + 1)

tInicial = time()
for n in G.nodos:
    if n.estado is 0: # no visitado
        Visitar(G.vecinos[n], n, t)

tFinal = time() - tInicial
print("tiempo transcurrido = %.10f" % tFinal)
print("nodos = " + str(nodosTotales) + " ; arcos = " + str(arcos) + " ; tiempo total = " + str(t))

G.DibujarGrafo("Ejemplo")
