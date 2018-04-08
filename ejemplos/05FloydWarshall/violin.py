import csv

with open('tiempos.txt', 'r') as f:
    tiempo = csv.reader(f)

    ordenada = sorted(tiempo, key=lambda row: row[0])

    for row in ordenada:
        print(row)
