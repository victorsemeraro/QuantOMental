import time 

from Tradier.Data import get_fundamentals 

def get_fundamentals_screener(mongo_client, tickers):
    """
    Input:

    1. None

    Output: 
    
    1. Returns the results of a wide market screen grabbing financial metrics
    """

    # Connect to Database
    db = mongo_client["QuantEquity"]

    # Iterate Thru Each Ticker
    for i in range(len(tickers)):

        # Log Ticker Symbol
        ticker_symbol = tickers[i]
        print("Ticker Symbol: ", ticker_symbol)

        # Fetch Financial Metrics
        F = get_fundamentals(ticker_symbol)

        # Fetch Collection
        coll = db[tickers[i][0]]

        dict = { 
            "book_value": F.book_value[0], 
            "shiller_ratio": F.shiller_ratio[0],
            "price_book": F.price_book[0],
            "price_earnings": F.price_earnings[0],
            "price_sales": F.price_sales[0], 
            }

        resp = coll.insert_one(dict)
        print(resp)

        # Limit Api Calls
        time.sleep(2)

    return 0