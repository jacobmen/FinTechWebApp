import pandas as pd

# function that calculates price of stock when rate of increase
# of dividends changes
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio1 - first growth rate
# param cRatio2 - second growth rate after change
# param length1 - number of years with growth rate cRatio1
# param length2 - number of years with growth rate cRatio2
# param irRate - interest rate
def twoPartDDM(dividend, payInterval, cRatio1, cRatio2, length1, length2, irRate):
    # hold the prices after certain intervals
    totalPrice1 = 0
    totalPrice2 = 0

    rPayInterval = 1 / payInterval
    numPayments1 = int(length1 * rPayInterval)  # the # of payments in interval 1
    numPayments2 = int(length2 * rPayInterval)  # the # of payments in interval 2
    intervalInt = int(payInterval * rPayInterval)  # scaling # payments
    interest = (1 + irRate / 100)  # convert interest from percent to modifier
    commonR1 = (1 + cRatio1 / 100)  # convert common ratio 1 from percent to modifier
    commonR2 = (1 + cRatio2 / 100)  # convert common ratio 2 from percent to modifier

    # the dividend to use for the second price calculation
    dividendAtChange = float(dividend * (commonR1 ** (numPayments1-1)) /
                             (interest ** float(numPayments1 * payInterval)))

    # loop through each payment and calculate the total price in interval 1
    for i in range(0, numPayments1, intervalInt):
        totalPrice1 = totalPrice1 + dividend * (commonR1 ** i) / (interest ** float((i+1) * payInterval))

    # loop through each payment and calculate the total price in interval 2
    for j in range(0, numPayments2,intervalInt):
        totalPrice2 = totalPrice2 + dividendAtChange * (commonR2 ** (j+1))/(interest ** float((j+1) * payInterval))
    return round(totalPrice1 + totalPrice2,2)

print(twoPartDDM(5,0.5,2,5,2,2,4))

# function that calculates price of stock when interest rate
# changes during the duration of stock payments
# param dividend - initial dividend value
# param payInterval - time between payments, in years
# param cRatio1 - common ratio as a percent
# param irRate1 - interest rate for first time interval, as a percent
# param irRate2 - interest rate for second time interval, as a percent
# param length1 - number of years with first interest rate
# param length2 - number of years with second interest rate
def twoPartIR(dividend, payInterval, cRatio, irRate1, irRate2, length1, length2):
    # hold the prices after certain intervals
    totalPrice1 = 0
    totalPrice2 = 0

    rPayInterval = 1 / payInterval
    numPayments1 = int(length1 * rPayInterval)  # the # of payments in interval 1
    numPayments2 = int(length2 * rPayInterval)  # the # of payments in interval 2
    intervalInt = int(payInterval * rPayInterval)  # scaling # payments
    interest1 = (1 + irRate1 / 100)  # convert interest rate 1 from percent to modifier
    interest2 = (1 + irRate2 / 100)  # convert interest rate 2 from percent to modifier
    commonR = (1 + cRatio / 100)  # convert common ratio from percent to modifier

    # the dividend to use for the second price calculation
    dividendAtChange = float(dividend * (commonR ** (numPayments1-1)) /
                             (interest1 ** float(numPayments1 * payInterval)))

    # loop through each payment and calculate the total price in interval 1
    for i in range(0, numPayments1, intervalInt):
        totalPrice1 = totalPrice1 + dividend * (commonR ** i) / (interest1 ** float((i+1) * payInterval))

    # loop through each payment and calculate the total price in interval 2
    for j in range(0, numPayments2,intervalInt):
        totalPrice2 = totalPrice2 + dividendAtChange * (commonR ** (j+1))/(interest2 ** float((j+1) * payInterval))
    return round(totalPrice1 + totalPrice2,2)
print(twoPartIR(5,1,5,2,5,2,2))