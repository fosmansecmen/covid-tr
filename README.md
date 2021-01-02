# Covid-tr
Covid-19 Stats for Turkey

A simple machine-learning trial with the Covid-19 data for Turkey.

It gathers the data from https://covid-api.com/api.

The last 20 days' data is used to guess the next day's case number.

## Running on a Virtualenv (recommended)
1. First create a virtualenv
    `python3 -m venv env`
2. Activate it
    `source env/Scripts/active`
3. Install required packages
    `pip3 install -r requirements.txt`
4. Run the program
    `python guess.py`

## Running with Docker
Make sure you have docker installed and that the Docker daemon is running.
- `docker build -t covid-tr .`
- `docker run -it -p 5000:5000 covid-tr`

### Restrictions
Requires python3+ and pip3+