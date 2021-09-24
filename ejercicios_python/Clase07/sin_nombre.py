# -----------------------------------------------------------------
# Ejercicio 7.1
# -----------------------------------------------------------------

# import csv

# def parse_csv(nombre_archivo, has_headers = True, select = None, types = None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         registros = []
#         if not has_headers and select:
#             raise RuntimeError("Para seleccionar, necesito encabezados.")

#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(nombre_columna) for nombre_columna in select]
#                 headers = select
#             else:
#                 indices = []       
#             for row in rows:
#                 if not row:    # Saltea filas sin datos
#                     continue
#                 if indices:
#                     row = [row[index] for index in indices]
#                 if types: 
#                     row = [func(val) for func, val in zip(types, row)]
#                 registro = dict(zip(headers, row))
#                 registros.append(registro)
#         else:
#             for row in rows:
#                 if not row:    # Saltea filas sin datos
#                     continue            
#                 if types: 
#                     row = [func(val) for func, val in zip(types, row)]
#                 registros.append(tuple(row))
#     return registros

# -----------------------------------------------------------------
# Ejercicio 7.2
# -----------------------------------------------------------------

# import csv

# def parse_csv(nombre_archivo, has_headers = True, select = None, types = None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         registros = []
#         if not has_headers and select:
#             raise RuntimeError("Para seleccionar, necesito encabezados.")

#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(nombre_columna) for nombre_columna in select]
#                 headers = select
#             else:
#                 indices = []       
#             for i, row in enumerate(rows):
#                 if not row:    # Saltea filas sin datos
#                     continue
#                 if indices:
#                     row = [row[index] for index in indices]
#                 if types: 
#                     try:
#                         row = [func(val) for func, val in zip(types, row)]
#                     except Exception as e:
#                         print(f'Fila {i + 1}: No pude convertir {row}')
#                         print(f'Fila {i + 1}: Motivo {e}')
#                 registro = dict(zip(headers, row))
#                 registros.append(registro)
#         else:
#             for i, row in enumerate(rows):
#                 if not row:    # Saltea filas sin datos
#                     continue            
#                 if types:
#                     try: 
#                         row = [func(val) for func, val in zip(types, row)]
#                     except Exception as e:
#                         print(f'Fila {i}: No pude convertir {row}')
#                         print(f'Fila {i}: Motivo {e}')
#                 registros.append(tuple(row))
#     return registros

# -----------------------------------------------------------------
# Ejercicio 7.3
# -----------------------------------------------------------------

# import csv

# def parse_csv(nombre_archivo, has_headers = True, select = None, types = None, silence_errors = False):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         registros = []
#         if not has_headers and select:
#             raise RuntimeError("Para seleccionar, necesito encabezados.")

#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(nombre_columna) for nombre_columna in select]
#                 headers = select
#             else:
#                 indices = []       
#             for i, row in enumerate(rows):
#                 if not row:    # Saltea filas sin datos
#                     continue
#                 if indices:
#                     row = [row[index] for index in indices]
#                 if types: 
#                     try:
#                         row = [func(val) for func, val in zip(types, row)]
#                     except Exception as e:
#                         if not silence_errors:
#                             print(f'Fila {i + 1}: No pude convertir {row}')
#                             print(f'Fila {i + 1}: Motivo {e}')
#                 registro = dict(zip(headers, row))
#                 registros.append(registro)
#         else:
#             for i, row in enumerate(rows):
#                 if not row:    # Saltea filas sin datos
#                     continue            
#                 if types:
#                     try: 
#                         row = [func(val) for func, val in zip(types, row)]
#                     except Exception as e:
#                         if not silence_errors:
#                             print(f'Fila {i}: No pude convertir {row}')
#                             print(f'Fila {i}: Motivo {e}')
#                 registros.append(tuple(row))
#     return registros

# -----------------------------------------------------------------
# Ejercicio 7.4
# -----------------------------------------------------------------

