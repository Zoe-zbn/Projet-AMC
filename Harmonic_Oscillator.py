import numpy as np
import matplotlib.pyplot as plt
from Physical_parameter import hbar,F_e,Dq,V,E0
from MC import T,dt,N0,nmax



# Initialisation : creation des tableaux
x = np.random.normal(0, np.sqrt(dt*Dq*2), N0) # liste de N0 particules sur une gaussien
s = np.ones(N0) # Liste de un parametre de vie s=1 et mort s=0
n_list = [N0] # Liste du nombre de particules morte ou vivante du system
E_list = [E0] # Liste des valeur d'energie
x_max=10 # Taille de la liste maximal 
n = N0 # Paramètre de contage 
death_list = []
E_ref_list = [E0] #Liste pour stocker les positions des particules mortes 
E=E0


# Boucle temporelle virtuel 
for t in np.arange(0, T, dt):
    # Diffusion Brownien suivant une loi gaussien 
    for i in range(len(s)):
        '''
        #Enregistrement de l'ancienne postion pour le test ligne 34-37
        x_test = x[i]
        '''
        # Diffusion pour chaque particules
        x[i] += np.random.normal(0, np.sqrt(2*Dq*dt)
                                 
        '''
        #Test de la nouvelle probabilitée    
        # Acceptation ou rejet 
        if np.random.uniform(0.0, 1.0) < np.exp(-(V(x[i]) - V(x_test)) / hbar)  :
            x[i] = x[i]
        else:
            x[i]=x_test
        '''
        
        # Test Monte-Carlo : life-death rate cf raport 
        if s[i] == 1.0 : # on regarde uniquement les particules en vie (s=1)
            # Création d'une particule
            if E - V(x[i]) > 0 : 
                if np.random.uniform() > np.exp(dt*(F_e*V(x[i]) - E)/hbar):
                    n += 1
                    if len(death_list) != 0: # La particule ressuscite
                        s[int(death_list[0])] = 1
                        death = np.delete(death_list,0) # supprime l'information de la particule uttilisée (premiere de la liste)
                    else:
                        x = np.append(x,x[i])
                        s = np.append(s,1)
            else:
                # Test de survie
                if np.random.uniform() > np.exp(-dt*(F_e*V(x[i]) - E)/hbar):
                    s[i]=0
                    n-=1
                    death_list = np.append(death_list,i) # stockage de la position de la particule morte

    # Réajustement de l'énergie (Article Anderson )
    V_sum=0
    N_sum=0
    for i in range(len(s)):
        if s[i]==1.0:
            V_sum +=V(x[i])
            N_sum+=1
    V_mean=V_sum/N_sum
    E = F_e*V_mean - (n-N0)/(N0*dt)

    # Enregistrement des données
    n_list.append(n)
    E_list.append(F_e*V_mean)
    E_ref_list.append(E)
    
    if len(x) > nmax:
        break

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(np.arange(0, T+dt, dt), E_list)
ax1.set_xlabel('Times')
ax1.set_ylabel('Energy ')
ax2.plot(np.arange(0, T+dt, dt), E_ref_list)
ax2.set_xlabel('Energy reference')
ax2.set_ylabel('Particles Numbers')
plt.savefig("OH.png")
plt.plot()
