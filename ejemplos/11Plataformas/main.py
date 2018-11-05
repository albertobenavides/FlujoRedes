import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()

n = Nodo()
n.radio = 0.01
n.posicion = (
    0.5 + n.radio * cos(theta * i), 0.5 + n.radio * sin(theta * i)
)
G.AgregarNodo(n)

G.ConectarNodos(n, v[0], random() * 2)

G.DibujarGrafo("Ejemplo 3. Arcos")
