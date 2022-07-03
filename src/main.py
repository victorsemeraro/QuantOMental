import time 

from Tradier.Data import get_fundamentals 
from TickerSymbols import get_ticker_symbols

if __name__ == "__main__":

    def main():

        tickers = get_ticker_symbols()

        for i in range(len(tickers)):

            ticker_symbol = tickers[i]
            print(ticker_symbol)
            get_fundamentals(ticker_symbol)

            time.sleep(2)

    # Call Main... duh
    main()

