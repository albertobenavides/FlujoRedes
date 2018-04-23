'''
rejilla k x k

aristas simétricas: parametrizadas por l (umbral de distancia de manhatan)
l <= k; l puede tomar valores pequeños
Si l vale 0: no hay ninguna conexión
Si l vale 1: los nodos se conectan con 1 vecinos en distancia manhatan
Si l vale 2: los nodos se conectan en 2 vecinos...
Vecindades de manhatan 1-3

¿Qué pasa al modelo si se hace un torus? Oh, dizque impresionaría a Elisa.

s y t están en las esquinas

p muy pequeño (3 vecinos, 4 vecinos) probabilidad de agregar saltos cuánticos :o; se conecta con arista dirigida, random

más grande k -> más pequeño p

la gran mayoría de aristas de l (comida), la minoría de p (condimento)

calcular flujo máximo de s (superior izquierda) a t (inferior derecha); k, l, p modifican flujo

capacidades a estas aristas.

Ponderar aristas con pesos de una distribución normal de enteros. Elegir una media y una desviación estándar. Podemos experimentar cuánto afectaría eso. Evitar negativos y ceros. Elisa haría: redondear hacia arriba más 1, a ver qué pasa, aunque hay otras formas

p es de distribución exponencial: Para los pesos de largo alcance, se usará una distribución exponencial para que haya muchos pequeños, pero alguno muy grande :o

Bucar paquetes que generen distribuciones normales y exponenciales en python.

Dibujar grosor o color en los arcos. Implementar colores a los arcos dependiendo de dónde salen.

1) Escribir un generador que crea grafo y visualiza
2) Percolar (?): percolación de vértices y aristas. Quitar cosas.

Percolar aristas es eliminar aristas. Se elimina una arista al azar. Esto puede reduci el flujo máximo. Se quitan una tras otra y se ve qué le pasa al flujo máximo. Se dejan de quitar aristas cuando s ya no alcanza a t. Ya que no es posible llegar de s a t, no se sigue.

Se quiere ver cuándo es el maxflow (y) y cua´ntas aristas se han quitado (x). Conviene correr réplicas (y hacer diagramas de caja y bigotes entre quitar 1, 2, 3... aristas)

Ejemplo: red fluvial, qué tanto se disminuye la capacidad del sistema cuando uno se tapa

Percolación de vértices: Quitar un nodo y todas las aristas que entran y salen de ese nodo. El colapso del flujo debería ser más drástico que al eliminar vérticies. Quitar vértices sería comparable a quitar usuarios de una red social (interesados en propagación de rumores)

Mientras se percola, se ve el efecto del maxflow. Ver qué le pasa al tiempo de ejecución del algoritmo. Si se pone más rápido o más lento. Quizás debería ponerse más rápido. Y también es posible que no se ponga más rápido. A ver qué. El tipo de ejecución no depende sólo del tamaño. Graficar para ver ver qué pasa mientras se percola.

1)Descripción de la implementación del modelo
2) Describir cómo se implementa la percolación de aristas
3) qué pasó al maxflow
4) percolación de vértices y qué les pasa.

Se usa el ford-fulkerson para medir las cosas

Un dibujo que muestre cómo van quedando las estrucutars.

En los parámetros de los pesos, mostrar cómo varían. Mostrar como varían las l.

Calcular el flujo. Visualizar el flujo. Eso sería interesante. Ver cómo modificarlo en Ford-Fulkerson. Se puede poner rojo si está en capacidad máxima, negra si no cabe. Depurar: dibujar el flujo para comprender lo que sucede. Podría ser por grados de rojo.
'''

import sys
sys.path.append('../../fuente/')

from Grafo import Grafo
from Nodo import Nodo
from random import random
from math import sqrt, floor

k = 20 # lado
k = k ** 2

lado = floor(sqrt(k))

G = Grafo()
G.dirigido = True

for i in range(k):
    n = Nodo()
    if i == 0:
        n.id = "s"
    elif i == k-1:
        n.id = "t"
    else:
        n.id = ""
    n.radio = 3 / k
    n.posicion = ((i % lado) / lado, 1 - int(i / lado) / (lado - 1)) # la parte de la y tiene 1 - para que empiece desde arriba y no desde abajo
    G.AgregarNodo(n)

for i in range(k - 1):
    if i % lado != lado - 1:
        G.ConectarNodos(G.nodos[i], G.nodos[i + 1])

    if int(i / lado) < lado and i < lado ** 2 - lado:
        G.ConectarNodos(G.nodos[i], G.nodos[i + lado])

G.DibujarGrafo("Rejilla")
