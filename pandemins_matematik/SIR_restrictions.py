''' detta skript löser SIR-modellen och plottar ifektionskurvorna för givna
    bygennelsevillkor och k-värden och visar hur restriktioner (ändringar av
    b-värdet) påverkar kurvorna
'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import exp


"""
    Funktionen returnerar listan dz/dt=[dsdt, didt, drdt], och beskriver
    de tre differentialekvationerna i SIR-modellen. Denna funktion kan användas
    för att illustrera hur restriktioner (alltså förändringar i b-värdet)
    påverkar lösningarna.

    - parametern 'restrictionsApplied' är en boolean, och är alltså antingen
        True eller False. Om du vill att restriktioner ska införas - sätt
        denna parameter till True.
    - parametern 'daysOfRestriction' är ett heltal som anger hur många dagar
        restriktionen gäller.
    - parametern 'startDay' är ett heltal som anger vid vilken dag i ordningen
        som restriktionerna börjar införas
    - parametern b0 är en float (decimaltal) och är det b-värde vi har utan restriktioner
    - parametern b_min är en float (decimaltal) och är det minsta b-värde vi har,
        alltså det b-värde vi har när restriktionerna har införts 'helt'
"""
def model(z,t, b, restrictionsApplied, daysOfRestriction, startDay, b0, b_min): #ta in b som parameter!
    s = z[0]
    i = z[1]
    r = z[2]
    k = 0.04 #k=1/D där D är antal dagar en person är infekterad i snitt
    #kom ihåg: R_0 = b/k
    ''' Om restrictionsApplied=True så kommer datorn gå in i allt som står
        i blocket nedan (allt som är indenerat/tabat under if-satsen)
    '''
    if restrictionsApplied:
        #~~~början på block~~
        n=0.1 #en förändringsfaktor, sätt inte ett större värde än 1!
        if t>startDay and t<startDay+daysOfRestriction:
            #****början på block****
            ''' Om den nuvararande tidpunkten/dagen befinner sig i intervallet då
                vi har restriktioner, så ges b av formeln nedan. Denna formeln
                gör så att inte b går direkt från b0 till b_min, utan att det
                blir en 'mjuk' övergång från b0 till b_min. Om vi istället
                sätter b=b_min så kommer vi få ett 'hack' i kurvan. Testa själv!
                Du väljer själv om du vill ha en direkt övergång eller en gradvis övergång.
            '''
            t1 = t - startDay #för att få 'rätt' t till formeln nedan
            b= b0* exp(- n * t1) + (1 - exp(- n * t1)) * b_min
            #****slut på block****
        if t>=startDay+daysOfRestriction:
            #^^^^början på block^^^
            ''' När restriktionerna är slut så kommer b gå från b_min tillbaka
                till b_0 med en 'mjuk' övergång. Ju större n är, desto snabbare
                sker övergången!
            '''
            t2 = t - startDay - daysOfRestriction
            b= b_min* exp(- n * t2) + (1 - exp(- n * t2)) * b0
            #^^^^slut på block^^^^
        #~~~~slut på block~~~~
    #print(b, t)
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
b1 = 0.2
b_min = 0.05
#det är viktigt att du passar in parametrarna i samma ordning som i funktionsdefinitionen!!

''' Här löser vi SIR-modellen då vi inför restriktioner dag 40, och som pågår
    i 100 dagar. Under restriktionerna går b ner till b_min
'''
solution1 = odeint(model, z0, t, args=(b1, True, 100, 40, b1, b_min))

''' Här inför vi inga restriktioner, eftersom vi passar in parametern False,
    vilket betyder att i funktioner kommer restrictionsApplied sättas till False.
    Observera att de andra parametrarna kan sättas till vad som helst -
    eftersom dessa inte kommer användas.'''
solution2 = odeint(model, z0, t, args=(b1, False, 30, 40, b1, b_min))


''' solution innehåller lösningarna till alla tre: s(t), i(t) & r(t). solution
    är en lista av längd n=365. Varje element i denna lista ger lösningen av
    differentialekvationerna vid varje tidpunkt. Vart och ett av dessa element
    är i sin tur en lista av längd 3, på formen [s(t_j), i(t_j), r(t_j)] där
    t_j är en specifik tidpunkt (exempelvis dag 73). Alltså;
    solution = [[s(0), i(0), r(0)], [s(1), i(1), r(1)], ... [s(364), i(364), r(364)]]
'''

i1_solution = solution1[:, 1] #vi hämtar alla element på plats två i varje lista i solution1
i2_solution = solution2[:, 1]

#plotta de två infektionskurvorna
plt.plot(t, i1_solution,'pink',label='Restriktioner dag 40-140, b=[0.2, 0.05]')
plt.plot(t, i2_solution,'orange',label='Inga restriktioner, b=0.2')


plt.xlabel("Dagar")
plt.ylabel("Andel")
plt.ylim(top=1) #om du vill se hela y-axeln
plt.legend(loc='best') #väljer den 'bästa' platsen för linjebeskrivningarna
#plt.savefig("SIRexempel.png")
plt.show()
