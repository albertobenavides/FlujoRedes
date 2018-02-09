from random import random
import os

n = 5

for i in range(n):
    x = random()
    y = random()
    c = random()
    with open ("secuencia.csv", "a") as s:
        print(x, y, c, file = s)
        with open("secuencia.txt", "w") as g:
            print("set terminal png truecolor", file = g)
            print("set output 'images/" + str(i) + ".png'", file = g)
            print("set key off", file = g)
            print("unset colorbox", file = g)
            print("set style circle radius 0.001", file = g)
            print("set style fill transparent solid 0.5 noborder", file = g)
            print("plot [0:1][0:1] 'secuencia.csv' u 1:2:($3*256) w circles fc var", file = g)
        os.system("gnuplot secuencia.txt")
os.remove("images/")
