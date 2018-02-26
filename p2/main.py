from Grafo import Grafo
from Nodo import Nodo
from random import random, randint
from time import time

nodosTotales = 4

G = Grafo()
for i in range(nodosTotales):
    n = Nodo()
    n.id = i
    n.posicion = (random(), random())
    G.AgregarNodo(n)

randint(0, nodosTotales - 1)

listaNodos = list(G.nodos)
arcosTotales = 0
for i in range(nodosTotales - 1):
    arcos =  randint(1, 1) # arcos desde nodo i
    for a in range(arcos):
        arcosTotales = arcosTotales + 1
        siguiente = i + 1
        rVecino = randint(siguiente, nodosTotales - 1)
        G.ConectarNodos(listaNodos[i], listaNodos[rVecino])
        print("i = " + str(i) + "; nodo = " + str(listaNodos[i].id) )

#Estados
#no visitado    0
#visitado       1
#terminado      2

for n in G.nodos:
    n.estado = 0
    n.mama = None
t = 0

def Tiempo(tiempo):
  global t
  #print("tLocal = " +str(tiempo) + "tGlobal = " + str(t))
  t = t + tiempo
  return t

def Visitar(vecinos, n, tiempo):
    n.estado = 1 # visitado
    global t
    t = t + tiempo
    #Tiempo(tiempo + 1)
    for v in vecinos:
        if v.estado == 0: # si no está visitado o terminado
            v.mama = n
            Visitar(G.vecinos[v], v, tiempo)
        n.estado = 2 # terminado
        #Tiempo(tiempo + 1)
        t = t + tiempo

tInicial = time()
for n in G.nodos:
    if n.estado is 0: # no visitado
        Visitar(G.vecinos[n], n, t)

tFinal = time() - tInicial
print("tiempo transcurrido = %.10f" % tFinal)
print("nodos = " + str(nodosTotales) + " ; arcos = " + str(arcos) + " ; tiempo total = " + str(t))

#grafo.DibujarGrafo("hola")
