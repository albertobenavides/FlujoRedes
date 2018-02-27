set terminal png truecolor
set output 'grafo.png'
set key off
set size square
unset colorbox
set title'Ejemplo 1'
set label '1' at 0.5,0.5 left offset char -0.4,0
set object circle at 0.5,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set style fill transparent solid 0.5 noborder
plot [-0.1:1.1][-0.1:1.1] NaN t''
quit
