import unittest

from lesson3.test8 import ITEmployee

class EmpNoPositionTests(unittest.TestCase):

    def test_creation1(self):

        emp = ITEmployee("Oksana", "Alekseienko")
        self.assertEqual(emp.name, "Oksana")
        self.assertEqual(emp.surname, "Alekseienko")

        self.assertEqual(emp.position, None)
        self.assertIsNone(emp.position)

        self.assertEqual(len(emp.skills), 0)

class NegativeTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()