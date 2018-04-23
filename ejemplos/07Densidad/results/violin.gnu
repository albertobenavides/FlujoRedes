set terminal png truecolor size 800, 480
set output 'Tiempos.png'
set key off

set style fill solid 0.25 border -1
set style boxplot outliers pointtype 7
set style data boxplot
set logscale y
set ylabel "Logaritmo de tiempo en segundos"
set xlabel "k"
plot "todos.csv" using 1:4:(0.5):2

#http://soc.if.usp.br/manual/gnuplot-doc/htmldocs/boxplot.html
