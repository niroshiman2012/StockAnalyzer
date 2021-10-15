# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This module contains all the tests pertaining to Technical Analysis using pulled data
#          Documentation at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

from datetime import date, timedelta

from myStockInfo import get_stock_overview, get_stock_incomeStatement, \
    get_stock_cashFlow, get_stock_balanceSheet, \
    get_stock_dailyPrice, get_stock_EMA, get_stock_RSI, \
    get_stock_WMA

# Dates of yesterday and day before that
yesterday = date.today() - timedelta(days=2)
yyesterday = date.today() - timedelta(days=3)


# TEST 01 : Daily Price
def test01_dailyPrice(TICKER, point):

    # E.g.:
    # "2021-10-11": {
    #     "1. open": "787.6500",
    #     "2. high": "801.2400",
    #     "3. low": "785.5000",
    #     "4. close": "791.9400",
    #     "5. volume": "14200322",
    # }

    dailyPriceData = get_stock_dailyPrice(TICKER)

    ydata = dailyPriceData["Time Series (Daily)"][str(yesterday)]
    yydata = dailyPriceData["Time Series (Daily)"][str(yyesterday)]

    yclose = float(ydata["4. close"])
    yyclose = float(yydata["4. close"])

    print("Last Price: " + str(yclose))

    yvol = float(ydata["5. volume"])
    yyvol = float(yydata["5. volume"])

    gainPercent = 100 * (yclose - yyclose) / yclose
    volChange = yvol - yyvol
    print("Gain Percent: " + str(round(gainPercent,2)))
    print("Vol Change: " + str(volChange))

    if (gainPercent > 5.0) and volChange > 0:
        point += 1

    return yclose, point  # returns a tuple


# TEST 02 : EMA
def test02_EMA(TICKER, point, yclose):
    EMA20 = get_stock_EMA(TICKER,"20")["Technical Analysis: EMA"] # EMA20
    EMA50 = get_stock_EMA(TICKER, "50")["Technical Analysis: EMA"] # EMA50
    EMA200 = get_stock_EMA(TICKER, "200")["Technical Analysis: EMA"] # EMA200

    yEMA20 = float(EMA20[str(yesterday)]["EMA"])
    yEMA50 = float(EMA50[str(yesterday)]["EMA"])
    yEMA200 = float(EMA200[str(yesterday)]["EMA"])

    # Check for Golden Cross using short term and mid term EMA
    if yEMA20 > yEMA50:
        point += 1

    # Check if stock on up trend
    if yclose > yEMA20: # Short-term
        point += 1
        print("EMA20 Check")

    if yclose > yEMA50: # Mid-term
        point += 1
        print("EMA50 Check")

    if yclose > yEMA200: # Long-term
        point += 1
        print("EMA200 Check")

    return point


# TEST 03 : WMA
def test03_WMA(TICKER, point, yclose):

    WMA = get_stock_WMA(TICKER, "20")
    yWMA = float(WMA["Technical Analysis: WMA"][str(yesterday)]["WMA"])

    if yclose > yWMA:
        point += 1
        print("WMA200 Check")

    return point


# TEST04 : MACD


# TEST05 : STOCHASTIC OSCILLATOR


# TEST06 : RSI
def test06_RSI(TICKER, point):

    RSI = get_stock_RSI(TICKER, "14")
    print(RSI)
    yRSI = float(RSI["Technical Analysis: RSI"][str(yesterday)]["RSI"])

    if yRSI > 65:
        point += 1
        print("RSI Check")

    return point


# TEST07 : MOM


# TEST08 : MFI


# TEST09 : BBANDS
