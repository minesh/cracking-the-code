#!/usr/bin/env python
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def getBestBuySellTime(stocks):
    lowest = None
    highest = None
    for i in stocks[::-1]:
        if (lowest == None):
            lowest = i
            highest = i
        elif (i >= highest):
            highest = i
        elif (i < lowest):
            lowest = i

    return lowest, highest

def main():
   buy, sell = getBestBuySellTime(stock_prices_yesterday)
   if (buy != None and sell != None):
       print "Price low %d, high %d" % (buy, sell)
       print "Most money = %d" % (sell - buy)

if __name__ == '__main__':
   main()

