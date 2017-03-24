import unittest

from homework3.class_ITEmployee import ITEmployee

class EmployeeWithoutPositionTests(unittest.TestCase):

    def setUp(self):
        self.emp = ITEmployee("Oksana", "Alekseienko")

    def test_names(self):
        self.assertEqual(self.emp.name, "Oksana")
        self.assertEqual(self.emp.surname, "Alekseienko")

    def test_no_positon(self):
        self.assertIsNone(self.emp.position)

    def test_no_skills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def test_add_position(self):
        self.emp.set_position('QA engineer')
        self.assertEqual(self.emp.position, 'QA engineer')

    def test_add_one_skill(self):
        self.emp.add_skill('git')
        self.assertIn('git', self.emp.skill)


class ITEmployeeTests(unittest.TestCase):

    def setUp(self):
        self.emp = ITEmployee("Oksana", "Alekseienko", "QA engineer")

    def test_one(self):
        self.assertIsNotNone(self.emp.name)
        self.assertIsNotNone(self.emp.surname)
        self.assertIsNotNone(self.emp.position)

    def test_two(self):
        self.assertGreaterEqual(len(self.emp.name), 2)
        self.assertGreaterEqual(len(self.emp.surname), 2)
        self.assertGreaterEqual(len(self.emp.position), 2)

    def test_three(self):
        self.emp.add_skills('git', 'SQL', 'jira')
        self.assertIn('SQL', self.emp.skills)
        self.assertNotIn('PHP', self.emp.skills)
        self.assertIsNotNone(self.emp.add_skills)


if __name__ == "__main__":
    unittest.main()