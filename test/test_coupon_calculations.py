import unittest

from TOP3.coupon_calculations import calculate_order


class MyTestCase(unittest.TestCase):
    def test_coupon_calculation_under_101(self):
        self.assertEqual(calculate_order(4, 5, .10), 9.77)

    def test_coupon_calculation_under_102(self):
        self.assertEqual(calculate_order(7.50, 5, .15), 8.20)

    def test_coupon_calculation_under_103(self):
        self.assertEqual(calculate_order(9, 5, .20), 9.34)

    def test_coupon_calculation_under_104(self):
        self.assertEqual(calculate_order(6.55, 10, .10), 12.20)

    def test_coupon_calculation_under_105(self):
        self.assertEqual(calculate_order(3.95, 10, .15), 9.51)

    def test_coupon_calculation_under_106(self):
        self.assertEqual(calculate_order(8.92, 10, .20), 13.51)

    # Testing between 10 and 30

    def test_coupon_calculation_over_10_under_301(self):
        self.assertEqual(calculate_order(15.95, 5, .10), 18.4)

    def test_coupon_calculation_over_10_under_302(self):
        self.assertEqual(calculate_order(25.94, 5, .15), 26.82)

    def test_coupon_calculation_over_10_under_303(self):
        self.assertEqual(calculate_order(12, 5, .20), 13.89)

    def test_coupon_calculation_over_10_under_304(self):
        self.assertEqual(calculate_order(29, 10, .10), 26.08)

    def test_coupon_calculation_over_10_under_305(self):
        self.assertEqual(calculate_order(17.89, 10, .15), 15.06)

    def test_coupon_calculation_over_10_under_306(self):
        self.assertEqual(calculate_order(27.62, 10, .20), 22.89)


if __name__ == '__main__':
    unittest.main()
