import unittest

from homework3.func_IsYearLeap import is_year_leap

class IsYearLeapTests(unittest.TestCase):

    def test_one(self):
        res = 2016
        if res == True:
            self.assertTrue(res)
        elif res == False:
            self.assertFalse(res)

    def test_two(self):
        res = str()
        self.assertFalse(res)

    def test_three(self):
        res = -2016
        self.assertLessEqual(res, 0)