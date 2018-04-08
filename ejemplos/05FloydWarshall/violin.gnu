set terminal png truecolor
set output 'boxplotFord.png'
set key off

set title 'Diagramas de caja bigote para Ford-Fulkerson'
set xlabel 'Potencias de 2 nodos por grafo'
set ylabel 'Logaritmo de tiempo de procesamiento'
#set logscale y
set style fill solid 0.25 border -1
set style boxplot outliers pointtype 7
set style data boxplot
#f(x) = 150 * exp(x) - 12

plot "tiempos.txt" using (-8):(log($3)):(0.5):1

#http://soc.if.usp.br/manual/gnuplot-doc/htmldocs/boxplot.html
