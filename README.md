# Grafos con `python` para Flujo en Redes

Este repositorio pretende ofrecer un programa que permita generar y trazar grafos enfocados a representar problemas de Flujo en redes, aunque podría utilizarse para otros fines.

## Requisitos

Es necesario tener instalados:
* [`python3`][08100e87]
* [`gnuplot`][a873f787]

Los usuarios de `Windows` deben agregar los directorios de instalación de ambos programas al `PATH` de `Windows` <note id="b1">[[1]](#a1)</note> para poder correr los ejemplos desde la `Consola de comandos`.

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
* Nombre: "grafo"
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

La imagen del grafo generado hasta este punto muestra un eje de coordenadas con título **Ejemplo 1** donde aparece plasmado un nodo en color gris, con centro en (0.5, 0.5), radio 0.1 e identificador "1":

![](https://raw.githubusercontent.com/jbenavidesv87/FlujoRedes/master/ejemplos/01GrafoSimple/grafo.png)

De momento <note id="b2">[[\*]](#a2)</note>, para trazar arcos en un grafo hacen falta al menos dos nodos vecinos que ocupen una posición distinta, por lo que primero se tendría que agregar otro nodo, *n<sub>2</sub>*, al grafo. En esta ocasión, tras crear el nodo, se modificará su identificador y posición, para finalmente agregarlo al grafo *G* antes definido, todo lo cual se hará mediante las instrucciones:

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

El programa completo de este primer ejemplo puede consultarse en `ejemplos/01GrafoSimple/main.py`.

## Tareas pendientes
- [ ] Arcos simples
- [ ] Configuración de nodos
- [ ] Configuración de grafos
- [ ] Ejemplos de aplicación con algoritmo genético
- [ ] Ejemplo de aplicación de flujo en redes
- [ ] Agregar imágenes en formato `EPS`
- [ ] <note id="a2">[*](#b2) Agregar conexiones de un mismo nodo consigo mismo

  <note id="a1">[1](#b1)</note>: Instrucciones para [`python3`][862993bb] y [`gnuplot`][2294b1ea]

  [862993bb]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Proceso de agregado de carpetas al `PATH` de Windows."
  [08100e87]: https://www.python.org/downloads/ "Descargas de `python3`."
  [a873f787]: https://sourceforge.net/projects/gnuplot/files/gnuplot/ "Descarga de `gnuplot`."
  [2294b1ea]: https://superuser.com/questions/1042480/execute-gnuplot-from-cmd "Instrucciones para agregar carpetas de `gnuplot` al `PATH` de Windows."
