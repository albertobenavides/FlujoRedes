# Ejemplo 1. Grafo simple
<span style="font-family:Palatino"></span>

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

![](grafo.png?raw=true)

De momento [falta agregar conexiones de un mismo nodo consigo mismo], para trazar arcos en un grafo hacen falta al menos dos nodos vecinos que ocupen una posición distinta, por lo que primero se tendría que agregar otro nodo, *n<sub>2</sub>*, al grafo. En esta ocasión, tras crear el nodo, se modificará su identificador y posición, para finalmente agregarlo al grafo *G* antes definido, todo lo cual se hará mediante las instrucciones:

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

![](arco.png?raw=true)
