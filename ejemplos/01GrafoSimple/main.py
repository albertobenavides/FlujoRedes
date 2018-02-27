import sys
sys.path.append('../../fuente/') # https://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
n = Nodo()
G.AgregarNodo(n)

G.DibujarGrafo("Ejemplo 1")
