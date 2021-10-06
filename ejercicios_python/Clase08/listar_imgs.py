# -----------------------------------------------------------------
# Ejercicio 8.5
# -----------------------------------------------------------------

import os

def archivos_png(directorio):
    imagenes = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-4:].lower() == '.png':
                imagenes.append(name)
    return imagenes    

if __name__ == '__main__':
    import sys
    imagenes = archivos_png(sys.argv[1])
    for imagen in imagenes:
        print(imagen)