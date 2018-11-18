####
#
# MACD Indicator programming
#
# Author: Lukas Andriejunas
# Date: 2018-10-30
# Email: lukas.andriejunas at gmail dot com
#
####

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # show matplotlib graph window in front of other windows (for macOS)
import matplotlib.pyplot as plt


# define MACD indicator calculation as function

# How to understand this indicator
# 1. Crossovers - As shown in the chart above, when the MACD falls below the signal line, it is a bearish signal,
# which indicates that it may be time to sell. Conversely, when the MACD rises above the signal line,
# the indicator gives a bullish signal, which suggests that the price of the asset is likely to experience upward
# momentum. Many traders wait for a confirmed cross above the signal line before entering into a position to avoid
# getting "faked out" or entering into a position too early, as shown by the first arrow.
#
# 2. Divergence - When the security price diverges from the MACD, it signals the end of the current trend.
# For example, a stock price that is rising and a MACD indicator that is falling could mean that the rally
# is about to end. Conversely, if a stock price is falling and the MACD is rising, it could mean that a
# bullish reversal could occur in the near-term. Traders often use divergence in conjunction with other technical
# indicators to find opportunities.
#
# 3. Dramatic Rise - When the MACD rises dramatically - that is, the shorter moving average pulls away from the
# longer-term moving average - it is a signal that the security is overbought and will soon return to normal levels.
# Traders will often combine this analysis with the Relative Strength Index (RSI) or other technical indicators
# to verify overbought or oversold conditions.
#
# Traders also watch for a move above or below the zero line because this signals the position of the short-term
# average relative to the long-term average. When the MACD is above zero, the short-term average is above the
# long-term average, which signals upward momentum. The opposite is true when the MACD is below zero.
# As you can see from the chart above, the zero line often acts as an area of support and resistance for the indicator.
#
# Read more: Moving Average Convergence Divergence (MACD) https://www.investopedia.com/terms/m/macd.asp#ixzz5VfwX1yUA

def calculate_macd(df, PRICE_NAME, period1, period2, period3): # default MACD period values are: period1 = 26, period2 = 12, period3 = 9.
    EMA_1 = df[PRICE_NAME].ewm(span=period1, adjust=False).mean()
    EMA_2 = df[PRICE_NAME].ewm(span=period2, adjust=False).mean()
    MACD_line = EMA_2 - EMA_1
    MACD_Signal_line = MACD_line.ewm(span=period3, adjust=False).mean()
    MACD_Histogram = MACD_line - MACD_Signal_line
    return MACD_line, MACD_Signal_line, MACD_Histogram



### 1. Data reading from file

DATA_FILE_PATH = "apple.csv"

df = pd.read_csv(DATA_FILE_PATH, sep=',')

TIMESTAMP_NAME = "Date" # timestamp name from .csv
PRICE_NAME = "Close" # define price name that will be used from .csv



### 2. Show historic price data in the first subplot
plt.figure(figsize=(10,5)) # change default figure size
ax1 = plt.subplot(2, 1, 1)
plt.plot(df[TIMESTAMP_NAME], df[PRICE_NAME])
plt.title("NASDAQ: APPL daily MACD")
plt.ylabel("Price, USD")
plt.grid()

frame1 = plt.gca() # hide x axis values
frame1.axes.xaxis.set_ticklabels([])



### 3. Calculate MACD indicator and add it to subplot
MACD_line, MACD_Signal_line, MACD_Histogram = calculate_macd(df, PRICE_NAME, 26, 12, 9) # calculating with the default MACD values

# add data to subplot
ax2 = plt.subplot(2, 1, 2, sharex = ax1)
plt.plot(df[TIMESTAMP_NAME], MACD_line, color = 'blue')
plt.plot(df[TIMESTAMP_NAME], MACD_Signal_line, color = 'red')
plt.bar(df[TIMESTAMP_NAME], MACD_Histogram)
plt.grid()

frame1 = plt.gca() # hide x axis values
frame1.axes.xaxis.set_ticklabels([])



### 4. Show subplot
plt.show()