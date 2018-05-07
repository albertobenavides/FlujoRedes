import sys
from math import floor, sqrt
from os import system, remove
sys.path.append('../../fuente/')
veces = 20

for k in range(3, 11): # Hasta k = 10 nodos por lado
    k = k ** 2
    lado = floor(sqrt(k))
    for l in range(1, int(sqrt(k)) + 1):
        if l > 3:
            break

        with open('plot.r', 'w') as f:
            f.write("suppressMessages(library(ggtern))\n")
            f.write("p <- read.csv(file='results/k{0:03d}l{1:03d}.csv', header=TRUE, sep=' ')\n".format(k, l))
            f.write("png('img/k{0:03d}l{1:03d}.png')\n".format(k, l))
            f.write("print(\n")
            f.write("ggtern(data=p,aes(a * 100 / 745, p * 1000, ford * 100 / 9)) +\n")
            f.write("geom_mask() +\n")
            f.write("geom_point(aes(colour=ford)) +\n")
            f.write("scale_color_gradient(low='green',high='red') +\n")
            f.write("scale_T_continuous(labels = seq(0, 0.1, 0.02)) +\n")
            f.write("scale_L_continuous(labels = seq(0, 750, 150)) +\n")
            f.write("scale_R_continuous(labels = seq(0, 10, 2)) +\n")
            f.write("labs(x='a', y='p', z='f', color = 'Ford-Fulkerson', title='k = {}; l = {}')\n".format(int(sqrt(k)), l))
            f.write(")\n")
            f.write("graphics.off()")

        system("rscript plot.r")
        remove('plot.r')
system("magick -delay 100 img/k*.png tern.gif")
