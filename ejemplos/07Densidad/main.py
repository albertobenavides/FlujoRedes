import sys
sys.path.append('../../fuente/')
from math import floor

from Grafo import Grafo
from Nodo import Nodo

G = Grafo()

N = 21
k = 10
umbral = floor(N / 2)
if k > umbral:
    k = umbral
#print(k)
veces = 0

for i in range(0, N):
    n = Nodo()
    n.id = ""
    G.AgregarNodo(n)
    if k > i: # Si la k es mayor al número en que se va
        t = i # Se conectará con i anteriores
    else: # Si no,
        t = k # Se conectará con k anteriores; así se evita salir del rango
    for j in range(0, t): # Se conecta con tantos nodos anteriores como k haya
        G.ConectarNodos(n, G.nodos[i - j - 1])
        veces += 1
    if k + i >= N: # Si hace falta conectarse con nodos siguientes, se conecta exactamente con el excedente de nodos faltantes
        for extra in range(0, k + i - N + 1):
            G.ConectarNodos(n, G.nodos[extra])
            veces += 1

#print(veces)
G.Circular(G.nodos)
G.DibujarGrafo()
