# -----------------------------------------------------------------
# Ejercicio 5.1
# -----------------------------------------------------------------
# import random

# def tirar():
#     tirada = []
#     for i in range(5):
#         tirada.append(random.randint(1,6))

#     return tirada

# def es_generala(tirada):
#     valor = tirada[0]
#     for dado in tirada:
#         if dado != valor:
#             return False
#     return True

# N = 100000
# G = sum([es_generala(tirar()) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# -----------------------------------------------------------------
# Ejercicio 5.3
# -----------------------------------------------------------------
# import random
# from collections import Counter

# def cumpleaños(N):
#     cumples = []
#     for i in range(N):
#         cumples.append(random.randint(1,365))
#     return cumples

# def hay_iguales(cumples):
#     cumples_dic = Counter(cumples)
#     mismo_cumple = max(cumples_dic)
#     if mismo_cumple > 1:
#         return True
#     else:
#         return False

# def prob_mismo_cumple(N,gente):
#     prob = sum([hay_iguales(cumpleaños(gente)) for i in range(N)])
#     prob /= N
#     return prob

# -----------------------------------------------------------------
# Ejercicio 5.6
# -----------------------------------------------------------------
# import random
# from collections import Counter

# def medir_temp(n):
#     return [37.5 + random.normalvariate(0, 0.2) for i in range(n)]

# def resumen_temp(n):
#     lista_temp = medir_temp(n).sort()  
#     longitud = len(lista_temp) 
#     return max(lista_temp), min(lista_temp), sum(lista_temp)/longitud, lista_temp[longitud/2]

# -----------------------------------------------------------------
# Ejercicio 5.7
# -----------------------------------------------------------------

# import numpy as np

# vector = np.arange(1, 19, 2)
# vector2 = np.linspace(1, 19, 10)

# -----------------------------------------------------------------
# Ejercicio 5.10
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# -----------------------------------------------------------------
# Ejercicio 5.11
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album_incompleto

# -----------------------------------------------------------------
# Ejercicio 5.12
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# -----------------------------------------------------------------
# Ejercicio 5.13
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# def cuantas_figus(figus_total):
#     album = crear_album(figus_total)
#     figuritas = 0
#     while album_incompleto(album):
#         album[comprar_figu(figus_total)] += 1
#         figuritas += 1
#     return figuritas

# -----------------------------------------------------------------
# Ejercicio 5.14
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# def cuantas_figus(figus_total):
#     album = crear_album(figus_total)
#     figuritas = 0
#     while album_incompleto(album):
#         album[comprar_figu(figus_total)] += 1
#         figuritas += 1
#     return figuritas

# def main_5_14():
#     resultados = [cuantas_figus(6) for i in range(1000)]
#     print(f'Se necesitan en promedio {np.mean(resultados)} figuritas para llenar un album de 6 figuritas')

# -----------------------------------------------------------------
# Ejercicio 5.15
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# def cuantas_figus(figus_total):
#     album = crear_album(figus_total)
#     figuritas = 0
#     while album_incompleto(album):
#         album[comprar_figu(figus_total)] += 1
#         figuritas += 1
#     return figuritas

# def main_5_14():
#     resultados = [cuantas_figus(6) for i in range(1000)]
#     print(f'Se necesitan en promedio {np.mean(resultados)} figuritas para llenar un album de 6 figuritas')

# def experimento_figus(n_repeticiones, figus_total):
#     resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
#     return np.mean(resultados)

# -----------------------------------------------------------------
# Ejercicio 5.17
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# def cuantas_figus(figus_total):
#     album = crear_album(figus_total)
#     figuritas = 0
#     while album_incompleto(album):
#         album[comprar_figu(figus_total)] += 1
#         figuritas += 1
#     return figuritas

# def main_5_14():
#     resultados = [cuantas_figus(6) for i in range(1000)]
#     print(f'Se necesitan en promedio {np.mean(resultados)} figuritas para llenar un album de 6 figuritas')

# def experimento_figus(n_repeticiones, figus_total):
#     resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
#     return np.mean(resultados)

# def comprar_paquete(figus_total, figus_paquete):
#     return [random.randint(0,figus_total - 1) for i in range(figus_paquete)]

# -----------------------------------------------------------------
# Ejercicio 5.18
# -----------------------------------------------------------------
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def crear_album(figus_total):
#     return np.zeros(figus_total)

# def album_incompleto(album):
#     return 0 in album

# def comprar_figu(figus_total):
#     return random.randint(0,figus_total - 1)

# def cuantas_figus(figus_total):
#     album = crear_album(figus_total)
#     figuritas = 0
#     while album_incompleto(album):
#         album[comprar_figu(figus_total)] += 1
#         figuritas += 1
#     return figuritas

# def main_5_14():
#     resultados = [cuantas_figus(6) for i in range(1000)]
#     print(f'Se necesitan en promedio {np.mean(resultados)} figuritas para llenar un album de 6 figuritas')

# def experimento_figus(n_repeticiones, figus_total):
#     resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
#     return np.mean(resultados)

# def comprar_paquete(figus_total, figus_paquete):
#     return [random.randint(0,figus_total - 1) for i in range(figus_paquete)]

# def cuantos_paquetes(figus_total, figus_paquete):
#     album = crear_album(figus_total)
#     paquetes = 0
#     while album_incompleto(album):
#         paquetes += 1
#         paquete = comprar_paquete(figus_total, figus_paquete)
#         for i in paquete:
#             album[i] += 1
#     return paquetes 
    
# -----------------------------------------------------------------
# Ejercicio 5.26
# -----------------------------------------------------------------

# import csv
# import os
# import matplotlib.pyplot as plt
# import numpy as np

# def leer_arboles(archivo):
#     f = open(archivo, 'rt', encoding="utf8")
#     rows = csv.reader(f)
#     headers = next(rows)
#     types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
#     arboleda = [{nombre:func(valor) for nombre, func, valor in zip(headers, types, row)} for row in rows]
#     return arboleda

# def medidas_de_especies(especies, arboleda):
#     datos_especies = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
#     return datos_especies

# def main_5_25():
#     arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#     alturas_jacaranda = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#     plt.hist(alturas_jacaranda, bins = 100)
#     plt.show()