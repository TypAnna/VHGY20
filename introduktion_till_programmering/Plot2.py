#Vi importerar pyplot modulen/delen av biblioteket och kallar det plt
import matplotlib.pyplot as plt
#Importerar numpy och kallar det np
import numpy as np

'''
    Vi skapar en lista med x-värden mha numpy. Den inbyggda funktionen linspace
    i biblioteket numpy kan användas för detta. Det första värdet är det minsta
    x-värdet, det andra det största x-värde vi vill ha, och det sista värdet
    är så många datapunkter vi vill ha.
'''

x = np.linspace(0, 5, 100)
y = 2*x + 3 #anger hur y beror av x

plt.plot(x, y) #Notera att ordningen är viktigt! Först x-värdena, sedan y-värdena
plt.xlabel("x") #Skriv ut vad x-axlen är
plt.ylabel("y") #Skriv ut vad y-axeln är
plt.show() #Denna funktioner visar den faktiska figuren. Utan denna - ingen graf!
