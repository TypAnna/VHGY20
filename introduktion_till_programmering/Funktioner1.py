# -*- coding: utf-8 -*- detta skriver vi för att kunna använda 'åäö'

''' Vi definierar en funktion med nyckelordet 'def' följt av namnet på vår
    funktion, följt av en parentes som innehåller eventuella argument.
'''
def helloYou(name):
    print("Hello", name)

helloYou("Kaj") #Vi anropar funktionen 'helloYou' med parametern "Kaj".


def greetings(name, age): #den här funktionen tar två argument
    print("Hello! I'm", name, "and I'm", age, "years olds")

#Vi kan anropa en funktion hur många gånger som helst!
greetings("Ben", 89)
greetings("Sherlock", 40)

#En typisk matematisk funktion
def polynomialFunction(x):
    y = x^2 + 2*x + 7
    print("When x is",x, "y is", y)

polynomialFunction(2)

#Vi kan också låta en funktion returnera ett värde - så att vi kan spara det
def straightLineFunction(x):
    answer = 3*x + 5
    return answer

x = 10
y = straightLineFunction(x)
print("When x is",x, "y is", y)
