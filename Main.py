### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 1

import pprint
import yfinance as yf


tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
days = 10

stock_data = {}
for ticker in tickers:
    ticker = yf.Ticker(ticker)
    print(ticker.history(period=f"{days}d"))
    stock_data[ticker] = hist["Close"].tolist()

pprint.pprint(stock_data)