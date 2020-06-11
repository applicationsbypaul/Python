"""
Program: test_validation_with_try.py
Author: Paul Ford
Last date modified: 06/10/2020
Purpose: gather user information
display average score with information
"""

import unittest

from average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average_exception1(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_exception2(self):
        with self.assertRaises(ValueError):
            average(90, -89, 78)

    def test_average_exception3(self):
        with self.assertRaises(ValueError):
            average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
