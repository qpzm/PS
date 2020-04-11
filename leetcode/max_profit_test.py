import unittest
from max_profit import maxProfit

class MaxProfitTest(unittest.TestCase):
    def test1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(maxProfit(prices), 7)

    def test2(self):
        prices = [0,2,1,5,7,3,2,6,8]
        self.assertEqual(maxProfit(prices), 14)

    def test3(self):
        prices = [7,6,4,3,1]
        self.assertEqual(maxProfit(prices), 0)

    def test_wrong(self):
        prices = [2,4,1]
        self.assertEqual(maxProfit(prices), 2)

if __name__ == '__main__':
    unittest.main()
