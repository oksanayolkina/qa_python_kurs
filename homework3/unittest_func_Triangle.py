import  unittest

from homework3.func_Triangle import triangle

class TriangleTests(unittest.TestCase):

    def test_one(self):
        res = triangle(0, 0, 0)
        self.assertFalse(res, False)

    def test_two(self):
        res = triangle(10, 5, 11)
        self.assertTrue(res, True)

    def test_three(self):
        res = triangle(-3, -5, -2)
        self.assertFalse(res, False)

    def test_four(self):
        res = triangle(5, 6, 11)
        self.assertIsNotNone(res)

# def test_no_positon(self): self.assertIsNone(self.emp.position)
