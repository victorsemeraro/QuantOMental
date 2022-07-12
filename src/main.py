from Helpers import get_fundamentals_screener
from TickerSymbols import get_ticker_symbols
from Mongo.Mongo import get_mongo_connection, fetch_mongo

if __name__ == "__main__":

    def main():

        # Read Ticker Symbols
        tickers = get_ticker_symbols()

        # Connect to MongoDB
        mongo_client = get_mongo_connection()

        # Run the Screener 
        # get_fundamentals_screener(mongo_client, tickers)

        for i in range(len(tickers)):

            # Fetch MongoDB Documents
            F = fetch_mongo(mongo_client, tickers[i][0])

    # Call Main... duh
    main()

