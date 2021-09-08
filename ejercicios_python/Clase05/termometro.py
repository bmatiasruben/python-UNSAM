# -----------------------------------------------------------------
# Ejercicio 5.8
# -----------------------------------------------------------------
import random
from collections import Counter
import numpy as np

def medir_temp(n):
    return [37.5 + random.normalvariate(0, 0.2) for i in range(n)]

def resumen_temp(n):
    lista_temp = medir_temp(n).sort()  
    if n%2 == 1:
        return max(lista_temp), min(lista_temp), sum(lista_temp)/n, (lista_temp[n//2] + lista_temp[n//2-1])/2
    else:
        return max(lista_temp), min(lista_temp), sum(lista_temp)/n, lista_temp[n//2]
temp_array = np.array(medir_temp(999))
np.save('../Data/temperaturas', temp_array)

