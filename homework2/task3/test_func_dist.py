import unittest

from exercise import distance

class PositiveTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_zero(self):
        result = distance(5, 0, 0, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()