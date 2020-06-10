import unittest

from TOP3.coupon_calculations import calculate_order


class MyTestCase(unittest.TestCase):
    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(4, 5, .10), False)

    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(7.50, 5, .15), False)

    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(9, 5, .20), False)

    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(6.55, 10, .10), False)

    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(3.95, 10, .15), False)

    def test_coupon_calculation_under_10(self):
        self.assertEqual(calculate_order(8.92, 10, .20), False)


if __name__ == '__main__':
    unittest.main()
