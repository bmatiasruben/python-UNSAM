# -----------------------------------------------------------------
# Ejercicio 8.2
# -----------------------------------------------------------------

import datetime

def cuanto_falta():
    fecha = datetime.datetime.now()
    if (fecha.month > 9) or (fecha.month == 9 and fecha.day > 21):
        prox_primavera = datetime.datetime(fecha.year + 1, 9, 21)
    else:
        prox_primavera = datetime.datetime(fecha.year, 9, 21)
    
    diferencia = prox_primavera - fecha
    print(f'FALTAN {diferencia.days} DIAS PARA LA PRIMAVERA')
    return diferencia.days