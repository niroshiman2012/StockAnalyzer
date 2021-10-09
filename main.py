# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This is just a base code that gets you the stock price for your interested stock (TICKER)
#          Visit alphavantage.com to get your stock api key and refer to the documentation to extract any data they provide
#          Visit newsapi.org to get your news api key and refer to the documentation for further info on their data
#          All your login details/ api keys should go into the myModule sheet and not the main script
# BRANCH : 01

import requests
import smtplib

from myModule import login_details


## PART 2: Function that searches for related stock news and returns it
# Documentation : https://newsapi.org/docs/endpoints/everything
# TODO: shorten the for loop that extracts news info, maybe by using a list with keys
def get_news(TICKER):

    parameter = {
        "apiKey": login_details["NEWS_API_KEY"],
        "qInTitle": TICKER,
        "from": "2021-09-16",
        "to": "2021-09-30",
        "sortBy": "publishedAt",
        "language": "en",
        # "domains": "theedgemarkets.com"
    }

    response = requests.get("https://newsapi.org/v2/everything?", params=parameter)
    response.raise_for_status()

    data = response.json()

    article_info = {} # creating an emtpy dictionary to store the each news result
    news = [] # info on each news results will be a separate dictionary by itself in this news list
    for article in data['articles']:  # go through each article i.e. each result to extract the below info
        article_info["data"] = article["publishedAt"]
        article_info["source"] = article["source"]["name"]
        article_info["title"] = article["title"]
        article_info["url"] = article["url"]

        # using copy method : https://stackoverflow.com/questions/23724136/appending-a-dictionary-to-a-list-in-a-loop
        #                   : https://beginnersbook.com/2019/03/python-set-copy-method/
        news.append(article_info.copy()) # add the dictionary above to the news list


    article_dict = {} # creating an empty dictionary which will hold all the above dictionaries tagged to respective key
    for i in range(1, len(news)+1): # iterate through the news list which has multiple dictionaries
        article_dict[str(i)] = news[i-1] # take each dictionary and tag it to a number

    return article_dict


## PART 1: Function that obtains stock info and returns a class
# TODO: introduce an API to extract fundamental data for the stock
def get_stock_data(TICKER):

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    # Parameters for stock's price data
    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    # Parameters for stock's fundamental data
    parameters_stock_fdata = {
        "function": "OVERVIEW",
        "symbol": TICKER,
        "apikey": login_details["STOCK_API_KEY"],
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters_stock)
    response.raise_for_status()
    data = response.json()

    # TODO: the dates on which price data is collected should automatically refer to the latest dates
    last_price_d0 = data["Time Series (Daily)"]["2021-09-30"]["4. close"]
    last_price_d1 = data["Time Series (Daily)"]["2021-09-29"]["4. close"]

    price_diff_per = 100 * abs(float(last_price_d0) - float(last_price_d1))/float(last_price_d1)

    news = get_news(TICKER)

    return {
        "symbol" : TICKER,
        "lastPrice" : last_price_d1,
        "d1_gain" : price_diff_per,
        "news" : news
    }


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











