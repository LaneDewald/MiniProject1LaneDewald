### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 1

import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]


stock_data = {}
for ticker in tickers:
    ticker = yf.Ticker(ticker)
    hist = (ticker.history(period="10d"))
    stock_data[ticker] = hist["Close"].tolist()
    myarray = np.array(stock_data)


for ticker, prices in stock_data.items():
    plt.figure()  # Create a new figure for each graph
    plt.plot(prices, label=ticker)
    plt.xlabel("Days")
    plt.ylabel("Closing Price (USD)")
    plt.title(f"Stock Prices for {ticker} Over Last 10 Days")  # Specific title for each ticker
    plt.legend()
    plt.show()

