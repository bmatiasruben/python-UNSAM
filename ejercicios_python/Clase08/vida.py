# -----------------------------------------------------------------
# Ejercicio 8.1
# -----------------------------------------------------------------

import datetime

def vida_en_segundos(fecha_nac):
    dia_nac, mes_nac, año_nac = fecha_nac.split('/')
    fecha_nacimiento = datetime.datetime(int(año_nac), int(mes_nac), int(dia_nac))
    fecha = datetime.datetime.now()

    diferencia = fecha - fecha_nacimiento
    return diferencia.days * 24 * 60 * 60 + diferencia.seconds + diferencia.microseconds * pow(10,-6)
