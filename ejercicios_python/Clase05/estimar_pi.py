# -----------------------------------------------------------------
# Ejercicio 5.5
# -----------------------------------------------------------------
import random
from collections import Counter

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def calculo_pi(N):
    puntos = 0
    for i in range(N):
        pos_x, pos_y = generar_punto()
        if pow(pos_x,2) + pow(pos_y,2) < 1:
            puntos += 1
    return 4*puntos/N   

def main():
    puntos = 0
    for i in range(100000):
        pos_x, pos_y = generar_punto()
        if pow(pos_x,2) + pow(pos_y,2) < 1:
            puntos += 1
    return 4*puntos/100000     