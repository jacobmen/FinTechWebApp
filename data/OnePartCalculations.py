import matplotlib.pyplot as plt
import pandas as pd

# function that calculates the stock price
# if dividend payments continue forever
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - commonRatio as a percent
# param irRate - interest rate as a percent
def perpetuity(dividend, payInterval, cRatio, irRate):
    # calculates denominator for perpetuity
    interest = (1 + irRate/100)**payInterval
    commonRatio = 1 + cRatio/100
    denom = 1-commonRatio/interest

    # Return whether the value will converge as time goes on
    # Converges if (denom > 0), infinite if (denom < 0)
    if (denom<0):
        returnVal = 'infinite value' #checks that price of stock is finite
    else:
        returnVal = round((dividend/interest)/denom,2)
    return returnVal

print(perpetuity(5,0.5,2,4))
print(perpetuity(5,0.5,2,5))

# function to generate a timeline of dividend payments
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio - common ratio as a percent
# param irRate - interest rate as a percent
# param stockLength - the duration of the hold of the stock
def createTimeline(dividend, payInterval, cRatio, irRate, stockLength):
    # create lists to store data values
    dates = [0] * int(stockLength/payInterval) #instantiates list with number of dividends plus 1
    values = [0] * int(stockLength/payInterval) #instantiates list with number of dividends plus 1

    recipPayInterval = 1 / payInterval
    numPayments = int(stockLength * recipPayInterval) #number of payments
    intervalInt = int(payInterval * recipPayInterval) #scaling number of payments

    # loop through the time intervals and store the values into the lists
    for i in range(0, numPayments, intervalInt):
        dates[i] = (i+1) * payInterval #fills dates list with number of years since first dividend
        values[i] = round(dividend * (1 + cRatio / 100) ** i,2) #fills values list with value of dividend

    # creates data frame, datesValues, to match up date to dividend value
    datesValues = pd.DataFrame({'Years': dates,'Dividend': values})
    return datesValues

print(createTimeline(5, 0.5, 2, 4, 10))

