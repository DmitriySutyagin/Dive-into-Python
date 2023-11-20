# test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом.
# Создайте два прямоугольника: один с шириной 3 и высотой 4, другой с шириной 10. 
# Попробуйте выполнить операцию вычитания r1 - r2 и убедитесь, что это вызывает исключение NegativeValueError.
# test_subtraction_same_perimeter: Тестирование операции вычитания с прямоугольниками одинакового периметра.
# Создайте два прямоугольника: один с шириной 5, другой с шириной 4 и высотой 3. 
# Выполните операцию вычитания r1 - r2 и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (1 и 1.0 соответственно).
# Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.

import unittest

class NegativeValueError(ValueError):
    pass


class TestRectangle(unittest.TestCase):

    def test_width(self):
        self.r1 = Rectangle(5)
        self.assertEqual(self.r1.width, 5)

    def test_height(self):
        self.r2 = Rectangle(3, 4)
        self.assertEqual(self.r2.height, 4)

    def test_perimrter(self):
        self.r1 = Rectangle(5)
        self.assertEqual(self.r1.perimeter(), 20)

    def test_area(self):
        self.r2 = Rectangle(3, 4)
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)
        self.r3 = self.r1 + self.r2
        self.assertEqual(self.r3.width, 8)
        self.assertEqual(self.r3.height, 9)

    def test_subtraction(self):
        self.r1 = Rectangle(10)
        self.r2 = Rectangle(3, 4)
        self.r3 = self.r1 - self.r2
        self.assertEqual(self.r3.width, 7)
        self.assertEqual(self.r3.height, 6)

    # def test_negative_width(self):
    #     try:
    #         self.r4 = Rectangle(-5)
    #     except NegativeValueError as e:
    #         raise e

    # def test_negative_height(self):
    #     self.r1 = Rectangle(5, -4)
    #     self.assertRaisesRegex(NegativeValueError, self.height, self.r1.height)

    def test_set_width(self):
        self.r1 = Rectangle(5)
        self.r1.width = 10
        self.assertEqual(self.r1.width, 10)

    # def test_set_negative_width(self):
    #     self.r1 = Rectangle(5)
    #     self.r1.width = -10
    #     self.assertEqual(self.r1.width, -10)
    
    def test_set_height(self):
        self.r1 = Rectangle(3, 4)
        self.r1.height = 6
        self.assertEqual(self.r1.height, 6)

    # def test_set_negative_height(self):
    #     self.r1 = Rectangle(3, 4)
    #     self.r1.height = -6
    #     self.assertEqual(self.r1.height, -6)

    # def test_subtraction_negative_result(self):
    #     self.r1 = Rectangle(3, 4)
    #     self.r2 = Rectangle(10)
    #     self.r3 = self.r1 - self.r2
    #     self.assertEqual(self.r3, Rectangle(-7, -6))
        
    def test_subtraction_same_perimeter(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(4, 3)
        self.r3 = self.r1 - self.r2
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 1.0)


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)




        






    

if __name__ == '__main__':
    unittest.main(verbosity=2)
