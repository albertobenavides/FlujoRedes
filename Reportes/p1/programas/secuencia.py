# Generador de n círculos en n pasos, graficados en cuadro unitario
from random import random
import os

n = 100 # Cantidad de círculos

os.system("del img") # Elimina el contenido de img (png generados)
os.system("del secuencia.csv") # Borra archivo donde se almacena la secuencia de círculos que se generan

for i in range(n):
    x = random() # Posición en x
    y = random() # Posición en y
    c = random() # Color al azar
    with open ("secuencia.csv", "a") as s: # Archivo que guarda secuencias de círculos
        print(x, y, c, file = s)
        with open("secuencia.txt", "w") as g: # Archivo que guarda el estado actual de círculos dibujados, se leerá en gnuplot
            print("set terminal png truecolor", file = g)
            print("set output 'img/" + str(i).zfill(3) + ".png'", file = g)
            print("set key off", file = g)
            print("set size square", file = g)
            print("unset colorbox", file = g)
            print("set style circle radius 0.1", file = g)
            print("set style fill transparent solid 0.5 noborder", file = g)
            print("plot [0:1][0:1] 'secuencia.csv' u 1:2:($3 * 256) w circles lc var", file = g) # https://stackoverflow.com/questions/34532568/gnuplot-how-to-make-scatter-plots-with-transparent-points
    os.system("gnuplot secuencia.txt") # Generación de imagen por gnuplot de cada paso de creación de círculos

os.system("magick -delay 15 img/*.png secuencia.gif") # Creación de gif a partir de las imágenes generadas en cada paso de la iteración
os.system("del img")
