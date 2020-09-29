import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint #ett annat sätt att importera

#funktion som returnerar dydt
def model(y,t):
    k = 0.3
    dydt = -k * y #detta är differentialekvationen vi vill lösa! Ex: bakterietillväxt
    return dydt

#begynnelsevillkor
y0 = 5

#de tidpunkter för vilka vi vill lösa y(t)
t = np.linspace(0,20)

#löser differentialakvationen med odeint-funktionen i scipy
y = odeint(model,y0,t)

# plotta resultat
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
