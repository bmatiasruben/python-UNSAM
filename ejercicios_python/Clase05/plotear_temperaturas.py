# -----------------------------------------------------------------
# Ejercicio 5.9
# -----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.xlabel("Temperaturas (ºC)")
    plt.ylabel("Ocurrencias")
    plt.hist(temperaturas,bins=25)
    plt.show() 