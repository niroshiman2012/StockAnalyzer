# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : A WIP code to analyze stocks
#          Visit alphavantage.com to get your stock api key and refer to the documentation to extract any data they provide
#          Visit newsapi.org to get your news api key and refer to the documentation for further info on their data
#          All your login details/ api keys should go into the myModule sheet
# BRANCH : 02


import requests

from myModule import login_details # importing login details needed for API and Email services
from myNews import get_news # importing function that can get stock related news
from myStockInfo import get_stock_overview, get_stock_incomeStatement, get_stock_cashFlow, get_stock_balanceSheet, get_stock_data
from myAlert import send_email


# Creating a stock class
class Stock:
    def __init__(self, symbol, lastPrice, d1_gain):
        self.symbol = symbol
        self.lastPrice = lastPrice
        self.d1_gain = d1_gain


## Testing Code Below
print(get_stock_data("TSLA")) # stock_data assumes a dictionary


