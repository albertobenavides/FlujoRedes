# Documentación de modificaciones a los algoritmos de la profe
# Ejempos para revisar si funciona el algoritmo correcto
# Revisar si funciona con grafos dirigidos
# Crear grafos de diferentes tamaños y correr los algoritmos para graficar los tiempos que les toma a los algoritmos correrse; graficar con diagramas caja bigote y violín; y error bars (x, y, largo) y candlesticks (parte baja, alta, cuartil, cuartil, meidana)
# Revisar con pruebas estadísticas si los datos son normalmente distribuidos
# ¡¡¡Ajuste de curvas!!!; gnuplot con fit()
# Ver qué tanto se ajusta lo teórico esperado con lo experimental y describir los comportamientos
# Definir curva teórica y experimental
# Buscar en Folk-Fulkerson
# Aristas directamente proporcionales al número de nodos (por densidad, como un 0.1 de aristas por cantidad de nodos)

import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
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

#print(G.vecinos[a])
#print(G.nodos)
#print(G.pesos)

G.DibujarGrafo("Test")

for (k, val) in G.Floyd_Warshall().items():
    n = k[0]
    v = k[1]
    print(n.id, v.id, val)

print("a -> b: " + str(G.Ford_Fulkerson(a, b)))

print("a -> d: " + str(G.Ford_Fulkerson(a, d)))
