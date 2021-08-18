# -----------------------------------------------------------------
# Ejercicio 2.1
# -----------------------------------------------------------------

# with open('../Data/camion.csv', 'rt') as f:
#     for line in f:
#         print(line, end = '')

# --------------------------

# f = open('../Data/camion.csv', 'rt')
# headers = next(f).split(',')
# print(headers)
# for line in f:
#     row = line.split(',')
#     print(row)

# f.close()

# -----------------------------------------------------------------
# Ejercicio 2.3
# -----------------------------------------------------------------

# f = open('../Data/precios.csv', 'rt')

# for line in f:
#     row = line.split(',')
#     if row[0] == 'Naranja':
#         print('El precio de la naranja es', row[1])

# f.close()

# -----------------------------------------------------------------
# Ejercicio 2.4
# -----------------------------------------------------------------

# import gzip

# with gzip.open('../Data/camion.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end = '')

# -----------------------------------------------------------------
# Ejercicio 2.5
# -----------------------------------------------------------------

# def saludar(nombre):
#     'Saluda a alguien'
#     print('Hola', nombre)

# nombre = input('Ingrese el nombre de a quien desea saludar: ')
# saludar(nombre)

# -----------------------------------------------------------------
# Ejercicio 2.7
# -----------------------------------------------------------------

# def buscarPrecio(fruta):
#     f = open('../Data/precios.csv', 'rt')

#     for line in f:
#         row = line.split(',')
#         if row[0].lower() == fruta.lower():
#             return row[1]
#             f.close()

#     return False    
    
# fruta = input('Ingrese la fruta a buscar el precio: ')

# precio = buscarPrecio(fruta)

# if precio == False:
#     print(f'{fruta} no figura en el listado de precios')
# else:
#     print(f'El precio de un cajón de {fruta} es: {precio}')

# -----------------------------------------------------------------
# Ejercicio 2.8a
# -----------------------------------------------------------------

# def preguntarEdad(nombre):
#     edad = int(input(f'ingresá tu edad {nombre}: '))
#     if edad<0:
#         raise ValueError('La edad no puede ser negativa.')
#     return edad

# for nombre in ['Pedro','Juan','Caballero']:
#     try:
#         edad = preguntarEdad(nombre)
#         print(f'{nombre} tiene {edad} años.')
#     except ValueError:
#         print(f'{nombre} no ingresó una edad válida.')

# -----------------------------------------------------------------
# Ejercicio 2.11
# -----------------------------------------------------------------

# import csv

# f = open('../Data/camion.csv', 'rt')
# rows = csv.reader(f)
# next(rows)
# row = next(rows)


# t = (row[0], int(row[1]), float(row[2]))
# print(t)

# nombre, cajones, precio = t
# print(nombre, cajones, precio)

# t = (nombre, 2*cajones, precio)
# print(t)

# -----------------------------------------------------------------
# Ejercicio 2.12
# -----------------------------------------------------------------

# import csv

# f = open('../Data/camion.csv', 'rt')
# rows = csv.reader(f)
# next(rows)
# row = next(rows)

# d = {
#     'nombre' : row[0], 
#     'cajones' : int(row[1]), 
#     'precio' : float(row[2])
# } 
# print(d)

# print(d['cajones'] * d['precio'])

# d['fecha'] = (14, 8, 2020)
# d['cuenta'] = 12345

# print(d)

# -----------------------------------------------------------------
# Ejercicio 2.13
# -----------------------------------------------------------------

# import csv

# f = open('../Data/camion.csv', 'rt')
# rows = csv.reader(f)
# next(rows)
# row = next(rows)

# d = {
#     'nombre' : row[0], 
#     'cajones' : int(row[1]), 
#     'precio' : float(row[2])
# } 

# d['fecha'] = (14, 8, 2020)
# d['cuenta'] = 12345

# for k in d:
#     print(k, '=', d[k])

# print(list(d))

# print(d.keys())

# -----------------------------------------------------------------
# Ejercicio 2.17
# -----------------------------------------------------------------

import csv

def leerPrecios():
    precios = {}
    f = open('../Data/precios.csv', 'rt')
    rows = csv.reader(f)
    for index, row in enumerate(rows):
        try:
            precios[row[0]] = float(row[1])
        except IndexError:
            print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.')
            
    return precios    
    
precios = leerPrecios()

fruta = input('Ingrese la fruta a buscar el precio: ')
try:
    print(f'El precio de un cajón de {fruta} es: {precios[fruta]}')
except KeyError:
    print(f'{fruta} no figura en el listado de precios')
