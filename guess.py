import sys, requests
from datetime import timedelta, date, datetime as dt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_recent_data(country_code):
    last_day_number = 15            # the number of days to take as reference, recommended 15 days as it is more realistic for Covid-19
    
    end_date = date.today()
    start_date = (end_date - timedelta(days=last_day_number))

    print("---\nLast 15 days' stats:")
    confirmed = []
    for single_date in daterange(start_date, end_date):
        day = single_date.strftime("%Y-%m-%d")
        print('date: ', day)
        link = 'https://covid-api.com/api/reports?date=' + day + '&iso=' + country_code
        # check the COVID-API: returns the total number of cases
        # get data and parse the total confirmed cases
        confirmed_cases = requests.get(link).json().get('data')[0].get('confirmed')
        print('total cases: {}'.format(confirmed_cases))
        if confirmed:
            new_cases = confirmed_cases - confirmed[-1:][0]     # subtract to find the new cases
            print('new cases: {}'.format(new_cases))
        
        confirmed.append(confirmed_cases)

    # return data
    return confirmed

def train_and_predict(data):
    x_axis = [i for i in range(len(data))] 
    y_axis = data
    index = x_axis[-1:][0]
    # print(x_axis, y_axis)
    mymodel = np.poly1d(np.polyfit(x_axis, y_axis, 3))
    print('---\ncorrelation: ', r2_score(y_axis, mymodel(x_axis)))
    guess = mymodel(index+1)
    print('my guess for tomorrow: {} \nnew cases: {}'.format(guess, guess-y_axis[-1:][0]))


if __name__ == '__main__':
    country_code = 'TUR'
    data = get_recent_data(country_code)
    train_and_predict(data)