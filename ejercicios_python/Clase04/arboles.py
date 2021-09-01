# -----------------------------------------------------------------
# Ejercicio 4.18
# -----------------------------------------------------------------

import csv

def leer_arboles(archivo):
    f = open(archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
    arboleda = [{nombre:func(valor) for nombre, func, valor in zip(headers, types, row)} for row in rows]
    return arboleda

def medidas_de_especies(especies, arboleda):
    datos_especies = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return datos_especies

def main16():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    alturas_jacaranda = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    print(alturas_jacaranda)

def main17():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    datos_jacaranda = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    print(datos_jacaranda)

def main18():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies,arboleda)
    print([len(medidas[especie]) for especie in especies])


