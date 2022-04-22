#Function that returns the most frequently value in a column
def func_freq(column):
    freq = df[column].value_counts()
    r_freq = 0
    for i, v in freq.items():
        if r_freq < v:
            r_freq = v
            r_launch = i
    return(r_launch)


#Function that returns the sum of flights in a group of years
def years_sum(years):
    freq_years = df["launch_year"].value_counts()
    r_sum = 0
    for n in years:
        for i, v in freq_years.items():
            if(n == i):
                r_sum += v
    return(r_sum)

#Libraries
import requests
import json
import pandas as pd

#Access API and transfer data to dataframe
request = requests.get("https://api.spacexdata.com/v3/launches")
a_json = json.loads(request.content)
df = pd.DataFrame.from_dict(a_json)

#Get year with most flights
r_launch_year = func_freq("launch_year")
#Get site with most flights
r_launch_site = func_freq("launch_site")

#Years group
a_years=[
    "2019","2020","2021"
    ]
#Get sum flights in years
r_years_sum = years_sum(a_years)

#Write answers
data = [
    ["Ano onde houve mais lançamentos:", r_launch_year],
    ["Launch_site onde mais houve lançamentos:", r_launch_site],
    ["Total de lançamentos entre os anos de 2019 – 2021:", r_years_sum]
    ]
# Create dataframe
df2 = pd.DataFrame(data, columns=['Questão', 'Resposta'])
# Write in excel
df2.to_excel("APIdata.xlsx")
