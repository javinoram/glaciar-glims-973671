import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
ice_density = 917
yield_stress = 45000
step_length = 100

def compute_b(lista, indx):
    return -(lista[indx-1] + lista[indx])

def compute_c(lista_1, lista_2, lista_3, lista_4, indx):
    aux1 = lista_3[indx-1]*(lista_2[i]-lista_4[indx-1])
    aux2_1 = 2*(lista_1[indx]-lista_1[indx-1])*yield_stress
    aux2_2 = g*ice_density
    return  aux1 - (aux2_1/aux2_2)

path_file = "glaciar.xlsx"
excel_sheet = "mp1"

for excel_sheet in ["mp1", "mp2", "mp3", "mp4"]:
    df = pd.read_excel(path_file, sheet_name=excel_sheet).to_numpy().T
    distancia = [ float(i) for i in df[0] ]
    altura = [float(i) for i in df[1]]

    distancia_terminal_l = []
    altitud_l = []
    elevacion_hielo_l = []
    h_l = []

    for i,altitud in enumerate(altura):
        if i == 0:
            altitud_l.append( altura[0] )
            elevacion_hielo_l.append( altura[0] )
            distancia_terminal_l.append( distancia[0] )
            h_l.append( 0 )

        else:
            altitud_l.append( altitud )
            distancia_terminal_l.append( distancia[i] )

            b = compute_b( altitud_l, i)
            c = compute_c(distancia_terminal_l, altitud_l, elevacion_hielo_l, h_l, i)
            elevacion_hielo_l.append( (-b + (b*b - 4*c)**0.5)/2.0 )

            h_l.append( elevacion_hielo_l[i] - altitud )


    fig, ax = plt.subplots()
    ax.plot(distancia, altura, linewidth=2.0)
    ax.plot(distancia, elevacion_hielo_l, linewidth=2.0)
    fig.savefig(f"{excel_sheet}.png", dpi=fig.dpi)
