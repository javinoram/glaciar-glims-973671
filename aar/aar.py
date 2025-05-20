import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#Ruta del archivo
path_file = "geomorfologia.xlsx"

##Nombre de las hojas, esto debe ser modificado para 
##ajustarse a los valores propios
for excel_sheet in ['mp1', 'mp2', 'mp3', 'mp4']:
    print(f"Procesando hoja {excel_sheet}")

    df = pd.read_excel(path_file, sheet_name=excel_sheet).to_numpy().T
    per = df[0]
    altura = df[1]
    #Usando la interpolacion se calcula la ELA en una vecindad
    #Se considera un area de ablasion de 0.6
    punto_inicial = 0.4
    vecindad = 1e-2

    ##Imagen descriptiva de la cuenca
    ##Se guardan en la carpeta en que se ejecutan
    fig, ax = plt.subplots()
    ax.plot(per, altura, linewidth=2.0)
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.axvline(x=(punto_inicial)*100, color='black', linestyle='-')
    ax.axvline(x=(punto_inicial+vecindad)*100, color='red', linestyle='--')
    ax.axvline(x=(punto_inicial-vecindad)*100, color='red', linestyle='--')
    fig.savefig(f"{excel_sheet}.png", dpi=fig.dpi)
