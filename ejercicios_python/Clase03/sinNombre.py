# -----------------------------------------------------------------
# Ejercicio 3.6
# -----------------------------------------------------------------

# for n in range(10): 
#     print(n, end=' ')

# for n in range(10,0,-1):
#     print(n, end=' ')

# for n in range(0,10,2): 
#     print(n, end=' ')

# -----------------------------------------------------------------
# Ejercicio 3.7
# -----------------------------------------------------------------

# data = [4, 9, 1, 25, 16, 100, 49]
# print(min(data), max(data), sum(data))

# for n, x in enumerate(data):
#     print(n, x)

# -----------------------------------------------------------------
# Ejercicio 3.8
# -----------------------------------------------------------------

# def costoCamion(archivo):
#     f = open(archivo, 'rt')
#     next(f)
#     costoTotal = 0
#     for index, line in enumerate(f):
#         try:
#             row = line.split(',')
#             costoTotal += int(row[1])*float(row[2])
#         except ValueError:
#             print(f'Fila {index + 2}: No pude interpretar: {row}')
        
#     f.close()
#     return(costoTotal)

# costo = costoCamion('../Data/missing.csv')
# print('Costo total:', costo)

# -----------------------------------------------------------------
# Ejercicio 3.9
# -----------------------------------------------------------------

# import csv

# def costoCamion(archivo):
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows)
#     costoTotal = 0
#     for index, line in enumerate(rows):
#         record = dict(zip(headers, line))
#         try:
#             nCajones = int(record['cajones'])
#             precio = float(record['precio'])
#             costoTotal += nCajones*precio
#         except ValueError:
#             print(f'Fila {index + 2}: No pude interpretar: {line}')

#     f.close()
#     return(costoTotal)

# print(costoCamion('../Data/fecha_camion.csv'))

# -----------------------------------------------------------------
# Ejercicio 3.10
# -----------------------------------------------------------------

# precios = {
#         'Pera' : 490.1,
#         'Lima' : 23.45,
#         'Naranja' : 91.1,
#         'Mandarina' : 34.23
#     }

# print(precios.items())

# listaPrecios = list(zip(precios.values(),precios.keys()))

# print(listaPrecios)

# -----------------------------------------------------------------
# Ejercicio 3.11
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerCamion(archivo):
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

# camion = leerCamion('../Data/camion.csv')
# camion2 = leerCamion('../Data/camion2.csv')
# tenencias = Counter()
# tenencias2 = Counter()

# for s in camion:
#     tenencias[s['nombre']] += s['cajones']

# for s in camion2:
#     tenencias2[s['nombre']] += s['cajones']

# combinada = tenencias + tenencias2

# print(combinada)

# -----------------------------------------------------------------
# Ejercicio 3.12
# -----------------------------------------------------------------

# value = 42863.1

# print(f'print(value): {value}')
# print(f'print(value:0.4f): {value:0.4f}')
# print(f'print(value:>16.2f): {value:>16.2f}')
# print(f'print(value:<16.2f): {value:<16.2f}')
# print(f'print(value:>16.2f): {value:*>16,.2f}')

# -----------------------------------------------------------------
# Ejercicio 3.13
# -----------------------------------------------------------------

# import csv

# # Funcion para leer los datos del archivo camion.csv
# def leerCamion(archivo):
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
# def leerPrecios(archivo):
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'ERROR. Se ignoró la linea {index + 1} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios    

# datosCompra = leerCamion('../Data/camion.csv')
# datosVenta = leerPrecios('../Data/precios.csv')

# def hacerInforme(camion,precios):
#     table = []
#     for row in camion:
#         producto = row['nombre']
#         cambio = precios[producto] - row['precio']
#         list = (producto, row['cajones'], row['precio'], cambio)
#         table.append(list)
#     return table


# print(hacerInforme(datosCompra, datosVenta))

# -----------------------------------------------------------------
# Ejercicio 3.14
# -----------------------------------------------------------------

# import csv

# # Funcion para leer los datos del archivo camion.csv
# def leerCamion(archivo):
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
# def leerPrecios(archivo):
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios    

# datosCompra = leerCamion('../Data/camion.csv')
# datosVenta = leerPrecios('../Data/precios.csv')

# def hacerInforme(camion,precios):
#     table = []
#     for row in camion:
#         producto = row['nombre']
#         cambio = precios[producto] - row['precio']
#         list = (producto, row['cajones'], row['precio'], cambio)
#         table.append(list)
#     return table

# informe = hacerInforme(datosCompra,datosVenta)

# # for r in informe:
# #     print('%10s %10d %10.2f %10.2f' % r)

# for nombre, cajones, precio, cambio in informe:
#     print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

# -----------------------------------------------------------------
# Ejercicio 3.15
# -----------------------------------------------------------------

# import csv

# # Funcion para leer los datos del archivo camion.csv
# def leerCamion(archivo):
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
# def leerPrecios(archivo):
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios    

# datosCompra = leerCamion('../Data/camion.csv')
# datosVenta = leerPrecios('../Data/precios.csv')

# def hacerInforme(camion,precios):
#     table = []
#     for row in camion:
#         producto = row['nombre']
#         cambio = precios[producto] - row['precio']
#         list = (producto, row['cajones'], row['precio'], cambio)
#         table.append(list)
#     return table

# informe = hacerInforme(datosCompra,datosVenta)

# headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

# print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
# print(('-' * 10 + ' ') * 4)

# for nombre, cajones, precio, cambio in informe:
#     print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

# -----------------------------------------------------------------
# Ejercicio 3.18
# -----------------------------------------------------------------

# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista')
#         exit
#     else:
#         return arbolesEnParque

# listaArboles = leerParque('../Data/arbolado-en-espacios-verdes.csv', 'general PAZ')

# -----------------------------------------------------------------
# Ejercicio 3.19
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def especies(listaArboles):
#     especiesList = []
#     for arbol in listaArboles:
#         especiesList.append(arbol['nombre_com'])
#     return set(especiesList)

# -----------------------------------------------------------------
# Ejercicio 3.19
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def especies(listaArboles):
#     especiesList = []
#     for arbol in listaArboles:
#         especiesList.append(arbol['nombre_com'])
#     return set(especiesList)

# print(especies(leerParque('../Data/arbolado-en-espacios-verdes.csv', 'general paz')))

# -----------------------------------------------------------------
# Ejercicio 3.20
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def contarEjemplares(listaArboles):
#     especiesDict = Counter()
#     for arbol in listaArboles:
#         especiesDict[arbol['nombre_com']] += 1
#     return especiesDict

# print('Parque General Paz:')
# print(contarEjemplares(leerParque('../Data/arbolado-en-espacios-verdes.csv', 'General Paz')).most_common(5))

# print('Parque Los Andes:')
# print(especies(leerParque('../Data/arbolado-en-espacios-verdes.csv', 'Andes, Los')).most_common(5))

# print('Parque Centenario:')
# print(especies(leerParque('../Data/arbolado-en-espacios-verdes.csv', 'Centenario')).most_common(5))

# # Obtuve
# # Parque General Paz:
# # [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
# # Parque Los Andes:
# # [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
# # Parque Centenario:
# # [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

# -----------------------------------------------------------------
# Ejercicio 3.21
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def obtenerAlturas(listaArboles, especie):
#     alturas = []
#     for arbol in listaArboles:
#         if arbol['nombre_com'].lower() == especie.lower():  
#             alturas.append(float(arbol['altura_tot']))
#     if alturas == []:
#         print(f'La especie no se encuentra en este parque: {parque}')
#         exit
#     else:
#         return alturas


# parques = ['General Paz', 'Andes, Los', 'Centenario']

# for parque in parques:
#     print(parque)
#     alturas = obtenerAlturas(leerParque('../Data/arbolado-en-espacios-verdes.csv', parque), 'Jacarandá')
#     print(f'Máx: {max(alturas):0.2f}')
#     print(f'Prom: {sum(alturas)/len(alturas):0.2f}')

# # Obtuve
# # General Paz
# # Máx: 16.00
# # Prom: 10.20
# # Andes, Los
# # Máx: 25.00
# # Prom: 10.54
# # Centenario
# # Máx: 18.00
# # Prom: 8.96

# -----------------------------------------------------------------
# Ejercicio 3.22
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def obtenerInclinaciones(listaArboles, especie):
#     inclinaciones = []
#     for arbol in listaArboles:
#         if arbol['nombre_com'].lower() == especie.lower():  
#             inclinaciones.append(float(arbol['inclinacio']))
#     if inclinaciones == []:
#         print(f'La especie no se encuentra en este parque: {parque}')
#         exit
#     else:
#         return inclinaciones

# -----------------------------------------------------------------
# Ejercicio 3.23
# -----------------------------------------------------------------

# from collections import Counter
# import csv

# def leerParque(archivo, parque):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     arbolesEnParque = []
#     for index, arboles in enumerate(rows):
#         try:
#             record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
#         except ValueError:
#             print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
#         if record['espacio_ve'].lower() == parque.lower():
#             arbolesEnParque.append(record)
#     if arbolesEnParque == []:
#         print('El parque solicitado no se encuentra en la lista.')
#         exit
#     else:
#         return arbolesEnParque

# def especies(listaArboles):
#     especiesList = []
#     for arbol in listaArboles:
#         especiesList.append(arbol['nombre_com'])
#     return set(especiesList)

# def obtenerInclinaciones(listaArboles, especie):
#     inclinaciones = []
#     for arbol in listaArboles:
#         if arbol['nombre_com'].lower() == especie.lower():  
#             inclinaciones.append(float(arbol['inclinacio']))
#     if inclinaciones == []:
#         print(f'La especie no se encuentra en este parque: {parque}')
#         exit
#     else:
#         return inclinaciones

# def especimenMasInclinado(listaArboles):
#     listaEspecies = especies(listaArboles)
#     dictInclinaciones = {}

#     for especie in listaEspecies:
#         dictInclinaciones[especie] = max(obtenerInclinaciones(listaArboles, especie))
#     # print(dictInclinaciones)
#     inclinacionMax = max(dictInclinaciones, key=dictInclinaciones.get)
#     return [inclinacionMax, dictInclinaciones[inclinacionMax]]

# parques = ['General Paz', 'Andes, Los', 'Centenario']

# for parque in parques:
#     print(parque)
#     inclinacionMax = especimenMasInclinado(leerParque('../Data/arbolado-en-espacios-verdes.csv', parque))
#     print(f'El {inclinacionMax[0]} es el arbol más inclinado del parque, con una inclinación de {inclinacionMax[1]:0.2f} grados')

