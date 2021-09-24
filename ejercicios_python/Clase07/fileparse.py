# -----------------------------------------------------------------
# Ejercicio 7.6
# -----------------------------------------------------------------

import csv

def parse_csv(lista, has_headers = True, select = None, types = None, silence_errors = False):
    '''
    Parsea una lista de columnas en una lista de registros
    '''
    rows = csv.reader(lista)
    registros = []
    if not has_headers and select:
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []       
        for i, row in enumerate(rows):
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
            if types: 
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except Exception as e:
                    if not silence_errors:
                        print(f'Fila {i + 1}: No pude convertir {row}')
                        print(f'Fila {i + 1}: Motivo {e}')
            registro = dict(zip(headers, row))
            registros.append(registro)
    else:
        for i, row in enumerate(rows):
            if not row:    # Saltea filas sin datos
                continue            
            if types:
                try: 
                    row = [func(val) for func, val in zip(types, row)]
                except Exception as e:
                    if not silence_errors:
                        print(f'Fila {i}: No pude convertir {row}')
                        print(f'Fila {i}: Motivo {e}')
            registros.append(tuple(row))
    return registros