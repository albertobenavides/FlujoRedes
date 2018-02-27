# Grafos con `python` para Flujo en Redes

Este repositorio pretende ofrecer un programa que permita generar y trazar grafos enfocados a representar problemas de Flujo en redes, aunque podría utilizarse para otros fines.

## Instalación

Es necesario tener instalados:
* [`python3`][08100e87]
* [`gnuplot`][a873f787]

Es necesario que los usuarios de `Windows` agreguen los directorios de instalación de ambos programas al `PATH` de `Windows`[1] para poder correr los ejemplos desde la `Consola de comandos`.

## Documentación

La carpeta de `ejemplos` tiene enumerados los códigos que aquí se explican, en orden de aparición.

### Ejemplo 1. Grafo simple

Para crear un grafo *G* basta con escribir el siguiente programa:

``` python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
```

Por defecto, un grafo inicializado de esta manera tiene las siguientes propiedades:
* Nombre: "grafo"
* No dirigido
* Un arreglo de nodos vacío
* Un diccionario de pesos vacío
* Un diccionario de vecinos vacío

Para agregar un nodo *n*, hay que declararlo primero y luego añadirlo a un grafo previamente existente:

```python
[...]

n = Nodo()
G.AgregarNodo(n)
```

De esta manera, se tendrá un grafo *G* con un nodo *n* que tendrá las siguientes propiedades:
* Identificador: "1" (cadena de texto)
* Radio: 0.1
* Color: Gris (8080808000<sub>hex</sub>)
* Posición: (0.5, 0.5)

Generar una imagen `PNG` con nombre de archivo `grafo.png` y título **Ejemplo 1**, requiere una línea de código más:

```python
[...]

G.DibujarGrafo("Ejemplo 1")
```

El programa completo de este primer ejemplo queda como sigue:

```python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
n = Nodo()
G.AgregarNodo(n)

G.DibujarGrafo("Título")
```

La imagen del grafo generado muestra un nodo en color gris, con coordenadas (0.5, 0.5), radio 0.1 e identificador "1":

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/01%20Grafo%20Simple/grafo.png)


## Tareas pendientes
- [ ] Agregar imágenes en formato `EPS`
- [ ] Agregar conexiones de un mismo nodo consigo mismo
- [ ] Arcos simples
- [ ] Configuración de nodos
- [ ] Configuración de grafos
- [ ] Ejemplos de aplicación con algoritmo genético
- [ ] Ejemplo de aplicación de flujo en redes

[1]: Instrucciones para [`python3`][862993bb] y [`gnuplot`][2294b1ea]

  [862993bb]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Proceso de agregado de carpetas al `PATH` de Windows."
  [08100e87]: https://www.python.org/downloads/ "Descargas de `python3`."
  [a873f787]: https://sourceforge.net/projects/gnuplot/files/gnuplot/ "Descarga de `gnuplot`."
  [2294b1ea]: https://superuser.com/questions/1042480/execute-gnuplot-from-cmd "Instrucciones para agregar carpetas de `gnuplot` al `PATH` de Windows."
