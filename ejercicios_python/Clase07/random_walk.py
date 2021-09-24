import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def graficar(distancia = 100000, trayectorias = 12):
    max = 0
    min = np.inf
    fig = plt.figure()
    plt.subplot(2, 1, 1)
    plt.xticks([])
    plt.title(f'{trayectorias} caminatas al azar')
    for i in range(trayectorias):
        random_list = randomwalk(distancia)
        plt.plot(random_list)
        if np.max(np.abs(random_list)) > max:
            max = np.max(np.abs(random_list))
            lista_max = random_list.copy()
        if np.max(np.abs(random_list)) < min:
            min = np.max(np.abs(random_list))
            lista_min = random_list.copy()
    
    plt.subplot(2, 2, 3)
    plt.title('La caminata que más se aleja')
    plt.plot(lista_max)
    plt.ylim(-np.max(np.abs(lista_max)), np.max(np.abs(lista_max)))
    plt.xticks([])
    plt.subplot(2, 2, 4)
    plt.title('La caminata que menos se aleja')
    plt.plot(lista_min)
    plt.xticks([]), plt.yticks([])
    plt.ylim(-np.max(np.abs(lista_max)), np.max(np.abs(lista_max)))

    plt.show()
    
graficar()
    




