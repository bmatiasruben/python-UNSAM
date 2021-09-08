# -----------------------------------------------------------------
# Ejercicio 5.15
# -----------------------------------------------------------------
import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(album):
    return 0 in album

def comprar_figu(figus_total):
    return random.randint(0,figus_total - 1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figuritas = 0
    while album_incompleto(album):
        album[comprar_figu(figus_total)] += 1
        figuritas += 1
    return figuritas

def main_5_14():
    resultados = [cuantas_figus(6) for i in range(1000)]
    print(f'Se necesitan en promedio {np.mean(resultados)} figuritas para llenar un album de 6 figuritas')

def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(resultados)