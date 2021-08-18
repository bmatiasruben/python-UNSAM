# -----------------------------------------------------------------
# Ejercicio 2.2
# -----------------------------------------------------------------

# f = open('../Data/camion.csv', 'rt') # abro el archivo
# headers = next(f).split(',') # Leo la primera linea del archivo (contiene los headers)
# costoTotal = 0 # Inicializo el costo total en 0

# for line in f:
#     row = line.split(',')
#     costoTotal += int(row[1])*float(row[2])
# f.close()

# print('Costo total', costoTotal)

# -----------------------------------------------------------------
# Ejercicio 2.6
# -----------------------------------------------------------------

# def costoCamion(archivo):
#     f = open(archivo, 'rt')
#     headers = next(f)
#     costoTotal = 0
#     for line in f:
#         row = line.split(',')
#         costoTotal += int(row[1])*float(row[2])
#     f.close()
#     return(costoTotal)

# costo = costoCamion('../Data/camion.csv')
# print('Costo total:', costo)

# -----------------------------------------------------------------
# Ejercicio 2.8b
# -----------------------------------------------------------------

# def costoCamion(archivo):
#     f = open(archivo, 'rt')
#     headers = next(f)
#     costoTotal = 0
#     for index, line in enumerate(f):
#         try:
#             row = line.split(',')
#             costoTotal += int(row[1])*float(row[2])
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.')
        
#     f.close()
#     return(costoTotal)

# costo = costoCamion('../Data/missing.csv')
# print('Costo total:', costo)

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

