''' Detta script visar ett exempel på hur en kan plotta riktig data från Covid-19.
    Notera att detta bara är ett exempel - massa andra saker kan göras!
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


''' Vi läser in all Covid-data. complete_df är en tabell med massor av data.
    Denna data kommer härifrån: https://github.com/owid/covid-19-data/tree/master/public/data.
    När du plottar själv, se till så att du har laddat ned filen owid-covid-data.csv.
'''
complete_df = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])
''' Alla kolumner i denna tabell är:

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


country = "SWE" #ange iso-koden för det land du vill plotta
df = complete_df[complete_df['iso_code'] == country]
ax = plt.gca()

#om du EXEMPELVIS vill plotta totala antalet dödsfall och insjuknade:
df.plot(kind='line', x='date', y='total_deaths', ax=ax)
df.plot(kind='line', x='date', y='total_cases', ax=ax, figsize=(10,7))
plt.ylabel("Antal")
plt.xlabel("Datum")
plt.savefig("SwedenCovid.png")
plt.show()
