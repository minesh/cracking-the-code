import unittest
from stocks import getBestBuySellTime

class TestStocks(unittest.TestCase):

    def test_DontBuy(self):
        buy, sell = getBestBuySellTime([3,2,1])
        self.assertEqual(buy, 1)
        self.assertEqual(sell, 3)

    def test_Buy1Sell8(self):
        buy, sell = getBestBuySellTime([1,2,3,5,2,8,7])
        self.assertEqual(buy, 1)
        self.assertEqual(sell, 8)

if __name__ == '__main__':
    unittest.main()
