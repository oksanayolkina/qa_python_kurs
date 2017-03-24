import unittest

from homework3.func_distance import distance

class DistanceTests(unittest.TestCase):

    def test_zero(self):
        res = distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_one(self):
        res = distance(0, 0, 0, 1)
        self.assertEqual(res, 1)

    def test_two(self):
        res = distance(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)

    def test_two(self):
        res = distance(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)

class PositiveTests(unittest.TestCase):

    def test_my_one(self):
        res = distance(-1, -1, -1, -1)
        self.assertGreaterEqual(res, 0)

    def test_my_five(self):
        res = distance(5, 5, 5, 5)
        self.assertEqual(res, 0)

    def test_my_two(self):
        res = distance(-1, 0, 0, 0)
        self.assertGreaterEqual(res, 0)

    def test_my_three(self):
        res = distance(0, -1, 0, 0)
        self.assertGreaterEqual(res, 0)

    def test_my_four(self):
        res = distance(0, 0, -1, 0)
        self.assertGreaterEqual(res, 0)

    def test_my_six(self):
        res = distance(0, 0, 0, -1)
        self.assertGreaterEqual(res, 0)

# class NegativeTest(unittest.TestCase):

    # @unittest.expectedFailure
    # def test_my_seven(self):
    #     self.assertEqual(1, 0, "str")

    # def test_my_eight(self):
    #     res = distance(int(a), int('a'), int('c'), int('b'))
    #     self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
