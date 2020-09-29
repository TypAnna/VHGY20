# -*- coding: utf-8 -*- detta skriver vi för att kunna använda 'åäö'

''' Den här funktionen beräknar hur gammal någon är, givet deras födelseår
    och det nuvarande årtalet'''
def calculateAge(name, birthYear, currentYear):
    print(name, "is", currentYear-birthYear, "years old")

calculateAge("Liza", 1983, 2020)
