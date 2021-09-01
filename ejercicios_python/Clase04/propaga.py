# -----------------------------------------------------------------
# Ejercicio 4.6
# -----------------------------------------------------------------

def propagar(lista):
    pos_carb = [-1]
    pos_enc = []
    lista_propagada = []
    largo = 0
    for index, fosforo in enumerate(lista):
        largo += 1
        lista_propagada.append(fosforo)
        if fosforo == -1:
            pos_carb.append(index)
        elif fosforo == 1:
            pos_enc.append(index)
    pos_carb.append(largo)

    for index, pos in enumerate(pos_carb[:-1]):
            if pos < pos_enc[0] < pos_carb[index + 1]:
                lista_propagada[pos + 1:pos_carb[index+1]] = [1 for i in range(pos_carb[index+1]-pos-1)]
                pos_enc.pop(0)

    return lista_propagada