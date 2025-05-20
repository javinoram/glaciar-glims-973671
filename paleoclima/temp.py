import pandas as pd
import numpy as np

#Variacion de temperatura es regla de 3
def temp_eq(t_actual, var_h):
    return t_actual + 6.5*var_h


#[0]: Actual, [1]: MR1, [2]:MR2, [3]:MR3
melm = (np.array([571, 477, 462]) - 605)/1000.0
thar = (np.array([693, 685, 657]) - 740)/1000.0
aar = (np.array([690, 649, 620]) - 696)/1000.0
temperatures = np.array([15.8, 9.9, 5.3])

print("MELM reconstruction")
for t in temperatures:
    print(t, [temp_eq(t, diff) for diff in melm ])

print("THAR reconstruction")
for t in temperatures:
    print(t, [temp_eq(t, diff) for diff in thar ])

print("AAR reconstruction")
for t in temperatures:
    print(t, [temp_eq(t, diff) for diff in aar ])

