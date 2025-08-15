import pandas as pd
import numpy as np

def ohmura_eq(t, dt):
    return 966 + 230*(t-dt) + 5.87*( (t-dt)**2 )
    #return 645 + 296*(t-dt) + 9*( (t-dt)**2 )

#Temperatura minima
#t_paleo_melm = [5.079, 4.468, 4.3705]
#t_paleo_thar = [4.9944, 4.9425, 4.7604]
#t_paleo_aar = [5.261, 4.9944, 4.806]
#t_actual = 5.3

#Temperatura media
t_paleo_melm = [0.0, 0.0, 10.3865]
t_paleo_thar = [10.5945, 10.5425, 10.3605]
t_paleo_aar = [10.861, 10.5945, 10.406]
t_actual = 10.9

#Temperatura maxima
#t_paleo_melm = [15.579, 14.968, 14.8705]
#t_paleo_thar = [15.4945, 15.4425, 15.2605]
#t_paleo_aar = [15.761, 15.4945, 15.306]
#t_actual = 15.8

delta = 0.0 
print("actual: ", ohmura_eq(t_actual, delta) )

for t in t_paleo_melm:
    delta = -(t_actual - t) 
    print("melm: ", ohmura_eq(t_actual, delta) )

for t in t_paleo_thar:
    delta = -(t_actual - t)
    print("thar: ", ohmura_eq(t_actual, delta) )

for t in t_paleo_aar:
    delta = -(t_actual - t) 
    print("aar: ", ohmura_eq(t_actual, delta) )
