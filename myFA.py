# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This module contains all the tests pertaining to Fundamental Analysis using pulled data
#          Documentation at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

from myStockInfo import get_stock_incomeStatement, get_stock_balanceSheet, get_stock_cashFlow

def testFA01(TICKER):

    data = get_stock_incomeStatement(TICKER)

    return data


def testFA02(TICKER):

    data = get_stock_balanceSheet(TICKER)

    return data

def testFA03(TICKER):

    data = get_stock_cashFlow(TICKER)

    return data