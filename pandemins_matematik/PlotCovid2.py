''' I detta script plottar vi riktig data från Sverige tillsammans med 'teoretisk' data.'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import exp

''' Vi läser in all Covid-data. complete_df är en tabell med massor av data.
    Denna data kommer härifrån: https://github.com/owid/covid-19-data/tree/master/public/data.
    När du plottar själv, se till så att du har laddat ned filen owid-covid-data.csv.

    Alla kolumner i denna tabell är:

    iso_code, continent, location, date, total_cases, new_cases,
    new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed,
    total_cases_per_million, new_cases_per_million,
    new_cases_smoothed_per_million, total_deaths_per_million,
    new_deaths_per_million, new_deaths_smoothed_per_million, total_tests,
    new_tests, new_tests_smoothed, total_tests_per_thousand,
    new_tests_per_thousand, new_tests_smoothed_per_thousand, tests_per_case,
    positive_rate, tests_units, stringency_index, population,
    population_density, median_age, aged_65_older, aged_70_older,
    gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence,
    female_smokers, male_smokers, handwashing_facilities,
    hospital_beds_per_thousand, life_expectancy, human_development_index

    Så all denna data finns! Du kan själv välja vad vill du vill kika närmre på.
    Se till så att du dubbelkollar datan (exempelvis har alla länder kanske inte
    rapporterat hur många som är äldre än 70, har diabetes, är rökare osv)
'''

''' VIKTIGT, observera att vi INTE har data på hur många som är infekterade vid varje
    tidpunkt. I tabellen har vi hur många RAPPORTERADE nya fall vi har varje dag,
    men vi vet inte när folk blir friska. I detta exempel har jag därför valt att
    använda datan i kolumnen 'total_cases', vilket alltså är det TOTALA antal rapporterade
    fall varje dag. Alltå, om vi har 10 fall dag 3, och 5 nya fall rapporteras dag 3,
    så är det totala antal fallen dag 4 = 10 + 5 = 15.

    Så vilken data motsvarar detta i SIR-modellen? Jo - det totala antalet fall
    är ju så många som är sjuka just nu (=I) plus så många som har tillfriskat samt
    avlidit (=R). Så i detta skript plottar vi funktionen I+R tillsammans med
    riktig data på samma siffror.

    Det är också viktigt att komma ihåg att det finns ett stort mörkertal. Alla
    som har/har haft Covid har inte testat sig. Alltså kommer datan vi har inte
    vara absolut sann. Istället är datan vi har de RAPPORTERADE fallen.
'''

complete_df = pd.read_csv('owid-covid-data.csv', parse_dates=['date']) #läser in all data
country = "SWE" #ange iso-koden för det land du vill plotta
df = complete_df[complete_df['iso_code'] == country] #spara enbart de rader med Sverige-data
df = df[df['total_cases'] >= 1] #spara enbart de rader som faktiskt innehåller data om covid-19 fall
df = df.reset_index() #snyggar till vår data frame (=tabell med data)

''' Vår SIR-model där vi kan applya restriktioner, lik filen SIR_restrictions.py.
    Notera: nu räknar modellen ut ANTAL (S, I, R), istället för ANDEL (s, i r)
'''
def model(z,t, b, restrictionsApplied, daysOfRestriction, startDay, b0, b_min): #ta in b som parameter!
    S = z[0]
    I = z[1]
    R = z[2]
    k = 0.125 #=1/8 k=1/D där D är antal dagar en person är infekterad i snitt
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
            b= b0* exp(- n * t1) + (1 - exp(- n * t1)) * b_min #b kommer gå mjukt från b0 till b_min
            #****slut på block****
        if t>=startDay+daysOfRestriction:
            #^^^^början på block^^^
            ''' När restriktionerna är slut så kommer b gå från b_min tillbaka
                till b_0 med en 'mjuk' övergång. Ju större n är, desto snabbare
                sker övergången!
            '''
            t2 = t - startDay - daysOfRestriction
            b= b_min* exp(- n * t2) + (1 - exp(- n * t2)) * b0 #b kommer gå mjukt från b_min till b0
            #^^^^slut på block^^^^
        #~~~~slut på block~~~~
    dSdt = -b*S*I/N
    dIdt = b*S*I/N-k*I
    dRdt = k*I
    dzdt = [dSdt,dIdt, dRdt]
    return dzdt


N = 10327589 #Sveriges befolkningsmängd, tagen härifrån: https://www.scb.se/hitta-statistik/sverige-i-siffror/manniskorna-i-sverige/sveriges-befolkning/
#begynnelsevillkor, S(0)=N-1, I(0)=q, R(0)
z0 = [N-1,1,0]

#antal tidpunkter (dagar) vi vill lösa differentialakvationen för
number_of_days = len(df.index) #så många dagar vi har covid-19 data för

#skapar en lista med tidpunkterna [0, 1, 2, 3, ..., number_of_days-1]
t = np.linspace(0,number_of_days-1,number_of_days)

#löser SIR-modellen
b1 = 0.31 #=0.125 #b=R0*k R≈2.5, k≈1/8=0.125 ==> b≈2.5*0.125≈0.31
b_min = 0.07
solution1 = odeint(model, z0, t, args=(b1, True, 150, 60, b1, b_min)) #med restriktioner
solution2 = odeint(model, z0, t, args=(b1, False, 150, 60, b1, b_min)) #utan restriktioner
''' solution innehåller lösningarna till alla tre: S(t), I(t) & R(t). solution
    är en lista av längd n=365. Varje element i denna lista ger lösningen av
    differentialekvationerna vid varje tidpunkt. Vart och ett av dessa element
    är i sin tur en lista av längd 3, på formen [S(t_j), I(t_j), R(t_j)] där
    t_j är en specifik tidpunkt (exempelvis dag 73). Alltså;
    solution = [[S(0), I(0), R(0)], [S(1), I(1), R(1)], ... ]
'''
#solution 1
solution1_r = solution1[:, 2]
solution1_i = solution1[:, 1]
solution1_r_plus_i = solution1_r + solution1_i
ri_solution1 = solution1_r_plus_i.tolist()
#print(ri_solution1)
df['theoretical_cases1'] = ri_solution1

#solution 2
solution2_r = solution2[:, 2]
solution2_i = solution2[:, 1]
solution2_r_plus_i = solution2_r + solution2_i
ri_solution2 = solution2_r_plus_i.tolist()
#print(ri_solution2)
df['theoretical_cases2'] = ri_solution2

#print(df)

#plotta all data
ax = plt.gca()
df.plot(kind='line', x='date', y='theoretical_cases1', ax=ax, color='orange', label = 'Teoretiskt antal fall, scenario 1')
df.plot(kind='line', x='date', y='theoretical_cases2', ax=ax, color='purple', label = 'Teoretiskt antal fall, scenario 2')
df.plot(kind='line', x='date', y='total_cases', ax=ax, color='pink', figsize=(10,7), label="Totalt antal rapporterade fall")

plt.legend(loc='best') #väljer den 'bästa' platsen för linjebeskrivningarna
plt.ylabel("Antal")
plt.xlabel("Datum")
plt.ylim(bottom=0) #låt y-axeln börja på noll
#plt.savefig("SwedenCovidRealAndTheoretical.png")
plt.show()
