import sys
sys.path.append('../../fuente/') # https://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
n1 = Nodo()
G.AgregarNodo(n1)

G.DibujarGrafo("Ejemplo 1.1 Un nodo")

n2 = Nodo()
n2.id = "2"
n2.posicion = (1,1)
G.AgregarNodo(n2)

G.ConectarNodos(n1, n2)

G.nombre = "arco"
G.DibujarGrafo("Ejemplo 1.2 Un arco")
