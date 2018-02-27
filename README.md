<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Grafos con `python` para Flujo en Redes

Este repositorio pretende ofrecer un programa que permita generar y trazar grafos enfocados a representar problemas de Flujo en redes, aunque podría utilizarse para otros fines.

## Instalación

Es necesario tener instalados:
* [`python3`][08100e87]
* [`gnuplot`][a873f787]

Además, los usuarios de `Windows` podrían encontrar conveniente agregar los directorios de instalación de ambos programas al `PATH` de `Windows`[^path] para poder correr los ejemplos desde la `Consola de comandos`.

## Documentación

Para crear un grafo $5$ basta con escribir el siguiente programa:

``` python
from Grafo import Grafo
from Nodo import Nodo

G = Grafo()
```

[^path]: Instrucciones para [`python3`][862993bb] y [`gnuplot`][2294b1ea]

  [862993bb]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Proceso de agregado de carpetas al `PATH` de Windows."
  [08100e87]: https://www.python.org/downloads/ "Descargas de `python3`."
  [a873f787]: https://sourceforge.net/projects/gnuplot/files/gnuplot/ "Descarga de `gnuplot`."
  [2294b1ea]: https://superuser.com/questions/1042480/execute-gnuplot-from-cmd "Instrucciones para agregar carpetas de `gnuplot` al `PATH` de Windows."
