# Grafos con `python` para Flujo en Redes

Este repositorio pretende ofrecer un programa que permita generar y trazar grafos enfocados a representar problemas de Flujo en redes, aunque podría utilizarse para otros fines.

## Requisitos

Es necesario tener instalados:
* [`python3`][08100e87]
* [`gnuplot`][a873f787]

Los usuarios de `Windows` deben agregar los directorios de instalación de ambos programas al `PATH` de `Windows` [[1]](#1) para poder correr los ejemplos desde el `Símbolo del sistema`.

## Documentación

La carpeta `ejemplos` contiene los códigos que aquí se explican, en orden de aparición.

### Ejemplo 1. Grafo simple

Para crear un grafo *G* basta con escribir el siguiente código:

``` python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
```

Por defecto, un grafo inicializado de esta manera tiene las siguientes propiedades:
* Nombre: "grafo" (cadena de texto)
* Dirigido: No

Para agregar un nodo *n<sub>1</sub>*, hay que declararlo primero y luego añadirlo a un grafo previamente existente:

```python
[...]
n1 = Nodo()
G.AgregarNodo(n1)
```

De esta manera, el grafo *G* contendrá al nodo *n1* que, a su vez, tendrá las siguientes propiedades iniciales:
* Identificador: "1" (cadena de texto)
* Radio: 0.1
* Color: Gris (8080808000<sub>hex</sub>)
* Posición: (0.5, 0.5)

Generar una imagen `PNG` con nombre de archivo `grafo.png` y título **Ejemplo 1.1 Un nodo**, requiere una línea de código más:

```python
[...]
G.DibujarGrafo("Ejemplo 1.1 Un nodo")
```

Hasta aquí, el código de este primer ejemplo queda como sigue:

```python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
n1 = Nodo()
G.AgregarNodo(n1)

G.DibujarGrafo("Ejemplo 1.1 Un nodo")
```

Cabe señalar que antes de obtener la imagen `PNG`, se crea un archivo `GNU` nombrado `grafo.gnu` (por el nombre del grafo) que contiene las instrucciones para que `gnuplot` procese la información del grafo extraida de `python`.

La imagen del grafo generado hasta este punto muestra un eje de coordenadas con título **Ejemplo 1.1 Un nodo** donde aparece plasmado un nodo en color gris, con centro en (0.5, 0.5), radio 0.1 e identificador "1":

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/01GrafoSimple/grafo.png)

De momento [[\*]](*), para trazar arcos en un grafo hacen falta al menos dos nodos vecinos que ocupen una posición distinta, por lo que primero se tendría que agregar otro nodo, *n<sub>2</sub>*, al grafo. En esta ocasión, tras crear el nodo, se modificará su identificador y posición, para finalmente agregarlo al grafo *G* antes definido, todo lo cual se hará mediante las instrucciones:

```python
[...]
n2 = Nodo()
n2.id = "2" # Identificador modificado
n2.posicion = (1,1) # Centro en (1, 1)
G.AgregarNodo(n2)
```

Enseguida se conectan ambos nodos para establecer su vecindad mediante la instrucción:

```python
[...]
G.ConectarNodos(n1, n2)
```

Un arco creado de este modo, tiene de manera predefinida un peso de 1 y una conexión bidireccional entre ambos nodos, ya que al no ser un grafo dirigido, se considera que ambos nodos están conectados entre sí.

Por último, se cambia el nombre del grafo a **arco** y se dibuja bajo el título **Ejemplo 1.2 Un arco**. Esto generará los archivos `arco.gnu` y `arco.png` correspondientes al nuevo nombre del grafo. El código para realizar esto es:

```python
[...]
G.nombre = "arco"
G.DibujarGrafo("Ejemplo 1.2 Un arco")
```

La nueva imagen muestra a *n<sub>1</sub>* acompañado de *n<sub>2</sub>* con sus propiedades predeterminadas pero con centro en (1, 1) e identificador "2"; ambos nodos unidos mediante un arco que simboliza su vecindad, como se aprecia en la imagen:

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/01GrafoSimple/arco.png)

El programa completo de este primer ejemplo puede consultarse en [`ejemplos/01GrafoSimple/main.py`](ejemplos/01GrafoSimple/main.py).


### Ejemplo 2. Nodos

En este ejemplo se crearán nodos y se modificarán sus propiedades iniciales de manera aleatoria mediante el uso de las funciones `random()` y `randint()` de la librería `random` de `python`. Al usar `random()` se genera un número decimal aleatorio entre 0 y 1, ambos incluidos; y `randint(a, b)` genera un número entero entre *a* y *b*, ambos incluidos.

```python
from Grafo import Grafo
from Nodo import Nodo
from random import random, randint # librerías de random
```

Primero se define un número total de nodos a generar, *N*, y se define un grafo *G* que los contendrá.

```python
N = 20 # Nodos totales

G = Grafo()
```

Posteriormente, se crearán *N* nodos con la ayuda de la función `range(N)`, la cual devuelve una lista de enteros de 0 hasta *N* - 1. A cada uno de estos *i* ∈ [0, 1, 2, ... , *N* - 1] nodos se les modificarán sus propiedades iniciales:
* Identificador: *i*
* Posición: Par ordenado con valores al azar entre 0 y 1 por componente
* Radio: Al azar entre 0.05 y 0.1
* Color: Componentes rojo, verde y azul con valores al azar entre 0 (mínimo) y 255 (máximo), y componente alfa (de transparencia) a 128 (punto medio del rango [0, 1, ..., 255])

Después se agregarán al grafo. Estas acciones se realizan con el siguiente código:

```python
[...]
for i in range(N): # Para todo i en [0, 1, ..., N - 1]
    n = Nodo() # Se crea el nodo i
    n.id = i # Se le asigna el identificador i
    n.posicion = (random(), random()) # Una posición al azar
    n.radio = 0.05 + 0.05 * random() # Un radio entre 0.5 y 1
    n.Color( # Se modifica el color
        randint(0, 255), # rojo (R)
        randint(0, 255), # verde (G)
        randint(0, 255),  # azul (B)
        128, # alfa (A); transparencia
    )
    G.AgregarNodo(n) # Se agrega el nodo i al grafo
```

Al final, se desplegará este grafo en un eje de coordenadas que lleve por título **Ejemplo 2. Nodos**, almacenado en una imagen `PNG` nombrada **grafo** por el nombre por defecto con que se genera el grafo con la instrucción `G.DibujarGrafo("Ejemplo 2. Nodos")`.

Una de las imágenes resultantes es:

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/02Nodos/grafo.png)


### Ejemplo 3. Arcos

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/03Arcos/grafo.png)

## Tareas pendientes
- [x] ~~Arcos simples~~
- [x] ~~Configuración de nodos~~
- [ ] Configuración de grafos
- [ ] Ejemplos de aplicación con algoritmo genético
- [ ] Ejemplo de aplicación de flujo en redes
- [ ] Agregar imágenes en formato `EPS`
- [ ] [\*] Agregar conexiones de un mismo nodo consigo mismo

  ###### 1: Instrucciones para [`python3`][862993bb] y [`gnuplot`][2294b1ea].

  [862993bb]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Proceso de agregado de carpetas al `PATH` de Windows."
  [08100e87]: https://www.python.org/downloads/ "Descargas de `python3`."
  [a873f787]: https://sourceforge.net/projects/gnuplot/files/gnuplot/ "Descarga de `gnuplot`."
  [2294b1ea]: https://superuser.com/questions/1042480/execute-gnuplot-from-cmd "Instrucciones para agregar carpetas de `gnuplot` al `PATH` de Windows."
