# -*- coding: utf-8 -*- detta skriver vi för att kunna använda 'åäö'


''' Men varför fungerar detta?! Hur vet datorn vad "Hello World!" är?
    Jo - detta har med TYPER att göra. Genom att omringa karaktärer med
    citattecken så säger vi åt datorn att detta är ett objekt av typen 'sträng'.
    Vi skapar faktiskt ett objekt med typen 'sträng' som datorn sedan skriver ut.
'''
print("Hello World!")


''' Vi skapar ett objekt som är av typen 'sträng' (string) och binder detta
    objekt till variabelnamnet 'namn'.
'''
namn = "Elin"

''' Vi skapar ett objekt som är av typen 'heltal' (integer) och binder detta
    objekt till variabelnamnet 'ålder'.
'''
ålder = 10

print("Hello", namn)
print("Jag är", ålder, "år gammal")


print("Summan av heltalen 3 och 4 är", 3+4)
print("Summan av strängarna 3 och 4 är", "3"+"4")
print("Längden av strängen", namn, "är", len(namn))
