import unittest

from homework3.class_Worker import Worker

class WorkerTestsOne(unittest.TestCase):

    def setUp(self):
        self.wor = Worker(full_name="Alekseienko Oksana", position="QA Engineer", salary=20000, experience=3)

    def test_one(self):
        self.assertIsNotNone(self.wor.full_name)
        self.assertIsNotNone(self.wor.position)
        self.assertIsNotNone(self.wor.salary)
        self.assertIsNotNone(self.wor.experience)

    def test_two(self):
        self.assertGreaterEqual(self.wor.salary, 0)
        self.assertGreaterEqual(self.wor.experience, 0)

    def test_three(self):
        self.assertEqual(self.wor.full_name, "Alekseienko Oksana")
        self.assertEqual(self.wor.position, "QA Engineer")
        self.assertEqual(self.wor.salary, 20000)
        self.assertEqual(self.wor.experience, 3)

    def test_four(self):
        self.assertNotEqual(self.wor.full_name, "Ivanov Ivan")
        self.assertNotEqual(self.wor.position, "QA")
        self.assertNotEqual(self.wor.salary, 5000)
        self.assertNotEqual(self.wor.experience, -3)

class WorkerTestsTwo(unittest.TestCase):

    def setUp(self):
        self.work = Worker(full_name="Alekseienko Oksana", salary=20000, experience=3)

    def test_five(self):
        self.assertEqual(self.work.get_firstname(), "Oksana")
        self.assertEqual(self.work.get_lastname(), "Alekseienko")

    def test_six(self):
        self.assertEqual(self.work.get_salary(10), 200000)

    def test_seven(self):
        self.assertEqual(self.work.get_experience(), "Your level is MIDDLE")

    def test_eight(self):
        self.work = Worker(full_name="Alekseienko Oksana", experience=0)
        self.assertEqual(self.work.get_experience(), "Experience is absent")