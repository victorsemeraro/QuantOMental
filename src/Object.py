import numpy as np

from numba import float64
from numba.experimental import jitclass

spec = [
    ('book_value', float64[:]),
    ('shiller_ratio', float64[:]),
    ('price_book', float64[:]),
    ('price_earnings', float64[:]),
    ('price_sales', float64[:])
]

@jitclass(spec)
class FinancialMetrics():
    """
    Object Wraps All Financial Metrics 
    """

    def __init__(self, length):

        self.book_value = np.zeros(length, dtype = np.float64)
        self.shiller_ratio = np.zeros(length, dtype = np.float64)
        self.price_book = np.zeros(length, dtype = np.float64)
        self.price_earnings = np.zeros(length, dtype = np.float64)
        self.price_sales = np.zeros(length, dtype = np.float64)


