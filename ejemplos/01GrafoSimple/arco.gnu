set terminal png truecolor
set output 'arco.png'
set key off
set size square
unset colorbox
set title'Ejemplo 1.2 Un arco'
set label '1' at 0.5,0.5 left offset char -0.4,0
set object circle at 0.5,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set label '2' at 1,1 left offset char -0.4,0
set object circle at 1,1 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.1
set arrow 1 from 0.5707106781186547,0.5707106781186547 to 0.9292893218813453,0.9292893218813453 linewidth 1 nohead
set style fill transparent solid 0.5 noborder
plot [-0.1:1.1][-0.1:1.1] NaN t''
quit
