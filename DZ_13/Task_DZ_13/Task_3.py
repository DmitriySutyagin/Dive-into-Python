# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

# Ваша задача:

# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.

class InvalidNameError(ValueError):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age: int) -> None:
        self.age = age

    def __str__(self) -> str:
        return f'Invalid age: {self.age}. Age should be a positive integer.'
    

class InvalidIdError(ValueError):
    def __init__(self, ID: int) -> None:
        self.ID = ID
    
    def __str__(self) -> str:
        return f'Invalid id: {self.ID}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, last_name: str, name: str, surname: str, age: int) -> None:
        if type(last_name) != str or len(last_name) == 0:
            raise InvalidNameError(last_name)
        if type(name) != str or len(name) == 0:
            raise InvalidNameError(name)
        if type(surname) != str or len(surname) == 0:
            raise InvalidNameError(surname)
        if type(age) != int or age <= 0:
            raise InvalidAgeError(age)
        
        self.last_name = last_name
        self.name = name
        self.surname = surname
        self._age = age

    def birtday(self):
        self._age += 1
    
    def get_age(self):
        return self._age

    def full_name(self):
        return f'{self.last_name} {self.name} {self.surname}'



class Employee(Person):
    DELITEL = 7

    def __init__(self, last_name: str, name: str, surname: str, age: int, ID: int) -> None:
        super().__init__(last_name, name, surname, age)
        if type(ID) != int or ID < 100_000 or ID > 999999:
            raise InvalidIdError(ID)
        self.ID = ID
        
    def get_level(self):
        return sum(int(i) for i in str(self.ID)) % self.DELITEL
