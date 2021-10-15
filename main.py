# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : A WIP code to analyze stocks
#          Visit alphavantage.com to get your stock api key and refer to the documentation to extract any data they provide
#          Visit newsapi.org to get your news api key and refer to the documentation for further info on their data
#          All your login details/ api keys should go into the myModule sheet
# BRANCH : 02


import requests

from myModule import login_details # importing login details needed for API and Email services
from myNews import get_news # importing function that can get stock related news

from myTA import test01_dailyPrice, test02_EMA, test03_WMA, test06_RSI
from myFA import testFA01, testFA02, testFA03

from myAlert import send_email

from datetime import date, timedelta


## Call the test functions below
TICKER = "TSLA"
point = 0

# FUNDAMENTAL ANALYSIS TESTS
# print(testFA01(TICKER))
# print(testFA02(TICKER))
# print(testFA03(TICKER))

# TECHNICAL ANALYSIS TESTS
# Alpha Vantage limits free API calls frequency to 5 calls / min and 500 calls / day
# yclose, point = test01_dailyPrice(TICKER, point)
#
# point = test02_EMA(TICKER, point, yclose)
#
# point = test03_WMA(TICKER, point, yclose)

# point = test06_RSI(TICKER, point)

# print("Point: " + str(point))






