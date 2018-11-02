# Market-Indicators
This project implements 3 Market indicators using Python programming language. This project was made for university subject "Practical Investment".

## 1) Moving Average Convergence Divergence (MACD)

### How to understand this indicator
1. Crossovers - As shown in the chart above, when the MACD falls below the signal line, it is a bearish signal, which indicates that it may be time to sell. Conversely, when the MACD rises above the signal line, the indicator gives a bullish signal, which suggests that the price of the asset is likely to experience upward momentum. Many traders wait for a confirmed cross above the signal line before entering into a position to avoid getting "faked out" or entering into a position too early, as shown by the first arrow.

2. Divergence - When the security price diverges from the MACD, it signals the end of the current trend. For example, a stock price that is rising and a MACD indicator that is falling could mean that the rally is about to end. Conversely, if a stock price is falling and the MACD is rising, it could mean that a bullish reversal could occur in the near-term. Traders often use divergence in conjunction with other technical indicators to find opportunities.

3. Dramatic Rise - When the MACD rises dramatically - that is, the shorter moving average pulls away from the longer-term moving average - it is a signal that the security is overbought and will soon return to normal levels. Traders will often combine this analysis with the Relative Strength Index (RSI) or other technical indicators to verify overbought or oversold conditions.

Traders also watch for a move above or below the zero line because this signals the position of the short-term average relative to the long-term average. When the MACD is above zero, the short-term average is above the long-term average, which signals upward momentum. The opposite is true when the MACD is below zero. As you can see from the chart above, the zero line often acts as an area of support and resistance for the indicator.

Read more: Moving Average Convergence Divergence (MACD) https://www.investopedia.com/terms/m/macd.asp#ixzz5VfwX1yUA

### Screenshot
![macd example](https://user-images.githubusercontent.com/24693129/47898112-22bead80-de7d-11e8-9afe-9964d379cc9b.png)

## 2) AROON (AR) 

### How to understand this indicator
If the Aroon-Up crosses above the Aroon-Down, then a new uptrend may start soon. Conversely, if Aroon-Down crosses above the Aroon-Up, then a new downtrend may start soon.
When Aroon-Up reaches 100, a new uptrend may have begun. If it remains persistently between 70 and 100, and the Aroon-Down remains between 0 and 30, then a new uptrend is underway.

### Screenshot
![ar example](https://user-images.githubusercontent.com/24693129/47898110-22bead80-de7d-11e8-8eae-dae8ba9c7167.png)

### 3) Relative Strength Index (RSI)

### How to understand this indicator
Wilder recommended using 70 and 30 as overbought and oversold levels respectively. Generally, if the RSI rises above 30 it is considered bullish for the underlying stock. Conversely, if the RSI falls below 70, it is a bearish signal. Some traders identify the long-term trend and then use extreme readings for entry points. If the long-term trend is bullish, then oversold readings could mark potential entry points.

### Screenshot
![rsi example](https://user-images.githubusercontent.com/24693129/47898111-22bead80-de7d-11e8-882c-af80ef14cfe2.png)

## Data comaparison with TradeStation 
Buy TradeStation here: https://www.tradestation.com/

The screenshot bellow shows the same indicator values from TradeStation
![data from tradestation](https://user-images.githubusercontent.com/24693129/47899325-dd50af00-de81-11e8-90eb-62562983c4e4.png)
