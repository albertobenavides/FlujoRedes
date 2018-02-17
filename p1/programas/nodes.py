from random import random
from math import sqrt

n = 100
u = 0.3
sqrt2 = sqrt(2)
nodes = list()

def ProbabilidadEuclidiana (x1, y1, x2, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d < u:
        return 1 - d / sqrt2
    else:
        return 0

with open("nodes.csv", "w") as f:
    for i in range(n):
        x = random()
        y = random()
        r = random()
        c = random()
        nodes.append((x, y))
        print(str(x) + " " + str(y) + " " + str(r) + " " + str(c) + " ", file = f)

print("set terminal png")
print("set output 'nodes.png'")
print("set key off")
print("unset colorbox")
print("set size square")
print("set xrange[-0.1 to 1.1]")
print("set yrange[-0.1 to 1.1]")
for i in range(n - 1):
    (x1, y1) = nodes[i]
    for j in range(i + 1, n):
        (x2, y2) = nodes[j]
        if random() < ProbabilidadEuclidiana(x1, y1, x2, y2):
            print("set arrow " + str(i + j) + " from " + str(x1) + ", " + str(y1) + " to " + str(x2) + ", " + str(y2) + " nohead")
print("show arrow")
print("plot 'nodes.csv' using 1:2:($3 * 2):($4 * 256) with points pt 7 ps var lc palette frac var")
