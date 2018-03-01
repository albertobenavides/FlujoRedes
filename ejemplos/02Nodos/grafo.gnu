set terminal png truecolor
set output 'grafo.png'
set key off
set size square
unset colorbox
set title'Ejemplo 2. Nodos'
set object circle at 0,0 fillcolor rgb '#00ff0000' fillstyle solid noborder size 0.2
set label '0' at 0.04434487183641955,0.6831201254439461 left offset char -0.4,0
set object circle at 0.04434487183641955,0.6831201254439461 fillcolor rgb '#8037fad1' fillstyle solid noborder size 0.08222761018434688
set label '1' at 0.47285126653020826,0.4341051933027821 left offset char -0.4,0
set object circle at 0.47285126653020826,0.4341051933027821 fillcolor rgb '#804c601a' fillstyle solid noborder size 0.05631162315331625
set label '2' at 0.1482194121473348,0.89690817356655 left offset char -0.4,0
set object circle at 0.1482194121473348,0.89690817356655 fillcolor rgb '#8081ca77' fillstyle solid noborder size 0.09326506070128524
set label '3' at 0.22494615035012533,0.05751855025998098 left offset char -0.4,0
set object circle at 0.22494615035012533,0.05751855025998098 fillcolor rgb '#809bb5c0' fillstyle solid noborder size 0.07504215370859879
set label '4' at 0.8146326115246402,0.3100853598327581 left offset char -0.4,0
set object circle at 0.8146326115246402,0.3100853598327581 fillcolor rgb '#8090d758' fillstyle solid noborder size 0.08366263775005478
set label '5' at 0.5530646967742143,0.40176280521366725 left offset char -0.4,0
set object circle at 0.5530646967742143,0.40176280521366725 fillcolor rgb '#80bccb6e' fillstyle solid noborder size 0.07109185193874618
set label '6' at 0.09599168495000232,0.448862994234428 left offset char -0.4,0
set object circle at 0.09599168495000232,0.448862994234428 fillcolor rgb '#80cfe46a' fillstyle solid noborder size 0.060385620841781396
set label '7' at 0.5934840492425532,0.335976808816009 left offset char -0.4,0
set object circle at 0.5934840492425532,0.335976808816009 fillcolor rgb '#80ec8a0b' fillstyle solid noborder size 0.05281968042982893
set label '8' at 0.14933650873956061,0.4019158812685747 left offset char -0.4,0
set object circle at 0.14933650873956061,0.4019158812685747 fillcolor rgb '#80ffa4d0' fillstyle solid noborder size 0.05885409894550417
set label '9' at 0.7568442580582917,0.16275526085284076 left offset char -0.4,0
set object circle at 0.7568442580582917,0.16275526085284076 fillcolor rgb '#80a4d208' fillstyle solid noborder size 0.09971425733517436
set label '10' at 0.6692405164400214,0.36869848112600745 left offset char -0.8,0
set object circle at 0.6692405164400214,0.36869848112600745 fillcolor rgb '#80e6b646' fillstyle solid noborder size 0.056333277111250045
set label '11' at 0.3269788980129005,0.3056869532661567 left offset char -0.8,0
set object circle at 0.3269788980129005,0.3056869532661567 fillcolor rgb '#803336b0' fillstyle solid noborder size 0.06645340172394504
set label '12' at 0.6501503912686073,0.2925074112287218 left offset char -0.8,0
set object circle at 0.6501503912686073,0.2925074112287218 fillcolor rgb '#80655ec5' fillstyle solid noborder size 0.05910330699484292
set label '13' at 0.7719827651192831,0.1982542112599205 left offset char -0.8,0
set object circle at 0.7719827651192831,0.1982542112599205 fillcolor rgb '#805a8d28' fillstyle solid noborder size 0.08198930700097631
set label '14' at 0.15446353780565658,0.31199688535298553 left offset char -0.8,0
set object circle at 0.15446353780565658,0.31199688535298553 fillcolor rgb '#80f6fb84' fillstyle solid noborder size 0.09648200761546358
set label '15' at 0.667657621049259,0.9574915089315037 left offset char -0.8,0
set object circle at 0.667657621049259,0.9574915089315037 fillcolor rgb '#805b5b7e' fillstyle solid noborder size 0.08644587019287339
set label '16' at 0.9749932165418942,0.7958207809013494 left offset char -0.8,0
set object circle at 0.9749932165418942,0.7958207809013494 fillcolor rgb '#8080547d' fillstyle solid noborder size 0.0680876575229639
set label '17' at 0.7622762748446629,0.780328468224246 left offset char -0.8,0
set object circle at 0.7622762748446629,0.780328468224246 fillcolor rgb '#802c3bf8' fillstyle solid noborder size 0.09136496723039036
set label '18' at 0.15776514323687396,0.7237678886004458 left offset char -0.8,0
set object circle at 0.15776514323687396,0.7237678886004458 fillcolor rgb '#808f1b83' fillstyle solid noborder size 0.06551004469631558
set label '19' at 0.5827584429414039,0.3965529808198551 left offset char -0.8,0
set object circle at 0.5827584429414039,0.3965529808198551 fillcolor rgb '#80e552ba' fillstyle solid noborder size 0.07509639808079059
set style fill transparent solid 0.5 noborder
plot [-0.1:1.1][-0.1:1.1] NaN t''
quit
