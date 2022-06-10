# May 25.2022

import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create a basic employee for use in test cases."""
        self.my_employee = Employee('bob', 'dole')

    def test_give_default_raise(self):
        """Raise the employee's salary by the default amount."""
        self.my_employee.give_raise()
        salary = self.my_employee.salary
        self.assertEqual(salary, 55000)

    def test_give_custom_raise(self):
        """Raise the employee's salary by a custom amount."""
        self.my_employee.give_raise(666)
        salary = self.my_employee.salary
        self.assertEqual(salary, 50666)

if __name__ == '__main__':
    unittest.main()
