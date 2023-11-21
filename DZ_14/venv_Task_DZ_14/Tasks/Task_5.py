import pytest


class NegativeValueError(ValueError):
    pass


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
    
    
def test_width():
    """ Тестирование инициализации ширины. """
    r1 = Rectangle(5)
    assert r1.width == 5


def test_height():
    """ Тестирование инициализации ширины и высоты.  """
    r1 = Rectangle(3, 4)
    assert r1.height == 4


def test_perimeter():
    """  Тестирование вычисления периметра. """
    r1 = Rectangle(5)
    assert r1.perimeter() == 20


def test_area():
    """  Тестирование вычисления площади. """
    r1 = Rectangle(3, 4)
    assert r1.area() == 12


def test_addition():
    """ Тестирование операции сложения двух прямоугольников.  """
    r1 = Rectangle(5, 3)
    r2 = Rectangle(1,4)
    r3 = r1 + r2
    assert r3.width == 6
    assert r3.height == 8.0


def test_negative_width():
    """  Тестирование инициализации отрицательной ширины. """
    with pytest.raises(NegativeValueError) as e:
        r1 = Rectangle(-5)
    assert e


def test_negative_height():
    """ Тестирование инициализации отрицательной высоты. """
    with pytest.raises(NegativeValueError) as e:
        r1 = Rectangle(5, -4)
    assert e


def test_set_width():
    """ Тестирование изменения ширины. """  
    r1 = Rectangle(5)
    r1.width = 10
    assert r1.width == 10


def test_set_negative_width():
    """  Тестирование изменения отрицательной ширины.  """
    r1 = Rectangle(5)
    with pytest.raises(NegativeValueError) as e:
        r1.width = -10
    assert e


def test_set_height():
    """  Тестирование изменения высоты. """
    r1 = Rectangle(3, 4)
    r1.height = 6
    assert r1.height == 6


def test_set_negative_height():
    """ Тестирование изменения отрицательной высоты.  """
    r1 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError) as e:
        r1.height = -6
    assert e


def test_subtraction():
    """  Тестирование операции вычитания двух прямоугольников.   """
    r1 = Rectangle(10, 1)
    r2 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError) as e:
        r3 = r1 - r2
    assert e


def test_subtraction_negative_result():
    """  Тестирование операции вычитания с отрицательным результатом. """
    r1 = Rectangle(3, 4)
    r2 = Rectangle(10, 1)
    r3 = r1 - r2


def test_subtraction_same_perimeter():
    """ Тестирование операции вычитания с одинаковым периметром.  """
    r1 = Rectangle(5, 1)
    r2 = Rectangle(4, 3)
    r3 = r1 - r2
    assert r3.width == 1
    assert r3.height == -2





if __name__ == '__main__':
    pytest.main(["--no-header", '-q', "--durations=0", __file__])
