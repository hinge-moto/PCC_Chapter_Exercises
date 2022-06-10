# May 25.2022

class Employee:
    """Describe a basic employee."""

    def __init__(self, first, last, salary=50000):
        """Initialize the employee class."""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def describe_employee(self):
        """Describes the employee."""
        name_and_salary = (f"{self.first} {self.last} makes "
                           f"${self.salary} per year.")
        return name_and_salary

    def give_raise(self, salary_raise=5000):
        """Increases the employee's salary by an amount."""
        self.salary += salary_raise

##my_employee = Employee('justice', 'ramrod')
##print(my_employee.describe_employee())
##
##my_employee.give_raise()
##print(my_employee.describe_employee())
