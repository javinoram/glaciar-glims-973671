import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

#Ruta del archivo
path_file = "geomorfologia.xlsx"
#Curva de altura de la cuenca
df = ( pd.read_excel(path_file).to_numpy().T )[0]

#Lista de porcentajes
percentaje_range = np.linspace(0.0, 1.0, len(df))

#Interpolacion de la curva de elevacion
spl = CubicSpline(percentaje_range, df)


#Usando la interpolacion se calcula la ELA en una vecindad
punto_inicial = 2.0/3.0
vecindad = 1e-2

p1 = np.round(spl(punto_inicial - vecindad), 3)
p2 = np.round(spl(punto_inicial), 3)
p3 = np.round(spl(punto_inicial + vecindad), 3)

print(p1, p2, p3)

fig, ax = plt.subplots()
x = np.linspace(0.0, 1.0, 25)
y = [ spl(x_i) for x_i in x ]
ax.plot(x, y, linewidth=2.0)
plt.show()
