from pprint import pprint
import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion=[]
    lote={}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote['nombre']=row[0]
            lote['cajones']=int(row[1])
            lote['precio']=float(row[2])
            camion.append(lote)
            lote={}
    return camion


def leer_precios(nombre_archivo):
    'Arma un diccionario con la lista de precios'
    lista_de_precios={}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)
            lista_de_precios[row[0]]=float(row[1])
    
    return lista_de_precios


def balance(archivo_camion,archivo_precio):
    'Calcula el balance -las ventas, según la lista de precios, menos el costo del camion'
    camion=leer_camion(archivo_camion)
    costo=0
    for item in camion:
        costo+=item['cajones']*item['precio']

    p=leer_precios(archivo_precio)
    ventas=0

    for item in camion:
        ventas+=p[item['nombre']]*item['cajones']
     
    return (round(costo,2),round(ventas,2))

    
costo,ventas= balance('../Data/camion.csv','../Data/precios.csv')
ganancia= round(ventas-costo,2)
print(f'El costo fue: {costo}. Las ventas fueron: {ventas}. El balance: {ganancia}')