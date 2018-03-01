# Grafos con `python` para Flujo en Redes

Este repositorio pretende ofrecer un programa que permita generar y trazar grafos enfocados a representar problemas de Flujo en redes, aunque podría utilizarse para otros fines.

## Requisitos

Es necesario tener instalados:
* [`python3`][08100e87]
* [`gnuplot`][a873f787]

También se requiere incluir las librerías [`Grafo`](fuente/Grafo.py) y [`Nodo`](fuente/Nodo.py).

```python
from Grafo import Grafo
from Nodo import Nodo
```

Nota: Los usuarios de `Windows` deben agregar los directorios de instalación de ambos programas al `PATH` de `Windows` para poder correr los ejemplos desde el `Símbolo del sistema`. Instrucciones para [`python3`][862993bb] y [`gnuplot`][2294b1ea].


## Documentación

La carpeta [`ejemplos`](ejemplos/) contiene los códigos que aquí se explican.

### Estructura mínima

 Para definir un grafo con un nodo y obtener una imagen `PNG` del mismo, basta con escribir el siguiente [código](ejemplos/01GrafoSimple/main.py):

```python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
n1 = Nodo()
G.AgregarNodo(n1)

G.DibujarGrafo("Ejemplo 1.1 Un nodo")
```

![](ejemplos/01GrafoSimple/grafo.png?raw=true)

### Grafos

```
G = Grafo()
```

Esta instrucción crearía un **grafo** *G* almacenado en la variable `G` con las siguientes propiedades:

Propiedad | Variable   | Valor por defecto
----------|------------|------------------
Nombre    | `nombre`   | `"grafo"`
Dirigido  | `dirigido` | `False`
Nodos     | `nodos`    | `[]`
Pesos     | `pesos`    | `dict()`
Vecinos   | `vecinos`  | `dict()`

El **nombre** del grafo indica el nombre de los archivos de imagen o instrucciones de `gnuplot` que se generarán de este grafo. Así, un grafo generado de manera predeterminada produciría archivos de imagen `grafo.png`.

Cambiar el nombre de un grafo en `G` por ["arco"](ejemplos/01GrafoSimple/main.py) se realiza del modo siguiente:

```python
G.nombre = "arco"
```

Para definir si un grafo *G* es **dirigido**, basta con especificarlo mediante una booleana:

```python
G.dirigido = True # G es dirigido

G.dirigido = False # G no es dirigido
```

Un grafo no dirigido, mantiene a los nodos vecinos conectados uno con el otro y representa esto mediante arcos sin flecha de dirección.

![](ejemplos/01GrafoSimple/arco.png?raw=true)

Un grafo dirigido considera que cada nodo podría dirigirse a vecinos que no necesariamente se dirijan a él, lo que se representa mediante arcos con una flecha que indica esta dirección.

![](ejemplos/03Arcos/grafo.png?raw=true)

Los nodos, vecinos y pesos se describirán en las secciones siguientes.


### Nodos

De manera análoga a la creación de un grafo, para crear un nodo *n* almacenado en la variable `n` se escribe:

```python
n = Nodo()
```

Por defecto, un nodo tiene las siguientes propiedades:

Propiedad  | Variable  | Valor por defecto
--|---|--
Identificador  | `id`  |  `"1"`
Tipo  | `tipo`  | `""`
Posición  | `posicion`  | `(0.5, 0.5)`
Radio  | `radio`  | `0.1`
Color (hexadecimal)  | `color`  | `"#0080808080"` (Gris)

El **identificador** se utiliza para mostrar una etiqueta en color negro dentro del nodo al dibujarlo. Se puede definir otro identificador con:

```python
n.id = "2" # Dibujaría un nodo con un 2 en el centro

n.id = "" # Dibujaría nodos sin etiqueta
```

El **tipo** es una variable que podría ser utilizada para definir categorías de nodos [falta agregar ejemplo de asignación de horarios].

La **posición** establece las coordenadas del centro del nodo para ser representado en un plano cartesiano bidimensional. Colocar un nodo en (0, 1) se haría así:

```python
n.posicion = (0, 1) # 0 para el eje horizontal (x) y 1 para el vertical (y)
```

El **radio** controla el tamaño del nodo con base en las unidades del eje de coordenadas, de modo que, por ejemplo, 0.5 de radio corresponderían a un nodo que ocupe una unidad del eje de coordenadas de diámetro. El valor del radio puede ser entero o decimal, de modo que podría asignársele valores a partir de operaciones que den por resultado este tipo de valores. Un radio de 0.3 periódico de un nodo se asigna mediante:

```python
n.radio = 1 / 3
```

El **color** de un nodo se establece con la función `Color`, que recibe como parámetros el componente rojo, verde, azul y, opcionalmente, alfa (transparencia) en rangos de números enteros de 0 a 255, para generar un color [RGBA](https://developer.mozilla.org/es/docs/Web/CSS/CSS_Colors/Herramienta_para_seleccionar_color). Para asignar cambios de color a un nodo se escribe:

```python
n.Color(255, 255, 0) # Nodo a color amarillo

n.Color(255, 0, 255, 128) # Nodo a color morado, transparencia media
```

![](ejemplos/02Nodos/grafo.png?raw=true)

### Arcos

Para establecer una vecindad en un grafo en `G` entre un nodo en `n` y otro en `v` con peso 1, se utiliza la función `ConectarNodos` del grafo:

```python
G.ConectarNodos(n, v)
```

Esta función realiza las siguientes acciones:
1. Agrega ambos nodos al grafo, en caso de no estarlo.
2. Establece una vecindad que va de *n* a *v*
3. Establece un peso de 1 para dicha vecindad

Además, si se trata de un grafo no dirigido, realiza los pasos 2 y 3 de *v* a *n*.

El **peso** inicial de una vecindad se puede modificar pasando como tercer parámetro de la función `ConectarNodos` el peso que se desee. Una vecindad con peso 0.5 entre *n* y *v* quedaría:

```python
G.ConectarNodos(n, v, 0.5)
```

Este peso se corresponderá con el grosor del arco que conecte a los nodos en la representación del grafo.

### Dibujar grafo

Las siguientes línea dibujar un grafo en `G` sin título y con título "Título":

```python
G.DibujarGrafo() # Imagen de un grafo sin título

G.DibujarGrafo("Título") # Imagen de un grafo con encabezado "Título"
```

## Tareas pendientes
- [x] ~~Arcos simples~~
- [x] ~~Configuración de nodos~~
- [x] Configuración de grafos
- [x] Completar documentación de arcos
- [ ] Eliminar vecindades
- [ ] Modificar pesos de vecindades
- [ ] Agregar ejemplo de asignación de horarios
- [ ] Nodos sólo con contorno y grosor de contorno
- [ ] Agregar rangos de los ejes del plano a dibujar
- [ ] Ejemplos de aplicación con algoritmo genético para tipos de nodo
- [ ] Ejemplo de aplicación de flujo en redes ()
- [ ] Agregar imágenes en formato `EPS`
- [ ] Agregar conexiones de un mismo nodo consigo mismo

  [862993bb]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Proceso de agregado de carpetas al `PATH` de Windows."
  [08100e87]: https://www.python.org/downloads/ "Descargas de `python3`."
  [a873f787]: https://sourceforge.net/projects/gnuplot/files/gnuplot/ "Descarga de `gnuplot`."
  [2294b1ea]: https://superuser.com/questions/1042480/execute-gnuplot-from-cmd "Instrucciones para agregar carpetas de `gnuplot` al `PATH` de Windows."
