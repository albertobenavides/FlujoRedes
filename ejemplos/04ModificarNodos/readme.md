# Ejemplo 4. Manipular nodos

En este ejemplo se un grafo *G*, dirigido y que lleva por nombre **dirigido** al que se le agregan veinte nodos a los que se les identifica por números enteros consecutivos, del 0 al 19, se les da un radio de 0.08 y una posición que los conforma en una red. Dicha posición está calculada a partir de los siguientes datos:

* *N* = 20 nodos
* *L* =
	&lceil; <span style="white-space: nowrap; font-size:larger">
&radic;<span style="text-decoration:overline;">&nbsp;20&nbsp;</span>
</span>	&rceil; : Nodos por fila y columna

La ecuación del par ordenado para la posición *p<sub>i</sub>* de cada nodo *n<sub>i</sub>* con *i* &in; {0, 1, 2, ..., *N - 1*} es:

*p<sub>i</sub>* = ( (*i* mod *L*) / *L* , &lfloor;(*i* / *L*)&rfloor; / *L* )

Cada uno de estos nodos se conecta con sus vecinos horizontales y verticales inmediatos.

Después, se elige el nodo con identificador **3**, se cambia su color a rojo y su posición a (1, 0) con el código:

```python
n = G.NodoConId(3)
n.Color(255, 0, 0)
n.posicion= (1, 0)
```

A continuación, se toma el nodo que tiene identificador **5**, se le asigna el color azul y se eliminan sus vecindades:

```python
n = G.NodoConId(5)
n.Color(0, 255, 0)
G.EliminarVecindades(n)
```

Después, se elimina el nodo con identificador **14**:

```python
n = G.NodoConId(14)
G.EliminarNodo(n)
```

Enseguida, se ponen los pesos de las vecindades del nodo **4** a un valor de 3:

```python
n = G.NodoConId(4)
G.ModificarPesos(n, 3)
```

Ahora, se dibuja el grafo dirigdo resultante, mostrado en la imagen siguiente:

![](dirigido.png?raw=true)

Para finalizar, se cambia el grafo a no dirigido y su nombre se actualiza a **noDirigido** y se modifican los pesos del nodo con identificador **11**. Este grafo resultante se muestra en una imagen en formato `EPS`:

![](noDirigido.png?raw=true)
