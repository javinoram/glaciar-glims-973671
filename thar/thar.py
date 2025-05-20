
def elevation_limit_altitude(t, ab, am):
    return ab + t*(am - ab)


#Constantes de thar segun Poter et al (1983)
#indica valores ente 0.4 y 0.5 para glaciares limpios
thar_constants = [0.4, 0.425, 0.45, 0.475, 0.5]


#Pares de altura de diferentes puntos de la geomorfologia
#del glaciar
list_of_pairs = [(571, 909), (477, 909), (462, 909), (605, 909)]


for (ab, am) in list_of_pairs:
    print(f"Altura basal: {ab} - Altura cima: {am}")
    for t in thar_constants:
        ELA = elevation_limit_altitude(t, ab, am)
        print(ELA)


