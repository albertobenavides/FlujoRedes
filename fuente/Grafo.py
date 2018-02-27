from math import sqrt, atan, sin, cos
from os import system
class Grafo:

    def __init__(self, nombre = "grafo"):
        self.nombre = nombre
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
                print("set label '" + str(n.id) + "' at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " left offset char -" + str(0.4 * len(n.id)) + ",0", file = f) # https://stackoverflow.com/questions/23690551/how-do-you-assign-a-label-when-using-set-object-circle-in-gnuplot
                print("set object circle at " + str(n.posicion[0]) + "," + str(n.posicion[1]) + " fillcolor rgb '" + n.color + "' fillstyle solid noborder size " + str(n.radio), file = f) # http://www.bersch.net/gnuplot-doc/layers.html

            i = 1 # Deben ser mayores a 1
            for n in self.nodos:
                for v in self.vecinos[n]:
                    x1 = n.posicion[0]
                    y1 = n.posicion[1]

                    x2 = v.posicion[0]
                    y2 = v.posicion[1]

                    m = (y2 - y1) / (x2 - x1)
                    alfa = atan(m)

                    xNodo = n.radio * cos(alfa)
                    yNodo = n.radio * sin(alfa)
                    xVecino = -v.radio * cos(alfa)
                    yVecino = -v.radio * sin(alfa)

                    if x1 > x2:
                        xNodo = xNodo * -1
                        yNodo = yNodo * -1
                        xVecino = xVecino * -1
                        yVecino = yVecino * -1

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
