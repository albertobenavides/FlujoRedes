# Grafo dirigido
# Grafo ponderado
# Formas de nodos
# Separar
# EPS

from math import sqrt
from os import system
class Grafo:

    def __init__(self, nombre = "grafo"):
        self.nodos = [] # un conjunto
        self.pesos = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
        self.nombre = nombre
        self.dirigido = False

    def AgregarNodo(self, n):
        self.nodos.append(n)
        if not n in self.vecinos: # vecindad de v
            self.vecinos[n] = set()

    def ConectarNodos(self, n1, n2, peso = 1):
        if n1 not in self.nodos:
            self.AgregarNodo(n1)
        if n2 not in self.nodos:
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
            print("set terminal png truecolor", file = f)
            print("set output '" + self.nombre + ".png'", file = f)
            print("set key off", file = f)
            print("set size square", file = f)
            print("unset colorbox", file = f)
            print("set title'" + titulo + "'", file = f)

            for n in self.nodos:
                print("set object circle at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " fillcolor rgb '" + n.color + "' front fillstyle solid noborder size " + str(n.radio), file = f) # http://www.bersch.net/gnuplot-doc/layers.html

            i = 1 # Deben ser mayores a 1
            for n in self.nodos:
                for v in self.vecinos[n]:
                    print("set arrow " + str(i) +
                        " from " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " to " + str(v.posicion[0]) + "," + str(v.posicion[1]), end = "", file = f) # https://stackoverflow.com/questions/5598181/multiple-prints-on-the-same-line
                    if self.dirigido:
                        print("", file = f)
                    else:
                        print(" nohead", file = f)
                i = i + 1

            print("set style fill transparent solid 0.5 noborder", file = f)
            print("plot [-0.1:1.1][-0.1:1.1] NaN t''", file = f)
            print("quit", file = f)

        system("gnuplot " + self.nombre +".gnu")
