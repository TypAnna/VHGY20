# -*- coding: utf-8 -*- detta skriver vi för att kunna använda 'åäö'

#Vad händer om vi istället skriver:
#print("Hello", Elin)

''' Då blir det fel i programmet! Datorn förstår inte vad Elin är.
    Datorn tror att Elin är ett variabelnamn. Men vi har inte sagt till datorn
    vad vi menar med Elin - därför får vi ett error när vi kör programmet.
'''

namn = "Elin" #Vi tilldeler variablen namn texten Elin
print("Hello", namn)

''' Nu vet datorn vad 'namn' betyder - för vi har sagt att namn är lika med
    "Elin!". Vi har tilldelat varibeln namn värdet "Elin"

'''

ålder = 24 #Vi tilldeldar variabeln 'ålder' siffran 24
print("Jag är", ålder, "år gammal")
