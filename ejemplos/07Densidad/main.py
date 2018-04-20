import sys
sys.path.append('../../fuente/')
from math import floor, pi
from os import system, remove
from Grafo import Grafo
from Nodo import Nodo

debug = False
N = 40
ka = 20
umbral = floor(N / 2)
if ka > umbral:
    ka = umbral
#print(ka)
veces = 0

for k in range(1, ka + 1):
    G = Grafo()
    for i in range(0, N):
        n = Nodo()
        n.id = ""
        G.AgregarNodo(n)
        if k > i: # Si la k es mayor al número en que se va
            t = i # Se conectará con i anteriores
        else: # Si no,
            t = k # Se conectará con k anteriores; así se evita salir del rango
        for j in range(0, t): # Se conecta con tantos nodos anteriores como k haya
            G.ConectarNodos(G.nodos[i], G.nodos[i - j - 1])
            veces += 1
        if k + i >= N: # Si hace falta conectarse con nodos siguientes, se conecta exactamente con el excedente de nodos faltantes
            for extra in range(0, k + i - N + 1):
                G.ConectarNodos(G.nodos[i], G.nodos[extra])
                veces += 1

    #print(veces)
    G.Circular(G.nodos)
    G.nombre = "{:03d}".format(k)
    print(G.DistanciaPromedio())
    if debug:
        G.DibujarGrafo()
        remove('{:03d}.gnu'.format(k))

        G.nombre = "{:03d}".format(2 * ka + 1 - k)
        G.DibujarGrafo()
        remove('{:03d}.gnu'.format(2 * ka + 1 - k))

if debug:
    system("magick -delay 10 0*.png p.gif")
