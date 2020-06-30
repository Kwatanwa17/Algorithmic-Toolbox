import unittest
from money_change import money_change


class TestSumOfTwoDigits(unittest.TestCase):
    def test(self):
        for (money, number_of_coins) in [(1, 1), (2, 2), (28, 6), (25, 3), (101, 11)]:
            self.assertEqual(money_change(money), number_of_coins)


if __name__ == '__main__':
    unittest.main()
