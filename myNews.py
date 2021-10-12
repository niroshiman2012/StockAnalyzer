# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This is a function that searches for stock related news
#          Documentation can be found at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

import requests
from myModule import login_details

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