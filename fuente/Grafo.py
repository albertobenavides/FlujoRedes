from math import sqrt
from os import system
class Grafo:

    def __init__(self):
        self.nombre = "grafo"
        self.dirigido = False
        self.nodos = [] # un conjunto
        self.pesos = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo

    def AgregarNodo(self, n):
        self.nodos.append(n)
        if not n in self.vecinos: # vecindad de v
            self.vecinos[n] = set()

    def ConectarNodos(self, n1, n2, peso = 1):
        if n1 not in self.nodos:
            self.AgregarNodo(n1)
        if n2 not in self.nodos:
            self.AgregarNodo(n2)
        self.vecinos[n1].add(n2)
        self.pesos[(n1, n2)] = peso
        if not self.dirigido:
            self.vecinos[n2].add(n1) # Si no es dirigido, también debería haber una conexión bivalente
            self.pesos[(n2, n1)] = peso

    def Distancia(self, p1, p2):
        d = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return d

    def DistanciaTotal(self):
        d = 0.0
        for n in self.vecinos:
            for v in self.vecinos[n]:
                d += self.Distancia(n.posicion, v.posicion)
        return d

    def DibujarGrafo(self, titulo = ""):
        self.nombre = str(self.nombre)
        with open(self.nombre + ".gnu", "w") as f:
            print("set terminal png truecolor", file = f)
            print("set output '" + self.nombre + ".png'", file = f)
            print("set key off", file = f)
            print("set size square", file = f)
            print("unset colorbox", file = f)
            print("set title'" + titulo + "'", file = f)

            for n in self.nodos:
                n.id = str(n.id)
                if len(n.id) > 0:
                    n.id = str(n.id)
                    print("set label '" + str(n.id) + "' at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " left offset char -" + str(0.4 * len(n.id)) + ",0", file = f) # https://stackoverflow.com/questions/23690551/how-do-you-assign-a-label-when-using-set-object-circle-in-gnuplot
                print("set object circle at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " fillcolor rgb '" + n.color + "' fillstyle solid noborder size " + str(n.radio), file = f) # http://www.bersch.net/gnuplot-doc/layers.html

            i = 1 # Deben ser mayores a 1
            for n in self.nodos:
                for v in self.vecinos[n]:
                    d = self.Distancia(n.posicion, v.posicion)

                    x1 = n.posicion[0]
                    y1 = n.posicion[1]

                    x2 = v.posicion[0]
                    y2 = v.posicion[1]

                    xNodo = n.radio * (x2 - x1) / d
                    yNodo = n.radio * (y2 - y1) / d

                    xVecino = n.radio * (x1 - x2) / d
                    yVecino = n.radio * (y1 - y2) / d

                    x1 = x1 + xNodo
                    x2 = x2 + xVecino
                    y1 = y1 + yNodo
                    y2 = y2 + yVecino

                    print("set arrow " + str(i) +
                        " from " + str(x1) + "," + str(y1) + " to " + str(x2) + "," + str(y2) + " linewidth " + str(self.pesos[(n, v)]), end = "", file = f) # https://stackoverflow.com/questions/5598181/multiple-prints-on-the-same-line
                    if self.dirigido:
                        print("", file = f)
                    else:
                        print(" nohead", file = f)
                    i = i + 1

            print("set style fill transparent solid 0.5 noborder", file = f)
            print("plot [-0.1:1.1][-0.1:1.1] NaN t''", file = f)
            print("quit", file = f)

        system("gnuplot " + self.nombre +".gnu")
