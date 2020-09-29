#Vi importerar pyplot modulen/delen av biblioteket och kallar det plt
import matplotlib.pyplot as plt
#Importerar numpy och kallar det np
import numpy as np

#Vi kan rita flera linjer i samma figur. Det gör vi enligt nedan.

x = np.linspace(0, 5, 100)
y1 = 2*x + 3 #linje 1
y2 = 1.5*x + 4 #linje 2

#linje 1, 'label' beskriver linjen och kommer skrivas ut i grafen.
plt.plot(x, y1, label="y=2x+3")
 #linje 2, ange linjens/kurvans namn med 'label'
plt.plot(x, y2, label="y=1.5x+4")
plt.xlabel("x") #Skriv ut vad x-axlen är
plt.ylabel("y") #Skriv ut vad y-axeln är
plt.legend() #anropa legend-funktionen för att linjernas namn ska synas i figuren
plt.show() #Denna funktioner visar den faktiska figuren. Utan denna - ingen graf!
