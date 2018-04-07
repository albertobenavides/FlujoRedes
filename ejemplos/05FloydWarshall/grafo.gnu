set terminal postscript color enhanced
set output 'grafo.eps'
set key off
set size square
unset colorbox
set title'Ejemplo de grafo con 4 nodos'
set label 'a' at 0,0 left offset char -0.4,0
set object circle at 0,0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set label 'b' at 1,0 left offset char -0.4,0
set object circle at 1,0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set label 'c' at 1,1 left offset char -0.4,0
set object circle at 1,1 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set label 'd' at 0,1 left offset char -0.4,0
set object circle at 0,1 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set arrow 1 from 0.07071067811865475,0.07071067811865475 to 0.9292893218813453,0.9292893218813453 linewidth 7
set arrow 2 from 0.1,0.0 to 0.9,0.0 linewidth 5
set arrow 3 from 1.0,0.1 to 1.0,0.9 linewidth 2
set arrow 4 from 0.9292893218813453,0.07071067811865475 to 0.07071067811865475,0.9292893218813453 linewidth 3
set arrow 5 from 0.9,1.0 to 0.1,1.0 linewidth 4
set style fill transparent solid 0.5 noborder
plot [-0.1:1.1][-0.1:1.1] NaN t''
