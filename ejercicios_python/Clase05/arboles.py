# -----------------------------------------------------------------
# Ejercicio 5.26
# -----------------------------------------------------------------

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

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

def main_5_25():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    alturas_jacaranda = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(alturas_jacaranda, bins = 100)
    plt.show()

def main17():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    datos_jacaranda = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    return datos_jacaranda

def scatter_hd(lista_de_pares):
    lista_aux = np.array(lista_de_pares)
    plt.scatter(lista_aux[:,1], lista_aux[:,0], s = 10, alpha=0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
    
def main_5_27():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    for index, i in enumerate(especies):
        array_aux = np.array(medidas[i])
        plt.figure(index)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title(f'Relación diámetro-alto para el {i}')       
        plt.xlim(0,100) 
        plt.ylim(0,30) 
        plt.scatter(array_aux[:,1], array_aux[:,0], alpha=0.3)
    plt.show()


