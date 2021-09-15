# -----------------------------------------------------------------
# Ejercicio 6.1
# -----------------------------------------------------------------
# def propagar_al_vecino(l):
#     modif = False
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1]==0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i>0 and l[i-1]==0:
#             l[i-1] = 1
#             modif = True
#     return modif

# def propagar(l):
#     m = l.copy()
#     veces=0
#     while propagar_al_vecino(l):
#         veces += 1

#     print(f"Repetí {veces} veces la función propagar_al_vecino.")
#     print(f"Con input {m}")    
#     print(f"Y obtuve  {l}")
#     return m

# En el peor caso hace n-1 iteraciones sobre una cadena de n elementos, el peor caso siendo [0,0,0,...,0,1]

# 1. Primero revisa el i<n-1 e i>0, entonces no entra a la tercera condicion
# 2. Porque el for funciona de izq a der. Propagar a derecha es más facil que propagar a izquierda.
# 3a. Already did that
# 3b. Realiza 6n-4 operaciones (6 comparaciones por elemento, excepto por los de las esquinas que hacen solo 4 c/u)
# 3c. Como máximo n(6n-4) operaciones. Complejidad cuadratica.

# -----------------------------------------------------------------
# Ejercicio 6.2
# -----------------------------------------------------------------
# def propagar_a_derecha(l):
#     n = len(l)
#     l2 = l.copy()
#     for i,e in enumerate(l2):
#         if e==1 and i<n-1:
#             if l2[i+1]==0:
#                 l2[i+1] = 1
#     return l2
# #%
# def propagar_a_izquierda(l):
#     return propagar_a_derecha(l[::-1])[::-1]
# #%
# def propagar(l):
#     ld=propagar_a_derecha(l)
#     lp=propagar_a_izquierda(ld)
#     return lp

# 1. Se usó la misma variable. Easy
# 2. Vaya uno a saber, no me parece muy importante
# 3. Lesto
# 4. Hace como máximo 3n operaciones
# 5. Hace como máximo (2*k + 3)*n, es lineal (primero se hace una y despues la otra, se suman las complejidades.)

# -----------------------------------------------------------------
# Ejercicio 6.3
# -----------------------------------------------------------------
# def trad2s(l):
#     '''traduce una lista con 1,0 y -1 
#     a una cadena con 'f', 'o' y 'x' '''
#     d={1:'f', 0 :'o', -1:'x'}
#     s=''.join([d[c] for c in l])
#     return s

# def trad2l(ps):
#     '''traduce cadena con 'f', 'o' y 'x'
#     a una lista con 1,0 y -1'''
#     inv_d={'f':1, 'o':0, 'x':-1}
#     l = [inv_d[c] for c in ps]
#     return l

# def propagar(l, debug = True):
#     s = trad2s(l)
#     if debug:
#         print(s)#, end = ' -> ')
#     W=s.split('x')
#     PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
#     ps='x'.join(PW)
#     if debug:
#         print(ps)
#     return trad2l(ps)

# l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
# lp = propagar(l)
# print("Estado original:  ",l)
# print("Estado propagado: ",lp)

# 1. La lista se acorta porque no se le agregan los -1
# 2. Lesto
# 3. La transformación a caractér lleva n pasos. La separación lleva otros n. Creo que es lineal. Porque PW es una operacion lineal también

# -----------------------------------------------------------------
# Ejercicio 6.4
# -----------------------------------------------------------------

# import csv

# # Funcion para leer los datos del archivo camion.csv
# def leerCamion(archivo):
#     '''
#     Lee un archivo y devuelve una lista de diccionarios con sus entradas.
#     '''
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
#     '''
#     Lee un archivo y devuelve un diccionario de precios por producto.
#     '''    
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios    

# def hacerInforme(camion,precios):
#     '''
#     Lee dos listas de diccionarios y crea un informe de balance en forma de lista de tuplas. 
#     El primer argumento tiene el formato [{nombre: '', precio: '', cantidad: ''},...] y el segundo el formato [{nombre: '', precio: ''},...]
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

# datosCompra = leerCamion('../Data/camion.csv')
# datosVenta = leerPrecios('../Data/precios.csv')
# imprimir_informe(hacerInforme(datosCompra,datosVenta))

# -----------------------------------------------------------------
# Ejercicio 6.5
# -----------------------------------------------------------------

# import csv

# # Funcion para leer los datos del archivo camion.csv
# def leerCamion(archivo):
#     '''
#     Lee un archivo y devuelve una lista de diccionarios con sus entradas.
#     '''
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
#     '''
#     Lee un archivo y devuelve un diccionario de precios por producto.
#     '''    
#     precios = {}
#     f = open(archivo, 'rt')
#     rows = csv.reader(f)
#     for index, row in enumerate(rows):
#         try:
#             precios[row[0]] = float(row[1]) # Asigno los valores del diccionario
#         except IndexError:
#             print(f'Se ignoró la linea {index + 1} de {archivo} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 1 porque el index arranca en 0)
            
#     return precios    

# def hacerInforme(camion,precios):
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

# def informe_camion(archivo_camion, archivo_precios):
#     datosCompra = leerCamion(archivo_camion)
#     datosVenta = leerPrecios(archivo_precios)
#     informe = hacerInforme(datosCompra,datosVenta)
#     imprimir_informe(informe)


# -----------------------------------------------------------------
# Ejercicio 6.6
# -----------------------------------------------------------------
# import csv

# def parse_csv(nombre_archivo):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)

#         # Lee los encabezados
#         headers = next(rows)
#         registros = []
#         for row in rows:
#             if not row:    # Saltea filas sin datos
#                 continue
#             registro = dict(zip(headers, row))
#             registros.append(registro)

#     return registros

# -----------------------------------------------------------------
# Ejercicio 6.7
# -----------------------------------------------------------------

# import csv

# def parse_csv(nombre_archivo, select = None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(nombre_columna) for nombre_columna in select]
#             headers = select
#         else:
#             indices = []

#         registros = []
#         for row in rows:
#             if not row:    # Saltea filas sin datos
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
    
#             registro = dict(zip(headers, row))
#             registros.append(registro)

#     return registros

# -----------------------------------------------------------------
# Ejercicio 6.8
# -----------------------------------------------------------------

# import csv

# def parse_csv(nombre_archivo, select = None, types = None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(nombre_columna) for nombre_columna in select]
#             headers = select
#         else:
#             indices = []

#         registros = []
#         for row in rows:
#             if not row:    # Saltea filas sin datos
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
#             if types: 
#                 row = [func(val) for func, val in zip(types, row) ]
#             registro = dict(zip(headers, row))
#             registros.append(registro)

#     return registros