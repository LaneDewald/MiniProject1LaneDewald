### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("Charts", exist_ok=True)

tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]


stock_data = {}
for ticker in tickers:
    ticker_obj = yf.Ticker(ticker)
    hist = (ticker_obj.history(period="10d"))
    stock_data[ticker] = hist["Close"].tolist()
    myarray = np.array(stock_data)


for ticker, prices in stock_data.items():
    plt.figure()
    plt.plot(prices, label=ticker)
    plt.xlabel("Days")
    plt.ylabel("Closing Price (USD)")
    plt.grid()
    plt.title(f"Stock Prices for {ticker} Over Last 10 Days")
    plt.legend()
    plt.show()
    plt.savefig(f"Charts/{ticker}.png")
