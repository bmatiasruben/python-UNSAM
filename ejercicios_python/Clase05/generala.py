# -----------------------------------------------------------------
# Ejercicio 5.2
# -----------------------------------------------------------------
import random
from collections import Counter

def es_generala(tirada):
    valor = tirada[0]
    for dado in tirada:
        if dado != valor:
            return False
    return True

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def mano_generala(tirada):
    for i in range(2):         
        if es_generala(tirada):
            return tirada
        else:
            maximo = max(Counter(tirada), key=Counter(tirada).get)
            tirada_aux = []
            for j in tirada:
                if j == maximo:
                    tirada_aux.append(j)
                else:
                    tirada_aux.append(random.randint(1,6))
            tirada = tirada_aux.copy()
    return(tirada)

def prob_generala(N):
    cant_gen = sum([es_generala(mano_generala(tirar())) for i in range(N)])
    return cant_gen/N