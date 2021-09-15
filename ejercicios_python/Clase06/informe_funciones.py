# -----------------------------------------------------------------
# Ejercicio 6.11
# -----------------------------------------------------------------

import fileparse

# Funcion para leer los datos del archivo camion.csv
def leer_camion(archivo):
    '''
    Lee un archivo y devuelve una lista de diccionarios con sus entradas.
    '''
    camion = fileparse.parse_csv(archivo, types = [str, int, float])
    return(camion)

# Funcion para leer los datos del archivo precios.csv
def leer_precios(archivo):
    '''
    Lee un archivo y devuelve un diccionario de precios por producto.
    '''
    precios = fileparse.parse_csv(archivo, types = [str, float], has_headers = False)    
    return dict(precios)    

def hacer_informe(camion,precios):
    '''
    Lee dos listas (una de diccionarios y otra de tuplas) y crea un informe de balance en forma de lista de tuplas. 
    El primer argumento tiene el formato [{nombre: '', precio: '', cantidad: ''},...] y el segundo el formato [(nombre, precio),...]
    La salida viene en formato [(nombre, cant_de_ventas, precio_de_venta, ganancia/perdida),...]
    '''
    table = []
    for row in camion:
        producto = row['nombre']
        cambio = precios[producto] - row['precio']
        list = (producto, row['cajones'], row['precio'], cambio)
        table.append(list)
    return table

def imprimir_informe(informe):
    '''
    Lee una lista de tuplas que contenga información de un informe de balance y lo imprime con formato.
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * 4)

    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$" + str(precio):>10s} {cambio:>10.2f}')

def informe_camion(archivo_camion = '../Data/camion.csv', archivo_precios = '../Data/precios.csv'):
    datosCompra = leer_camion(archivo_camion)
    datosVenta = leer_precios(archivo_precios)
    informe = hacer_informe(datosCompra,datosVenta)
    imprimir_informe(informe)

