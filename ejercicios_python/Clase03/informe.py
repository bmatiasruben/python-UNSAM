# -----------------------------------------------------------------
# Ejercicio 3.9
# -----------------------------------------------------------------

import csv

def costoCamion(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costoTotal = 0
    for index, line in enumerate(rows):
        record = dict(zip(headers, line))
        try:
            nCajones = int(record['cajones'])
            precio = float(record['precio'])
            costoTotal += nCajones*precio
        except ValueError:
            print(f'Fila {index + 2}: No pude interpretar: {line}')

    f.close()
    return(costoTotal)

print(costoCamion('../Data/fecha_camion.csv'))