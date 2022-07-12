from pymongo import MongoClient 
from Object import FinancialMetrics

def get_mongo_connection():

    try: 

        password = "APuXI7kPYRKNhaYA"
        client = MongoClient("mongodb+srv://vicarisiventures:" + password + "@optioncluster.ing0x.mongodb.net/?retryWrites=true&w=majority")

    except:

        print("Error Connecting to MongoDB")
        return 0

    return client 

def fetch_mongo(client, ticker):

    # Database Name
    db = client["QuantEquity"]

    # Collection Name
    coll = db[ticker]

    data = coll.find()

    # Initialize Object
    length = 1
    F = FinancialMetrics(length)

    for d in data:
        F.book_value[0] = d["book_value"]
        F.shiller_ratio[0] = d["shiller_ratio"]
        F.price_book[0] = d["price_book"]
        F.price_earnings[0] = d["price_earnings"]
        F.price_sales[0] = d["price_sales"]

    return F
