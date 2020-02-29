#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:10:01 2020

@author: matthewjalnos
"""
import matplotlib.pyplot as plt
import pandas as pd

# function to return the stock price at the end of the time period
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def stockprice(dividend, payInterval, cRatio, irRate, stockLength):
    totalPrice = 0
    rPayInterval = 1 / payInterval
    numPayments = int(stockLength * rPayInterval)  # the # of payments
    intervalInt = int(payInterval * rPayInterval)  # scaling # payments
    interest = (1 + irRate / 100)  # convert interest from percent to modifier
    commonR = (1 + cRatio / 100)  # convert common ratio from percent to modifier
    # loop through each payment and add the total price
    for i in range(0, numPayments+1, intervalInt):
        totalPrice = totalPrice + dividend * (commonR ** i) / (interest ** i)
    return round(totalPrice, 2)


print(stockprice(5, 0.5, 2, 4, 10))


# function to print the graph of price vs interest ratio
# when holding the other params constant
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphIR(dividend, payInterval, commonRatio, stockLength):
    # loop through all potential interest rates (0-100) and plot the values
    for i in range(0, 100, 1):
        graphValue = stockprice(dividend, payInterval, commonRatio, i, stockLength)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
        plt.xlabel('Interest Rate (percent)')  # labels x-axis
        plt.ylabel('Price (dollars)')  # labels y-axis
        plt.title(' Relationship Between Interest Rate and Price')  # title
    return (plt.show())

graphIR(5, 0.5, 2, 10)

# function to print the graph of Price vs Dividend
# when holding the other params constant
# param upperDiv - max dividend to be calculated
# param payInterval - time between payments, in years
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphDividend(upperDiv, payInterval, commonRatio, irRate, stockLength):
    # loop through each dividend (0-upperDiv) and plot the values
    for i in range(0, upperDiv+1, 1):
        graphValue = stockprice(i, payInterval, commonRatio, irRate, stockLength)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
        plt.xlabel('Initial Dividend Value (dollars)')  # labels x-axis
        plt.ylabel('Price (dollars)')  # labels y-axis
        plt.title(' Relationship Between Initial Dividend Value and Price')  # title
    return (plt.show())

graphDividend(100,0.5,2,4,10)

# function to print the graph of Price vs Pay Interval
# when holding the other params constant
# param upperInt - longest pay duration to be calculated
# param dividend - initial dividend value
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphInterval(upperInt, dividend, commonRatio, irRate, stockLength):
    # converts the pay interval to smaller chunks to loop through
    # DO NOT INCREASE THIS VALUE ABOVE 24 OR THE CODE BREAKS
    conversionMult = 24

    # loop through all potential intervals (1-upperInt) and plot the values
    for i in range(1, upperInt*conversionMult+1, 1):
        convertedInt = i/conversionMult
        graphValue = stockprice(dividend, convertedInt, commonRatio, irRate, stockLength)
        plt.plot(convertedInt, graphValue, '-o')  # x-axis, then y-axis
        plt.xlabel('Time Between Dividends (years)')  # labels x-axis
        plt.ylabel('Price (dollars)')  # labels y-axis
        plt.title(' Relationship Between Pay Period and Price')  # title
    return (plt.show())

graphInterval(1,5,2,4,10)

# function to print the graph of Price vs Common Ratio
# when holding the other params constant
# param upperCR - the highest pay ratio to be calculated
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphCommonRatio(upperCR, dividend, payInterval, irRate, stockLength):
    # loop through each dividend (0-upperCR) and plot the valued
    for i in range(0, upperCR+1, 1):
        graphValue = stockprice(dividend, payInterval, i, irRate, stockLength)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
        plt.xlabel('Common Ratio')  # labels x-axis
        plt.ylabel('Price (dollars)')  # labels y-axis
        plt.title(' Relationship Between Common Ratio and Price')  # title
    return (plt.show())

graphCommonRatio(400,5,0.5,4,10)

# function to print the graph of Price vs Stock Length
# when holding the other params constant
# param upperSL - the highest stock duration to be calculated
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
def graphStockLength(upperSL, dividend, payInterval, cRatio, irRate):
    # loop through each dividend (0-upperSL) and plot the valued
    for i in range(0, upperSL+1, 1):
        graphValue = stockprice(dividend, payInterval, cRatio, irRate, i)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
        plt.xlabel('Length of Stock (years)')  # labels x-axis
        plt.ylabel('Price (dollars)')  # labels y-axis
        plt.title(' Relationship Between Length of Stock and Price')  # title
    return (plt.show())

graphStockLength(100,5,0.5,2,4)

# function to calculate the value of a dividend at a given time
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold of the stock
def createTimeline(dividend, payInterval, cRatio, irRate, stockLength):
    dates = [0] * int(1+stockLength/payInterval) #instantiates list with number of dividends plus 1
    values = [0] * int(1+stockLength/payInterval) #instantiates list with number of dividends plus 1
    recipPayInterval = 1 / payInterval
    numPayments = int(stockLength * recipPayInterval) #number of payments
    intervalInt = int(payInterval * recipPayInterval) #scaling number of payments
    for i in range(0, numPayments+1, intervalInt):
        dates[i] = i * payInterval #fills dates list with number of years since first dividend
        values[i] = round(dividend * (1 + cRatio / 100) ** i,2) #fills values list with value of dividend
    datesValues = pd.DataFrame({'Years Since First Dividend': dates,'Dividend Value': values})
    #creates data frame, datesValues, to match up date to dividend value
    return datesValues


print(createTimeline(5, 0.5, 2, 4, 10))