# import fileparse
# import sys

# # Funcion para leer los datos del archivo camion.csv
# def leer_camion(archivo):
#     '''
#     Lee un archivo y devuelve una lista de diccionarios con sus entradas.
#     '''
#     camion = fileparse.parse_csv(archivo, types = [str, int, float])
#     return(camion)

# # Funcion para leer los datos del archivo precios.csv
# def leer_precios(archivo):
#     '''
#     Lee un archivo y devuelve un diccionario de precios por producto.
#     '''
#     precios = fileparse.parse_csv(archivo, types = [str, float], has_headers = False)    
#     return dict(precios)    

# def hacer_informe(camion,precios):
#     '''
#     Lee dos listas (una de diccionarios y otra de tuplas) y crea un informe de balance en forma de lista de tuplas. 
#     El primer argumento tiene el formato [{nombre: '', precio: '', cantidad: ''},...] y el segundo el formato [(nombre, precio),...]
#     La salida viene en formato [(nombre, cant_de_ventas, precio_de_venta, ganancia/perdida),...]
#     '''
#     table = []
#     for row in camion:
#         producto = row['nombre']
#         cambio = precios[producto] - row['precio']
#         list = (producto, row['cajones'], row['precio'], cambio)
#         table.append(list)
#     return table

# def imprimir_informe(informe):
#     '''
#     Lee una lista de tuplas que contenga información de un informe de balance y lo imprime con formato.
#     '''
#     headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

#     print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
#     print(('-' * 10 + ' ') * 4)

#     for nombre, cajones, precio, cambio in informe:
#         print(f'{nombre:>10s} {cajones:>10d} {"$" + str(precio):>10s} {cambio:>10.2f}')

# def informe_camion(archivo_camion = '../Data/camion.csv', archivo_precios = '../Data/precios.csv'):
#     datosCompra = leer_camion(archivo_camion)
#     datosVenta = leer_precios(archivo_precios)
#     informe = hacer_informe(datosCompra,datosVenta)
#     imprimir_informe(informe)

# def f_principal(argumentos):
#     informe_camion(argumentos[1], argumentos[2])

# -----------------------------------------------------------------
# Ejercicio 7.8
# -----------------------------------------------------------------

# def sumar_enteros1(desde, hasta):
#     '''Calcula la sumatoria de los números entre desde y hasta.
#        Si hasta < desde, entonces devuelve cero.

#     Pre: desde y hasta son números enteros
#     Pos: Se devuelve el valor de sumar todos los números del intervalo
#         [desde, hasta]. Si el intervalo es vacío se devuelve 0
#     '''
#     x = hasta
#     for i in range(desde, hasta):
#         x += i
    
#     return x

# def suma_triangular(N):
#     return N * (N + 1) / 2

# def sumar_enteros2(desde, hasta):
#     '''Calcula la sumatoria de los números entre desde y hasta.
#        Si hasta < desde, entonces devuelve cero.

#     Pre: desde y hasta son números enteros
#     Pos: Se devuelve el valor de sumar todos los números del intervalo
#         [desde, hasta]. Si el intervalo es vacío se devuelve 0
#     '''
#     return suma_triangular(hasta) - suma_triangular(desde - 1)

# -----------------------------------------------------------------
# Ejercicio 7.11
# -----------------------------------------------------------------

# import matplotlib.pyplot as plt

# fig = plt.figure()
# plt.subplot(2, 1, 1) # define la figura de arriba
# plt.plot([0,1,2],[0,1,0]) # dibuja la curva
# plt.xticks([]), plt.yticks([]) # saca las marcas

# plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
# plt.plot([0,1],[0,1])
# plt.xticks([]), plt.yticks([])

# plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
# plt.plot([0,1],[1,1])
# plt.xticks([]), plt.yticks([])

# plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
# plt.plot([0,1],[1,0])
# plt.xticks([]), plt.yticks([])

# plt.show()