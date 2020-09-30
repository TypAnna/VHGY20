''' detta skript löser SIR-modellen och plottar lösningarna, för givna
    bygennelsevillkor och värden på b och k
'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#funktion som returnerar listan dz/dt=[dsdt, didt, drdt]. Löser SIR-modellen
def model(z,t):
    s = z[0]
    i = z[1]
    r = z[2]
    #ange värdet på b (antal smittosamma kontakter) & k (andelen som tillfrisknar varje dag)
    b = 0.2
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
solution = odeint(model, z0, t)
''' solution innehåller lösningarna till alla tre: s(t), i(t) & r(t). solution
    är en lista av längd n=365. Varje element i denna lista ger lösningen av
    differentialekvationerna vid varje tidpunkt. Vart och ett av dessa element
    är i sin tur en lista av längd 3, på formen [s(t_j), i(t_j), r(t_j)] där
    t_j är en specifik tidpunkt (exempelvis dag 73). Alltså;
    solution = [[s(0), i(0), r(0)], [s(1), i(1), r(1)], ... [s(364), i(364), r(364)]]
'''
s_solution = solution[:, 0] #vi hämtar alla element på plats ett i varje lista i solution
i_solution = solution[:, 1] #vi hämtar alla element på plats två i varje lista i solution
r_solution = solution[:, 2] #vi hämtar alla element på plats tre i varje lista i solution

#plotta de tre linjerna
plt.plot(t, s_solution,'pink',label='s(t)')
plt.plot(t, i_solution,'orange',label='i(t)')
plt.plot(t, r_solution,'purple',label='r(t)')

plt.xlabel("Dagar")
plt.ylabel("Andel")
plt.legend(loc='best') #väljer den 'bästa' platsen för linjebeskrivningarna
#plt.savefig("SIRexempel.png")
plt.show()
