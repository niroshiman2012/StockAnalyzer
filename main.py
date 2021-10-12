# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This is just a base code that gets you the stock price for your interested stock (TICKER)
#          Visit alphavantage.com to get your stock api key and refer to the documentation to extract any data they provide
#          Visit newsapi.org to get your news api key and refer to the documentation for further info on their data
#          All your login details/ api keys should go into the myModule sheet and not the main script
# BRANCH : 02

import requests
import smtplib

from myModule import login_details # importing login details needed for API and Email services
from myNews import get_news # importing function that can get stock related news


## PART 1: Function that obtains stock info and returns a class
# TODO: introduce an API to extract fundamental data for the stock (DONE)
# TODO: combine the 5 functions below for collecting fundamental data to prevent redundancy
def get_stock_data(TICKER):

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's price data
    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock)
    response.raise_for_status()
    data = response.json()

    # TODO: the dates on which price data is collected should automatically refer to the latest dates
    last_price_d0 = data["Time Series (Daily)"]["2021-10-08"]["4. close"]
    last_price_d1 = data["Time Series (Daily)"]["2021-10-07"]["4. close"]

    price_diff_per = 100 * abs(float(last_price_d0) - float(last_price_d1))/float(last_price_d1)

    news = get_news(TICKER)

    return {
        "symbol" : TICKER,
        "lastPrice" : last_price_d1,
        "d1_gain" : price_diff_per,
        "news" : news
    }


def get_stock_overview(TICKER):
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's fundamental data
    parameters_stock_overview = {
        "function": "OVERVIEW",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock_overview)
    response.raise_for_status()
    data = response.json()

    return data


def get_stock_incomeStatement(TICKER):
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's fundamental data
    parameters_stock_overview = {
        "function": "INCOME_STATEMENT",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock_overview)
    response.raise_for_status()
    data = response.json()

    return data


def get_stock_balanceSheet(TICKER):
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's fundamental data
    parameters_stock_overview = {
        "function": "BALANCE_SHEET",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock_overview)
    response.raise_for_status()
    data = response.json()

    return data


def get_stock_cashFlow(TICKER):
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's fundamental data
    parameters_stock_overview = {
        "function": "CASH_FLOW",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock_overview)
    response.raise_for_status()
    data = response.json()

    return data


## PART 6: Creating a stock class
class Stock:
    def __init__(self, symbol, lastPrice, d1_gain, news):
        self.symbol = symbol
        self.lastPrice = lastPrice
        self.d1_gain = d1_gain
        self.news = news


## Testing Code Below
stock_data = get_stock_data("TSLA") # stock_data assumes a dictionary

# creating a class for that stock using the dictionary above
TSLA = Stock(stock_data["symbol"],stock_data["lastPrice"],stock_data["d1_gain"],stock_data["news"])

print(TSLA.symbol)
print(TSLA.lastPrice)
print(TSLA.d1_gain)
print(TSLA.news)


# ## PART 3: A function to send the related news via email, can edit to send whatever you want
# def send_email():
# #TODO: need to send a meaningful email
#
#     # creating an object from SMTP class, connect to the email provider
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls() # tls secures our connection to the email server, encrypts it
#         connection.login(user=login_details["my_email"], password=login_details["email_password"])
#         connection.sendmail(from_addr=login_details["my_email"], # sender's email
#                             to_addrs=login_details["my_email"], # receiver's email
#                             msg="Subject:Hello\n\nThis is the body"
#                             )
#         # connection.close() - no need to use this when using with, will close automatically
#


## Testing code


