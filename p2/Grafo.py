# Grafo dirigido
# Grafo ponderado
# Formas de nodos
# Separar
# EPS

from math import sqrt
from os import system
class Grafo:

    def __init__(self, nombre = "Grafo"):
        self.nodos = set() # un conjunto
        self.pesos = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
        self.nombre = nombre

    def AgregarNodo(self, n):
        self.nodos.add(n)
        if not n in self.vecinos: # vecindad de v
            self.vecinos[n] = set()

    def ConectarNodos(self, n1, n2, peso = 1):
        self.AgregarNodo(n1)
        self.AgregarNodo(n2)
        self.pesos[(n1, n2)] = peso
        self.vecinos[n1].add(n2)

    def DistanciaTotal(self):
        d = 0.0
        for n in self.vecinos:
            for v in self.vecinos[n]:
                d = d + sqrt((n.posicion[0] - v.posicion[0]) ** 2 + (n.posicion[1] - v.posicion[1]) ** 2)
        return d

    def DibujarGrafo(self, titulo = ""):
        with open(self.nombre + ".gnu", "w") as f:
            print("set terminal png", file = f)
            print("set output '" + self.nombre + ".png'", file = f)
            print("set key off", file = f)
            print("set size square", file = f)
            print("unset colorbox", file = f)
            print("set title'" + titulo + "'", file = f)

            for n in self.nodos:
                print("set object circle at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " fillcolor palette frac '" + str(n.color) + "' fillstyle solid noborder size " + str(n.radio), file = f)

            #minX = self.nodos.posicion
            #minY

            print("plot [-0.5:1.5][-0.5:1.5] NaN t''", file = f)
            print("quit", file = f)

        system("gnuplot " + self.nombre +".gnu")
