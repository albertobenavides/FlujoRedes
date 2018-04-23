from math import floor
with open("todos.csv", "w") as g:
    print('p,k,DistanciaPromedio,tDistancia,DensidadPromedio,tDensidad', file = g)
    for N in [8, 16, 32, 64, 128]:
        Ka = floor(N / 2) # Cantidad de vecinos laterales con los que se conectará cada nodo
        for k in range(1, Ka + 1):
            if k % 5 == 0:
                with open("N{0:03d}k{1:03d}.csv".format(N, k),"r") as f:
                    for line in f:
                        if line[0] != "p":
                            print(line, end = "", file = g)
