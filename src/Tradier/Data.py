import requests
from Object import FinancialMetrics

api_key = "rOugtXPJmfhLcf5XarlI3Ox8JYis"

def get_fundamentals(ticker_symbol):
    """
    Method Returns Fundamental Data related to the ticker symbol

    Input: 

    1. The ticker symbol, i.e. AAPL

    Output: 

    1. The Specified Financial Metric
    """
    
    # Initialize Object
    length = 1
    F = FinancialMetrics(length)

    try:

        response = requests.get('https://api.tradier.com/beta/markets/fundamentals/ratios',
        params={'symbols': ticker_symbol},
        headers={'Authorization': 'Bearer ' + api_key, 'Accept': 'application/json'}
        )

        json_response = response.json()

        # print(len(json_response[0]["results"]))
        # print(json_response[0]["results"][1]["tables"]["valuation_ratios"]["p_s_ratio"])

        # Book Value
        try: 
            F.book_value[0] = json_response[0]["results"][1]["tables"]["valuation_ratios"]["book_value_per_share"]
        except:
            F.book_value[0] = 0

        # Shiller Adjusted Earnings
        try:
            F.shiller_ratio[0] = json_response[0]["results"][1]["tables"]["valuation_ratios"]["c_a_p_e_ratio"]
        except:
            F.shiller_ratio[0] = 0

        # Price Book Ratio
        try:
            F.price_book[0] = json_response[0]["results"][1]["tables"]["valuation_ratios"]["p_b_ratio"]
        except: 
            F.price_book[0] = 0

        # Price Earnings Ratio
        try:
            F.price_earnings[0] = json_response[0]["results"][1]["tables"]["valuation_ratios"]["p_e_ratio"]
        except: 
            F.price_earnings[0] = 0

        # Price Sales Ratio
        try:
            F.price_sales[0] = json_response[0]["results"][1]["tables"]["valuation_ratios"]["p_s_ratio"]
        except: 
            F.price_sales[0] = 0

        return F

    except: 

        print("Api Call Has Failed")
        return F






