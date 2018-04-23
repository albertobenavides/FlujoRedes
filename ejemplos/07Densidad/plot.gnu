set terminal png truecolor
set output 'img/N128k064.png'
set key off
set title 'N = 128; k = 64'
set xlabel 'Probabilidad'
set ylabel 'Distancia promedio normalizada (azul)'
set y2label 'Densidad promedio (rojo)'
set style line 1 lc rgb '#0000ff' lt 1 lw 1
set style line 2 lc rgb '#ff0000' lt 1 lw 1
plot[0:0.5][0:1] 'results/N128k064.csv' using 1:3 w lines ls 1, 'results/N128k064.csv' using 1:5 w lines ls 2
