import matplotlib.pyplot as plt
#Vi importerar pyplot modulen/delen av biblioteket och kallar det plt


''' pyplot har en funktion som heter 'plot' som tar emot en mängd parametrar.
    Vi anropar denna funktion genom att skriva 'plt.plot()' tillsammans med
    de parametrar vi vill.

    Ett sätt att rita en kurva/linje är att skapa två listor. Låt de två
    listorna representera de olika par av (x, y) punkter i vår linje.
    Alltså: den ena listan är x-punkterna, och den andra är y-punkterna.
    Passa sedan dessa som parametrar likt nedan.
'''
x = [1, 2 , 3, 4, 5, 6]
y = [1, 3, 2, 2.6, 0.9, 1.5]
plt.plot(x, y) #Notera att ordningen är viktigt! Först x-värdena, sedan y-värdena
plt.xlabel("Mätning") #Skriv ut vad x-axlen är
plt.ylabel("Temperatur") #Skriv ut vad y-axeln är
plt.show() #Denna funktioner visar den faktiska figuren. Utan denna - ingen graf!
