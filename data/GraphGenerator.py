#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:10:01 2020

@author: matthewjalnos
"""
import matplotlib.pyplot as plt
import pandas as pd

# function to return the stock price at the end of a time period
# given all determining parameters
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def stockprice(dividend, payInterval, cRatio, irRate, stockLength):
    #variable to hold the price of the stock
    totalPrice = 0
    intervalInt = 1  # scaling # payments

    rPayInterval = 1 / float(payInterval)
    numPayments = int(float(stockLength) * rPayInterval)  # the # of payments
    interest = (1 + float(irRate) / 100)  # convert interest from percent to modifier
    commonR = (1 + float(cRatio) / 100)  # convert common ratio from percent to modifier

    # loop through each payment and add the total price
    for i in range(1, numPayments+1, intervalInt):
        totalPrice = totalPrice + float(dividend) * (commonR ** (i-1) / (interest ** float(i*float(payInterval))))

    # return rounded price
    return (dividend)
    return round(totalPrice, 2)


print(stockprice(5, 0.5, 2, 4, 10))

# function to print the graph of price vs interest ratio
# when holding the other params constant
# param lowerIR - the lowest interest rate to be calculated (percent)
# param upperIR - the highest interest rate to be calculated (percent)
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphIR(lowerIR, upperIR, dividend, payInterval, commonRatio, stockLength):
    # loop through all potential interest rates (0-100) and plot the values
    
    for i in range(lowerIR, upperIR+1, 1):
        graphValue = stockprice(dividend, payInterval, commonRatio, i, stockLength)
        #graphValue = stockprice(10, , 105, i, 10)
        plt.plot(i, graphValue,'-o')  # x-axis, then y-axisplt.xlabel('Interest Rate (percent)')  # labels x-axis
    plt.ylabel('Price (dollars)')  # labels y-axis
    plt.title(' Relationship Between Interest Rate and Price')  # title
    return (plt.show())

graphIR(10,50,5, 0.5, 2, 10)

# function to print the graph of Price vs Dividend
# when holding the other params constant
# param lowerDiv - lowest dividend to be calculated
# param upperDiv - highest dividend to be calculated
# param payInterval - time between payments, in years
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphDividend(lowerDiv,upperDiv, payInterval, commonRatio, irRate, stockLength):
    # loop through each dividend (0-upperDiv) and plot the values
    for i in range(lowerDiv, upperDiv+1, 1):
        graphValue = stockprice(i, payInterval, commonRatio, irRate, stockLength)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
    plt.xlabel('Initial Dividend Value (dollars)')  # labels x-axis
    plt.ylabel('Price (dollars)')  # labels y-axis
    plt.title(' Relationship Between Initial Dividend Value and Price')  # title
    plt.xticks(range(lowerDiv, upperDiv + 1))
    return (plt.show())

#graphDividend(70,100,0.5,2,4,10)

# function to print the graph of Price vs Pay Interval
# when holding the other params constant
# param lowerInt - shortest pay duration to be calculated
# param upperInt - longest pay duration to be calculated
# param dividend - initial dividend value
# param commonRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphInterval(lowerInterval,upperInterval, dividend, commonRatio, irRate, stockLength):
    # converts the pay interval to smaller chunks to loop through
    # DO NOT INCREASE THIS VALUE ABOVE 24 OR THE CODE BREAKS
    conversionMult = 100
    upperInter = int(upperInterval * conversionMult)+1
    lowerInter = int(lowerInterval * conversionMult)
    # loop through all potential intervals (1-upperInt) and plot the values
    for i in range(lowerInter, upperInter+1, 1):
        convertedInt = float(i/conversionMult)
        graphValue = stockprice(dividend, convertedInt, commonRatio, irRate, stockLength)
        plt.plot(convertedInt, graphValue, '-o')  # x-axis, then y-axis
    plt.xlabel('Time Between Dividends (years)')  # labels x-axis
    plt.ylabel('Price (dollars)')  # labels y-axis
    plt.title(' Relationship Between Pay Period and Price')  # title
    #plt.xticks(range(lowerInter, upperInter + 1))
    return (plt.show())

#graphInterval(0.10,0.55,5,2,4,10)

# function to print the graph of Price vs Common Ratio
# when holding the other params constant
# param lowerCR - the lowest pay ratio to be calculated
# param upperCR - the highest pay ratio to be calculated
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold on the stock
def graphCommonRatio(lowerCR,upperCR, dividend, payInterval, irRate, stockLength):

    # loop through each dividend (0-upperCR) and plot the valued
    for i in range(lowerCR, upperCR+1, 1):
        graphValue = stockprice(dividend, payInterval, i, irRate, stockLength)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
    plt.xlabel('Common Ratio')  # labels x-axis
    plt.ylabel('Price (dollars)')  # labels y-axis
    plt.title(' Relationship Between Common Ratio and Price')  # title
    #plt.xticks(range(lowerCR, upperCR + 1))
    return (plt.show())

#graphCommonRatio(-40,4,500,0.5,4,10)

# function to print the graph of Price vs Stock Length
# when holding the other params constant
# param lowerSL - the shortest stock duration to be calculated
# param upperSL - the longest stock duration to be calculated
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
def graphStockLength(lowerSL,upperSL, dividend, payInterval, cRatio, irRate):
    # loop through each dividend (0-upperSL) and plot the valued
    for i in range(lowerSL, upperSL+1, 1):
        graphValue = stockprice(dividend, payInterval, cRatio, irRate, i)
        plt.plot(i, graphValue, '-o')  # x-axis, then y-axis
    plt.xlabel('Length of Stock (years)')  # labels x-axis
    plt.ylabel('Price (dollars)')  # labels y-axis
    plt.title(' Relationship Between Length of Stock and Price')  # title
    return (plt.show())

#graphStockLength(90,100,5,0.5,2,4)
