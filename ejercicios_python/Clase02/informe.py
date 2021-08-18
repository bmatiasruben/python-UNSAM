# -----------------------------------------------------------------
# Ejercicio 2.18
# -----------------------------------------------------------------

import csv

# Funcion para leer los datos del archivo camion.csv
def leerCamion():
    f = open('../Data/camion.csv', 'rt')
    rows = csv.reader(f)
    next(rows) # El archivo contiene headers, salteo la primera fila
    camion = []
    for index, row in enumerate(rows):
        try:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        except ValueError:
            print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        
    f.close()
    return(camion)

# Funcion para leer los datos del archivo precios.csv
def leerPrecios():
    precios = {}
    f = open('../Data/precios.csv', 'rt')
    rows = csv.reader(f)
    for index, row in enumerate(rows):
        try:
            precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
        except IndexError:
            print(f'ERROR. Se ignoró la linea {index + 1} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
    return precios    

datosCompra = leerCamion()
datosVenta = leerPrecios()

costoTotal = 0
recaudado = 0

for fruta, cajones, precioCompra in datosCompra:
    costoTotal +=  precioCompra * cajones
    recaudado += datosVenta[fruta] * cajones

if recaudado < costoTotal:
    resultado = 'perdida'
    neto = costoTotal - recaudado
else:
    resultado = 'ganancia'
    neto = recaudado - costoTotal

print(f'El camión costó ${costoTotal} y recaudó ${recaudado}, obteniendo una {resultado} de ${neto}')
