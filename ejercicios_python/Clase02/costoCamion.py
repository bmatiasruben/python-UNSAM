# -----------------------------------------------------------------
# Ejercicio 2.9
# -----------------------------------------------------------------

import csv

def costoCamion(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costoTotal = 0
    for index, row in enumerate(rows):
        try:
            costoTotal += int(row[1])*float(row[2])
        except ValueError:
            print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.')
        
    f.close()
    return(costoTotal)

costo = costoCamion('../Data/camion.csv')
print('Costo total:', costo)

