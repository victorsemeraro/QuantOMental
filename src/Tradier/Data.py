import requests

api_key = "rOugtXPJmfhLcf5XarlI3Ox8JYis"

def get_fundamentals(ticker_symbol):
    """
    The Method Returns Fundamental Data related to the ticker symbol

    Input: 

    The ticker symbol, i.e. AAPL
    """

    response = requests.get('https://api.tradier.com/beta/markets/fundamentals/ratios',
        params={'symbols': ticker_symbol},
        headers={'Authorization': 'Bearer ' + api_key, 'Accept': 'application/json'}
    )

    json_response = response.json()

    print(response.status_code)
    print(json_response)
    ebitda = json_response[0]["results"][0]["tables"]["operation_ratios_restate"][0]["period_1y"]["e_b_i_t_d_a_margin"]
    print("Response: ", ebitda)

    return ebitda



