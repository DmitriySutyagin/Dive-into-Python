import doctest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def test_employee_full_name():
    """
    >>> FIO = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 10000)
    >>> FIO.full_name()
    'Ivanov Ivan Ivanovich'
    """


def  test_employee_birthday():
    """
    >>> FIO = Employee("Ivanov", "Ivan", "Ivanovich", 22, "Plumber", 10000)
    >>> FIO.birthday()
    >>> FIO.get_age()
    23
    """


def test_employee_raise_salary():
    """
    >>> emp = Employee("Ivanov", "Ivan", "Ivanovich", 22, "Plumber", 50000)
    >>> emp.raise_salary(10)
    >>> emp.salary
    55000.0
    """


def test_employee_str():
    """
    >>> FIO = Employee("Ivanov", "Ivan", "Ivanovich", 22, "Plumber", 10000)
    >>> str(FIO)
    'Ivanov Ivan Ivanovich (Plumber)'
    """


def test_employee_last_name_title():
    """
    >>> FIO = Employee("ivanov", "ivan", "ivanovich", 22, "plumber", 10000)
    >>> FIO.last_name.title()
    'Ivanov'
    """

    
# if __name__ == '__main__':
#     doctest.testmod(verbose=True)

__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})

    