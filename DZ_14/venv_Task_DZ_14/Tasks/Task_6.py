import pytest

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
    

class TestEmployee():

    def test_employee_full_name(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 50_000.0)
        assert 'Ivanov Ivan Ivanovich' == self.emp.full_name()

    def test_employee_birthday(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 50_000.0)
        self.emp.birthday()
        assert 31 == self.emp.get_age()

    def test_employee_raise_salary(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 50_000.0)
        self.emp.raise_salary(10)
        assert 55000.0 == self.emp.salary

    def test_employee_str(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 50_000.0)
        assert "Ivanov Ivan Ivanovich (Plumber)" == self.emp.__str__()
        # test_employee_last_name_title: Тестирование атрибута last_name.
# Создайте объект Employee с фамилией "Ivanov" и убедитесь, что атрибут last_nameвозвращается в верхнем регистре, то есть "Ivanov".
    def test_employee_last_name_title(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Plumber", 50_000.0)
        assert "Ivanov" == self.emp.last_name


if __name__ == '__main__':
    pytest.main(["--no-header", '-q', "--durations=0", __file__])


