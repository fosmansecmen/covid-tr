# create the initial .csv file
# check the country code and initial date
import requests
from datetime import timedelta, date
import pandas as pd

country_code = 'TUR'                # for the country codes, check https://covid-api.com/api/

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 3, 11)      # depends on the country, check https://covid-api.com/api/
end_date = date.today()

dates = []
confirmed = []
for single_date in daterange(start_date, end_date):
    day = single_date.strftime("%Y-%m-%d")
    dates.append(day)
    link = 'https://covid-api.com/api/reports?date=' + day + '&iso=' + country_code
    confirmed_cases = requests.get(link).json().get('data')[0].get('confirmed')
    confirmed.append(confirmed_cases)
    
data = {'dates': dates, 'confirmed': confirmed}
df = pd.DataFrame(data)
df.to_csv(path_or_buf='data.csv', index=False) 
