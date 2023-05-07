import numpy as np
import matplotlib.pyplot as plt
from Physical_parameter import Dq
from MC import T,dt

# Initialisation des variables
X0 =  np.random.normal(0, np.sqrt(dt*Dq*2),1)
X_list = [X0]
r0 = np.random.normal(0, np.sqrt(dt*Dq*2), (1, 3))
r_list=[r0]

X_3d=[]
Y_3d=[]
Z_3d=[]

# Boucle temporelle 
for t in np.arange(0, T, dt):
    # Diffusion Brownien suivant une loi gaussien 
    
    # Cas 1D 
    X=X0 + np.random.normal(0, np.sqrt(dt*Dq*2))
    X_list.append(X)
    X0 = X
    
    #Cas 3D
    r = r0 + np.random.normal(0, np.sqrt(2*Dq*dt), (1,3))
    r_list.append(r0)
    r0=r
    X_3d.append(r[:,0])
    Y_3d.append(r[:,1])
    Z_3d.append(r[:,2])

    
    
fig, (ax1) = plt.subplots(1, 1, figsize=(8, 4))
ax1.plot(X_list,np.arange(0, T+dt, dt))
ax1.set_ylabel('Times')
ax1.set_xlabel('Positions (1D)')
ax1.set_title('Brownian diffusion')
plt.savefig("BD1D.png")
plt.plot()

fig = plt.figure()
axes = fig.gca(projection='3d')
axes.scatter(X_3d,Y_3d,Z_3d,"x") 
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('z')
axes.set_title('Brownian diffusion 3D')
axes.tight_layout()
plt.savefig("BD3D.png")
plt.show()



