# -----------------------------------------------------------------
# Ejercicio 6.12
# -----------------------------------------------------------------

import informe_funciones 

def costo_camion(archivo):
    rows = informe_funciones.leer_camion(archivo)
    costo_total = 0
    for line in rows:
        costo_total += line['cajones'] * line['precio']
    return costo_total
