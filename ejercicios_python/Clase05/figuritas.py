# -----------------------------------------------------------------
# Ejercicio 5.19
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

def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0,figus_total - 1) for i in range(figus_paquete)]

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        paquetes += 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i] += 1
    return paquetes 
    
def main_5_19():
    paquetes = [cuantos_paquetes(670, 5) for i in range(100)]
    print(f'Se necesitan en promedio {np.mean(paquetes)} paquetes para llenar el album')
