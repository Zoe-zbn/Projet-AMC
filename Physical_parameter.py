import numpy as np

# Physical Constants

hbar = 1.0 # Constante de planck reduite 
m = 1.0 # Masse  
omega = 1
F_e=  m * (omega**2) # factor for Harmonqie oscillator
Dq = hbar/(2*m)
e = 1.0      # Electron charge
e_0 = 1.0  # Permittivité du vide

#Potential

# Harmonique oscillator

def V(x):
    return 0.5*(x**2)

E=E0=0.5

#lHydrogène Atom

def V_c(r):#potentiel coulombien
    return -e**2/(4*np.pi*e_0*np.linalg.norm(r))
