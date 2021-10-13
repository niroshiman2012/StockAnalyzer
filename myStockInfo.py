# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This is a function that searches for stock info related to the stock's background, financial statements,
#          stock price and etc
#          Documentation at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

import requests
from myModule import login_details

# Get the overview of the particular stock
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


# Gets income statement of the stock
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


# Gets the balance sheet of the stock
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


# Gets the cash flow statement of stock
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


def get_stock_dailyPrice(TICKER):

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

    return data


def get_stock_EMA(TICKER,TIME_PERIOD):

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's price data
    parameters_stock = {
        "function": "EMA",
        "symbol": TICKER,
        "interval": "daily",
        "time_period": TIME_PERIOD,
        "series_type": "close",
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock)
    response.raise_for_status()
    data = response.json()

    return data