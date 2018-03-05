set terminal png truecolor
set output 'dirigido.png'
set key off
set size square
unset colorbox
set title'Ejemplo 4.1 Manipulación de nodos en grafo dirigido'
set label '0' at 0.0,0.0 left offset char -0.4,0
set object circle at 0.0,0.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '1' at 0.25,0.0 left offset char -0.4,0
set object circle at 0.25,0.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '2' at 0.5,0.0 left offset char -0.4,0
set object circle at 0.5,0.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '3' at 1,0 left offset char -0.4,0
set object circle at 1,0 fillcolor rgb '#00ff0000' fillstyle solid noborder size 0.08
set label '4' at 0.0,0.25 left offset char -0.4,0
set object circle at 0.0,0.25 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '5' at 0.25,0.25 left offset char -0.4,0
set object circle at 0.25,0.25 fillcolor rgb '#0000ff00' fillstyle solid noborder size 0.08
set label '6' at 0.5,0.25 left offset char -0.4,0
set object circle at 0.5,0.25 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '7' at 0.75,0.25 left offset char -0.4,0
set object circle at 0.75,0.25 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '8' at 0.0,0.5 left offset char -0.4,0
set object circle at 0.0,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '9' at 0.25,0.5 left offset char -0.4,0
set object circle at 0.25,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '10' at 0.5,0.5 left offset char -0.8,0
set object circle at 0.5,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '11' at 0.75,0.5 left offset char -0.8,0
set object circle at 0.75,0.5 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '12' at 0.0,0.75 left offset char -0.8,0
set object circle at 0.0,0.75 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '13' at 0.25,0.75 left offset char -0.8,0
set object circle at 0.25,0.75 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '15' at 0.75,0.75 left offset char -0.8,0
set object circle at 0.75,0.75 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '16' at 0.0,1.0 left offset char -0.8,0
set object circle at 0.0,1.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '17' at 0.25,1.0 left offset char -0.8,0
set object circle at 0.25,1.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '18' at 0.5,1.0 left offset char -0.8,0
set object circle at 0.5,1.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set label '19' at 0.75,1.0 left offset char -0.8,0
set object circle at 0.75,1.0 fillcolor rgb '#0080808080' fillstyle solid noborder size 0.08
set arrow 1 from 0.0,0.08 to 0.0,0.16999999999999998 linewidth 1
set arrow 2 from 0.08,0.0 to 0.16999999999999998,0.0 linewidth 1
set arrow 3 from 0.33,0.0 to 0.42,0.0 linewidth 1
set arrow 4 from 0.25,0.08 to 0.25,0.16999999999999998 linewidth 1
set arrow 5 from 0.5,0.08 to 0.5,0.16999999999999998 linewidth 1
set arrow 6 from 0.58,0.0 to 0.92,0.0 linewidth 1
set arrow 7 from 0.9434314575050762,0.056568542494923796 to 0.8065685424949238,0.1934314575050762 linewidth 1
set arrow 8 from 0.0,0.33 to 0.0,0.42 linewidth 3
set arrow 9 from 0.08,0.25 to 0.16999999999999998,0.25 linewidth 3
set arrow 10 from 0.58,0.25 to 0.67,0.25 linewidth 1
set arrow 11 from 0.5,0.33 to 0.5,0.42 linewidth 1
set arrow 12 from 0.75,0.33 to 0.75,0.42 linewidth 1
set arrow 13 from 0.08,0.5 to 0.16999999999999998,0.5 linewidth 1
set arrow 14 from 0.0,0.58 to 0.0,0.67 linewidth 1
set arrow 15 from 0.25,0.58 to 0.25,0.67 linewidth 1
set arrow 16 from 0.33,0.5 to 0.42,0.5 linewidth 1
set arrow 17 from 0.58,0.5 to 0.67,0.5 linewidth 1
set arrow 18 from 0.75,0.58 to 0.75,0.67 linewidth 1
set arrow 19 from 0.08,0.75 to 0.16999999999999998,0.75 linewidth 1
set arrow 20 from 0.0,0.83 to 0.0,0.92 linewidth 1
set arrow 21 from 0.25,0.83 to 0.25,0.92 linewidth 1
set arrow 22 from 0.75,0.83 to 0.75,0.92 linewidth 1
set arrow 23 from 0.08,1.0 to 0.16999999999999998,1.0 linewidth 1
set arrow 24 from 0.33,1.0 to 0.42,1.0 linewidth 1
set arrow 25 from 0.58,1.0 to 0.67,1.0 linewidth 1
set style fill transparent solid 0.5 noborder
plot [-0.1:1.1][-0.1:1.1] NaN t''
