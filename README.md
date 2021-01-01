# Covid-tr
Covid-19 Stats for Turkey

A simple machine-learning trial with the Covid-19 data for Turkey.

It gathers the data from https://covid-api.com/api.

The last 15 days' data is used to guess the next day's case number.

## Usage
`docker build -t covid-tr .`
`docker run -it -p 5000:5000 covid-tr`

### Restrictions
Requires python3+ and pip3+