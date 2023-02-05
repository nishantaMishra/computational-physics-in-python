########################################################
######           Birch Murnaghan equation          ##########
#######################################################
"""This example requires to calculate the value using for loop """
import numpy as np
import matplotlib.pyplot as plt
#--------------------------
E_0 = -4852.902953
B = 49.4348
E2=[]
BP = 4.4875
V_0 = 1173.6125
V = [1167.2893, 1050.5603, 992.196, 1108.9248, 1284.0181, 1342.3827, 1167.2893, 1225.6537]
V.sort() #arranged V in ascending order
#----------------------------
for i in range(len(V)):
    N = (V_0/V[i])**(1/3)
    print('\t',N)
    E = E_0 + (9/16)*(B/14703.6)*V_0*(((((N**2)-1)**3)*BP)+ ((N**2)-1)**2*(6-4*N**2))
    E2.append(E)    
print('These are the values of E ',E2)
print('The Values of V are',V)
#-----------------------
plt.plot(E2,V)
plt.scatter(E2,V, label='Points of calculation')
plt.xlabel('Energy')
plt.ylabel('Volume')
plt.title("Volume Energy Graph")
plt.legend()
plt.show()

