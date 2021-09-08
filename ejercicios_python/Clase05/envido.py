# -----------------------------------------------------------------
# Ejercicio 5.4
# -----------------------------------------------------------------
import random
from collections import Counter

def mano_truco():
    mano = []
    palos = ['oro', 'copa', 'espada', 'basto']
    valores = [1,2,3,4,5,6,7,10,11,12]
    cartas = [(valor, palo) for valor in valores for palo in palos]
    mano = random.sample(cartas, k=3)
    return mano

def valor_envido(mano, cant):
    cant_palos = Counter(carta[1] for carta in mano)
    max_palo = max(cant_palos, key=cant_palos.get)
    envido = 0
    for valor, palo in mano:
        if cant_palos[max_palo] > 1 and palo == max_palo:
            if valor < 8:
                envido += valor
    if cant_palos[max_palo] == 3:
        if max(mano)[0] < 9:
            envido -= min(mano)[0]
    if envido == cant - 20:
        return True
    else:
        return False

def prob_envido(N, cant):
    prob = sum([valor_envido(mano_truco(), cant) for i in range(N)])
    return prob/N