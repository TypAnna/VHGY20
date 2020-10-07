''' detta skript löser SIR-modellen och plottar ifektionskurvorna för givna
    bygennelsevillkor och värden på b och k
'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#funktion som returnerar listan dz/dt=[dsdt, didt, drdt]. Löser SIR-modellen
# z = [s, i, r]
def model(z,t, b): #ta in b som parameter!
    s = z[0]
    i = z[1]
    r = z[2]
    #ange värdet på b (antal smittosamma kontakter) & k (andelen som tillfrisknar varje dag)
    k = 0.04 #k=1/D där D är antal dagar en person är infekterad i snitt
    #R_0 = b/k
    dsdt = -b*s*i
    didt = b*s*i-k*i
    drdt = k*i
    dzdt = [dsdt,didt, drdt]
    return dzdt

#begynnelsevillkor, s(0)=1, i(0)=0.0002, r(0)=0
z0 = [1,0.0002,0]

#antal tidpunkter (dagar) vi vill lösa differentialakvationen för
n = 365

#skapar en lista med tidpunkterna [0, 1, 2, 3, ..., 363, 364]
t = np.linspace(0,n-1,n)


#löser SIR-modellen
b1 = 0.4
b2 = 0.2
b3 = 0.1
solution1 = odeint(model, z0, t, args=(b1,)) #vi löser diff-ekvationerna en gång för b=0.4...
solution2 = odeint(model, z0, t, args=(b2,)) #och en gång för b=0.2 ...
solution3 = odeint(model, z0, t, args=(b3,)) #och en till gång för b=0.1
''' solution innehåller lösningarna till alla tre: s(t), i(t) & r(t). solution
    är en lista av längd n=365. Varje element i denna lista ger lösningen av
    differentialekvationerna vid varje tidpunkt. Vart och ett av dessa element
    är i sin tur en lista av längd 3, på formen [s(t_j), i(t_j), r(t_j)] där
    t_j är en specifik tidpunkt (exempelvis dag 73). Alltså;
    solution = [[s(0), i(0), r(0)], [s(1), i(1), r(1)], ... [s(364), i(364), r(364)]]
'''

i1_solution = solution1[:, 1] #vi hämtar alla element på plats två i varje lista i solution1
i2_solution = solution2[:, 1]
i3_solution = solution3[:, 1]

#plotta de tre infektionskurvorna
plt.plot(t, i1_solution,'pink',label='b=0.4') #ange vilket b-värde som är vilken kurva
plt.plot(t, i2_solution,'orange',label='b=0.2')
plt.plot(t, i3_solution,'purple',label='b=0.1')


plt.xlabel("Dagar")
plt.ylabel("Andel")
#plt.ylim(top=1) #om du vill se hela y-axeln
plt.legend(loc='best') #väljer den 'bästa' platsen för linjebeskrivningarna
#plt.savefig("SIRexempel.png")
plt.show()
