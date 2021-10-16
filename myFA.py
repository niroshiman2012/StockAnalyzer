# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : This module contains all the tests pertaining to Fundamental Analysis using pulled data
#          Documentation at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

from myStockInfo import get_stock_incomeStatement, get_stock_balanceSheet, get_stock_cashFlow

def testFA01(TICKER):

    data = get_stock_incomeStatement(TICKER)

    return data


def testFA02_BalanceSheet(TICKER,type):

    data = get_stock_balanceSheet(TICKER)

    if type == True:
        # Annual Report
        reports = data["annualReports"]  # returns an array with dictionaries of different fiscal dates
    else:
        # Quarterly Report
        reports = data["quarterlyReports"]  # returns an array with dictionaries of different fiscal dates

    print("Fr. Balance Sheet")
    for report in reports:
        print(report["fiscalDateEnding"])

        # calculate : net working capital
        netWorkingCapital = float(report["totalCurrentAssets"]) - float(report["totalCurrentLiabilities"])
        print(round(netWorkingCapital, 2))

        # calculate : current ratio and quick ratio
        currentRatio = float(report["totalCurrentAssets"]) / float(report["totalCurrentLiabilities"])
        quickRatio = (float(report["totalCurrentAssets"]) - float(report["inventory"])) / float(
            report["totalCurrentLiabilities"])

        print(round(currentRatio, 2))
        print(round(quickRatio, 2))

        # calculate : debt to asset ratio
        debt2Asset = float(report["shortLongTermDebtTotal"]) / float(report["totalAssets"])
        print(round(debt2Asset, 2))
        print("\n")


def testFA03(TICKER):

    data = get_stock_cashFlow(TICKER)

    return data