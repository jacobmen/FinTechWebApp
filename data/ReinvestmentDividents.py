import pandas as pd

def getDividends(dividend, payInterval, cRatio, irRate, stockLength):
    return createTimeline(divident,payInterval, cRatio, irRate, stockLength)

print(getDividends(5,0.5,2,4,10))