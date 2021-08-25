# -----------------------------------------------------------------
# Ejercicio 3.16
# -----------------------------------------------------------------

import csv

# Funcion para leer los datos del archivo camion.csv
def leerCamion(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows) # El archivo contiene headers, salteo la primera fila
    camion = []
    for index, row in enumerate(rows):
        try:
            record = dict(zip(headers, (row[0], int(row[1]), float(row[2])))) # Creo un diccionario que tenga los headers como clave y los elementos de fila (con su respectivo tipo) como valores
            camion.append(record) # se lo agrego a una lista
        except ValueError:
            print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        
    f.close()
    return(camion)

# Funcion para leer los datos del archivo precios.csv
def leerPrecios(archivo):
    precios = {}
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    for index, row in enumerate(rows):
        try:
            precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
        except IndexError:
            print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
    return precios    

datosCompra = leerCamion('../Data/camion.csv')
datosVenta = leerPrecios('../Data/precios.csv')

def hacerInforme(camion,precios):
    table = []
    for row in camion:
        producto = row['nombre']
        cambio = precios[producto] - row['precio']
        list = (producto, row['cajones'], row['precio'], cambio)
        table.append(list)
    return table

informe = hacerInforme(datosCompra,datosVenta)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-' * 10 + ' ') * 4)

for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$" + str(precio):>10s} {cambio:>10.2f}')
