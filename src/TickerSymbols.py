import pandas as pd

def get_ticker_symbols():
    """
    Read Tickers Symbols CSV and convert to Numpy Array
    """

    df = pd.read_csv('StockTickers.csv')
    ticker_array = df.to_numpy()

    return ticker_array
