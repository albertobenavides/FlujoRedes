from random import random, randint, sample
from math import ceil
from time import clock #https://stackoverflow.com/questions/1465146/how-do-you-determine-a-processing-time-in-python
import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo

for paso in range(0, 10):
    for p in range (8, 9):
        pot2 = 2 ** p
        G = Grafo()
        G.dirigido = True
        G.nombre = str(pot2)
        for i in range(0, pot2): # Se crean tantos nodos como la potencia de 2 correspondiente
            n = Nodo()
            n.id = ""
            n.posicion = (random(), random())
            n.radio = 0.01
            n.Color(
                randint(0, 255), # rojo (R)
                randint(0, 255), # verde (G)
                randint(0, 255)  # azul (B)
            )
            G.AgregarNodo(n)
        conexionesMax = pot2 * (pot2 - 1) # Puede haber tantas conexiones como nodos por el resto de nodos. Si ya 10 nodos, cada nodo se podría conectar con 9 más.
        porcentaje = ceil(conexionesMax * 0.1) # Porcentaje de arcos que se harán
        for i in range(0, porcentaje): # Se crean tantos arcos como el 10% de las conexiones totales posibles
            n = sample(G.nodos, 1)[0] # Como sample regresa una lista, se elige el primer elemento nomás, que es el nodo elegido al azar
            candidatos = set(G.nodos) - set([n]) - set(G.vecinos[n])
            v = sample(candidatos, 1)[0] # Lo mismo aquí, se elige el primer elemento de la lista
            G.ConectarNodos(n, v, random() * 2)
        #if(p < 4):
        #    G.DibujarGrafo()
        with open("tiempos.txt", "a") as f:
            tiempoFloyd = clock()
            G.Floyd_Warshall()
            tiempoFloyd = clock() - tiempoFloyd

            n = sample(G.nodos, 1)[0]
            candidatos = set(G.nodos) - set([n])
            v = sample(candidatos, 1)[0]
            tiempoFord = clock()
            G.Ford_Fulkerson(n, v)
            tiempoFord = clock() - tiempoFord
            f.write('{}, {}, {} \n'.format(p, tiempoFloyd, tiempoFord)) # https://pyformat.info/
