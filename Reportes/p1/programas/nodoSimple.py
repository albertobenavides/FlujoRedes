print("set terminal png size 600, 200")
print("set output 'img/carrera.png'") # https://stackoverflow.com/questions/13869439/gnuplot-how-to-increase-the-width-of-my-graph
print("unset key") # https://forums.manning.com/posts/list/21761.page
print("unset tics")
print("unset border")
print("unset colorbox")
print("set arrow 1 from 0,0 to 100,0 nohead")
print("set object circle at 0,0 fillstyle solid fillcolor 'blue'")
print("set object circle at 100,0 fillstyle solid fillcolor 'red'")
print("plot [-10:110][-0.1:0.1] NaN t''")
