# -----------------------------------------------------------------
# Ejercicio 4.1
# -----------------------------------------------------------------

# def invertir_lista(lista):
#     '''Recibe una lista L y la develve invertida.'''
#     invertida = []
#     i = len(lista)
#     while i > 0:    # tomo el último elemento 
#         i = i-1
#         invertida.append(lista[i])  # lista.pop(i) ---> lista[i] porque pop saca el elemento de la lista.
#     return invertida

# l = [1, 2, 3, 4, 5]    
# m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')

# -----------------------------------------------------------------
# Ejercicio 4.2
# -----------------------------------------------------------------

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion = []
#     registro = {}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)

# -----------------------------------------------------------------
# Ejercicio 4.3
# -----------------------------------------------------------------

# def buscar_u_elemento(lista, valor):
#     pos = -1
#     for index, numero in enumerate(lista):
#         if numero == valor:
#             pos = index
#     return pos    
    
# def buscar_n_elemento(lista, valor):
#     apariciones = 0
#     for numero in lista:
#         if numero == valor:
#             apariciones += 1
#     return apariciones   

# -----------------------------------------------------------------
# Ejercicio 4.6 extra
# -----------------------------------------------------------------

# def propagar(lista):
#     largo = len(lista)
#     if largo == 2:
#         if lista == [0,1] or lista == [1,0]:
#             lista = [1,1]
#             return lista
#     else:
#         mitad = largo // 2

#         lista1 = lista[:mitad]
#         lista2 = lista[mitad:]
#         if [lista1[-1],lista2[0]] == [0,1] or [lista1[-1],lista2[0]] == [1,0]:
#             lista1[-1] = 1
#             lista2[0] = 1

#         lista1 = propagar(lista1)
#         lista2 = propagar(lista2)

#         if [lista1[-1],lista2[0]] == [0,1] or [lista1[-1],lista2[0]] == [1,0]:
#             lista1[-1] = 1
#             lista2[0] = 1
        
#     return lista

# -----------------------------------------------------------------
# Ejercicio 4.7
# -----------------------------------------------------------------

# nums = [1,2,3,4]
# cuadrados = [x * x for x in nums]
# print(cuadrados)

# dobles = [2 * x for x in nums if x > 2]
# print(dobles)

# -----------------------------------------------------------------
# Ejercicio 4.8
# -----------------------------------------------------------------

# import csv

# def leer_camion(archivo):
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows) # El archivo contiene headers, salteo la primera fila
#     camion = []
#     for index, row in enumerate(rows):
#         try:
#             record = dict(zip(headers, (row[0], int(row[1]), float(row[2])))) # Creo un diccionario que tenga los headers como clave y los elementos de fila (con su respectivo tipo) como valores
#             camion.append(record) # se lo agrego a una lista
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        
#     f.close()
#     return(camion)

# # Funcion para leer los datos del archivo precios.csv
# def leer_precios(archivo):
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios  

# camion = leer_camion('../Data/camion.csv')
# precios = leer_precios('../Data/precios.csv')
# costo = sum([s['cajones'] * s['precio'] for s in camion])
# valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
# print(costo)
# print(valor)

# -----------------------------------------------------------------
# Ejercicio 4.9
# -----------------------------------------------------------------

# import csv

# def leer_camion(archivo):
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows) # El archivo contiene headers, salteo la primera fila
#     camion = []
#     for index, row in enumerate(rows):
#         try:
#             record = dict(zip(headers, (row[0], int(row[1]), float(row[2])))) # Creo un diccionario que tenga los headers como clave y los elementos de fila (con su respectivo tipo) como valores
#             camion.append(record) # se lo agrego a una lista
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        
#     f.close()
#     return(camion)

# # Funcion para leer los datos del archivo precios.csv
# def leer_precios(archivo):
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios  

# camion = leer_camion('../Data/camion.csv')
# precios = leer_precios('../Data/precios.csv')

# mas100 = [s for s in camion if s['cajones'] > 100]
# myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
# costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
# print(mas100)
# print(myn)
# print(costo10k)

# -----------------------------------------------------------------
# Ejercicio 4.10
# -----------------------------------------------------------------

# import csv

# def leer_camion(archivo):
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows) # El archivo contiene headers, salteo la primera fila
#     camion = []
#     for index, row in enumerate(rows):
#         try:
#             record = dict(zip(headers, (row[0], int(row[1]), float(row[2])))) # Creo un diccionario que tenga los headers como clave y los elementos de fila (con su respectivo tipo) como valores
#             camion.append(record) # se lo agrego a una lista
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        
#     f.close()
#     return(camion)

# camion = leer_camion('../Data/camion.csv')

# nombre_cajones =[(s['nombre'], s['cajones']) for s in camion]
# print(nombre_cajones)
# nombres = {s['nombre'] for s in camion}
# print(nombres)
# stock = {nombre: 0 for nombre in nombres}
# print(stock)

# for s in camion:
#     stock[s['nombre']] += s['cajones']
# print(stock)


# -----------------------------------------------------------------
# Ejercicio 4.11
# -----------------------------------------------------------------

# import csv

# f = open('../Data/fecha_camion.csv')
# rows = csv.reader(f)
# headers = next(rows)
# select = ['nombre', 'cajones', 'precio']
# indices = [headers.index(columna) for columna in select]
# # row = next(rows)
# # record = {columna : row[index] for columna, index in zip(select, indices)} 
# camion = [{columna : row[index] for columna, index in zip(select, indices)} for row in rows]

# -----------------------------------------------------------------
# Ejercicio 4.12
# -----------------------------------------------------------------

# import csv
# f = open('../Data/camion.csv')
# rows = csv.reader(f)
# headers = next(rows)

# types = [str, int, float]

# converted = [[func(val) for func,val in zip(types, row)] for row in rows]

# -----------------------------------------------------------------
# Ejercicio 4.13
# -----------------------------------------------------------------

# import csv
# f = open('../Data/camion.csv')
# rows = csv.reader(f)
# headers = next(rows)
# types = [str, int, float]

# datos = [{nombre:func(val) for nombre, func, val in zip(headers, types, row)} for row in rows]

# -----------------------------------------------------------------
# Ejercicio 4.14
# -----------------------------------------------------------------

# import csv
# f = open('../Data/dowstocks.csv')
# rows = csv.reader(f)
# headers = next(rows)
# types = [str, float, str, str, float, float, float, float, int]

# datos = [{nombre:func(val) for nombre, func, val in zip(headers, types, row)} for row in rows]

# -----------------------------------------------------------------
# Ejercicio 4.15
# -----------------------------------------------------------------

# import csv

# def leer_arboles(archivo):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
#     arboleda = [{nombre:func(valor) for nombre, func, valor in zip(headers, types, row)} for row in rows]
#     return arboleda

# -----------------------------------------------------------------
# Ejercicio 4.16
# -----------------------------------------------------------------

# import csv

# def leer_arboles(archivo):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
#     arboleda = [{nombre:func(valor) for nombre, func, valor in zip(headers, types, row)} for row in rows]
#     return arboleda

# arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
# alturas = [arbol['altura_tot'] for arbol in arboleda]
# alturas_jacaranda = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# -----------------------------------------------------------------
# Ejercicio 4.17
# -----------------------------------------------------------------

import csv

def leer_arboles(archivo):
    f = open(archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
    arboleda = [{nombre:func(valor) for nombre, func, valor in zip(headers, types, row)} for row in rows]
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
datos_jacaranda = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(datos_jacaranda)