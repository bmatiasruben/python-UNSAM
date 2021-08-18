import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costoCamion(nombre_archivo)
print('Costo total:', costo)