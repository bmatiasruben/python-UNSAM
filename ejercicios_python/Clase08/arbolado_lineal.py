# -----------------------------------------------------------------
# Ejercicio 8.7
# -----------------------------------------------------------------

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

f_nombre = os.path.join('..', 'Data', 'arbolado-publico-lineal-2017-2018.csv')
df = pd.read_csv(f_nombre)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]
especies_comunes = df_lineal['nombre_cientifico'].value_counts()[:10]
print(especies_comunes)

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
plt.show()
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')