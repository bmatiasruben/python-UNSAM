# -----------------------------------------------------------------
# Ejercicio 6.9
# -----------------------------------------------------------------

import csv

def parse_csv(nombre_archivo, has_headers = True, select = None, types = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        registros = []

        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []       
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                if indices:
                    row = [row[index] for index in indices]
                if types: 
                    row = [func(val) for func, val in zip(types, row)]
                registro = dict(zip(headers, row))
                registros.append(registro)
        else:
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue            
                if types: 
                    row = [func(val) for func, val in zip(types, row)]
                registros.append(tuple(row))
    return registros


    