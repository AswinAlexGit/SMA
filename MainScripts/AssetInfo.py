import yfinance as yf

def AI(asset):

    stock_info = yf.Ticker(asset).info
    # stock_info.keys() for other properties you can explore

    # print(stock_info.keys())
    try:
        aname = stock_info['longName']
        market_price = stock_info['regularMarketPrice']
        previous_close_price = stock_info['regularMarketPreviousClose']
        # print('market price ', market_price)
        # print('previous close price ', previous_close_price)
        return [aname, market_price, previous_close_price]

    except:
        return []
