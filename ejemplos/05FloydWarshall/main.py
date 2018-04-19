import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
# Comentar si se desea obtener un grafo no dirigido
G.dirigido = True
G.nombre = "ejemploDirigido"
# Hasta aquí

a = Nodo()
a.id = 'a'
a.posicion = (0,0)

b = Nodo()
b.id = 'b'
b.posicion = (1,0)

c = Nodo()
c.id = 'c'
c.posicion = (1,1)

d = Nodo()
d.id = 'd'
d.posicion = (0,1)

G.ConectarNodos(a, b, 5)
G.ConectarNodos(a, c, 7)
G.ConectarNodos(b, c, 2)
G.ConectarNodos(c, d, 4)
G.ConectarNodos(b, d, 3)

#G.DibujarGrafo("Ejemplo 5. Arcos con etiqueta", mostrarPesos = True, eps = True)
# G.DibujarGrafo("Ejemplo de grafo con 4 nodos", mostrarPesos = True, eps = True)
G.DibujarGrafo("Ejemplo de grafo dirigido con 4 nodos", mostrarPesos = True, eps = True)

for (k, val) in G.Floyd_Warshall().items(): # toma el camino más corto entre todos los nodos
    n = k[0]
    v = k[1]
    print(n.id, v.id, val)

print("a -> b: " + str(G.Ford_Fulkerson(a, b)))
print("a -> d: " + str(G.Ford_Fulkerson(a, d)))
