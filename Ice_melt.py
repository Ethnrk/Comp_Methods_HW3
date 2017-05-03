import numpy as np
from matplotlib import pyplot as plt

## initial parameters
Thickness = 2000

z_range = Thickness/10

z = 10. *np.arange(z_range)

T = 0.20 * np.arange(z_range)
## modifying T
for i in range(0,len(T)):
    T[i] = T[i] + -45
## more parameters
dt = 86400

k = 2.24
rho = 917
Cp = 210.8
rho_Cp = rho*Cp
T0 = T
## initial plot
plt.plot(T,z,'-m',linewidth =2)
plt.gca().invert_yaxis()




## set up for changing boundary condiitons
Surface_temp =[-40,-34,-27,-19]
for i in range(0,len(Surface_temp)):
    
    for h in range(int(3650*10)):
        ## set up so temperature changes with each time step except in the end.
        if i >> 0:
            diff = Surface_temp[i]-Surface_temp[i-1]
            delta_T = diff/(3650*10)
            Neu_Temp = Surface_temp[i] +(delta_T * np.arange(3650*10))
            T[0] = Neu_Temp[h]
        else:
            T[0] = Surface_temp[i]
            



        ## start differentiating by finding difference
    
        dT = np.diff(T)
        dz = np.diff(z)
        ## heat flux
        q = -k * dT/dz
        ## further differential work
        z_mid = np.cumsum(dz)
        dz_mid = np.diff(z_mid)
        ## the equation for finding temperature change
        dT_dt = -1/(rho_Cp) * np.diff(q) / dz_mid
        ## setting the actual changed temperature value
        T[1:-1] = T[1:-1] + dT_dt * dt
    ## plotting
    plt.plot(T,z)
    plt.title('Temperature profile of an ice sheet at 4 different periods')
    plt.ylabel('Ice Sheet Thickness (m)')
    plt.xlabel('Temperature (Celcius)')
plt.show()
