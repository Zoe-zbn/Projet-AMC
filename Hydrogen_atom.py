import numpy as np
import matplotlib.pyplot as plt
from Physical_parameter import hbar,Dq,e,e_0,m,V_c
from MC import T,dt,N0,nmax


# Initialisation des variables
r0 = np.random.normal(0, np.sqrt(dt*Dq*2), (N0, 3)) # positions initiales
r = r0.copy() # positions des particules
s = np.ones(N0)
n = N0 
n_list = [N0] # nombres de particules en fonction du temps
E=0
E_list = [E] # énergie de l'état fondamental en fonction du temps



# Boucle temporelle
for t in np.arange(0, T, dt):
    
    for i in range(len(r)):
        
        # Diffusion Brownien 3D
        r[i]+=np.random.normal(0, np.sqrt(2*Dq*dt), 3)

        # Test
        if s[i] >0 :
            # Création d'une particule
            if E - V_c(r[i]) > 0 : # rajouter la condition pour les plusieurs particules
                if np.random.uniform() > np.exp(-dt*(V_c(r[i]) - E)/hbar):
                    r = np.append(r, r)
                    s = np.append(s, 1)
                    n += 1
            else:
                # Test de survie
                if np.random.uniform() > np.exp(-dt*(V_c(r[i]) - E)/hbar):
                    s[i]=0
                    n-=1
                    
    # Réajustement de l'énergie
    V_sum=0
    N_sum=0
    for i in range(len(r)):
        if s[i]==1:
            V_sum +=V_c(r[i])
            N_sum+=1
    V_mean=V_sum/N_sum
    
    E = V_mean - (n-N0)/(N0*dt)
    E_list.append(V_mean)
    n_list.append(n)
    
    if len(r) > nmax:
        break


# Affichage des résultats
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(np.arange(0, T+dt, dt), E_list)
ax1.set_xlabel('Times')
ax1.set_ylabel('Energy')
ax2.plot(np.arange(0, T+dt, dt), n_list)
ax2.set_xlabel('Times')
ax2.set_ylabel('Particles Numbers')
plt.savefig("HA.png")
plt.plot()