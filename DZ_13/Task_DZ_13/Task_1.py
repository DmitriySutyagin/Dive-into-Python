class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """
    
class NegativeValueError(ValueError):
      pass

class Rectangle:
    
    def __init__(self, width: int, height: int = None):
        if width <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self._width + self._height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self._width * self._height
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

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self._width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

#     def __lt__(self, other):
#         """
#         Определяет операцию "меньше" для двух прямоугольников.

#         Аргументы:
#         - other (Rectangle): второй прямоугольник

#         Возвращает:
#         - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
#         """
#         return self.area() < other.area()

#     def __eq__(self, other):
#         """
#         Определяет операцию "равно" для двух прямоугольников.

#         Аргументы:
#         - other (Rectangle): второй прямоугольник

#         Возвращает:
#         - bool: True, если площади равны, иначе False
#         """
#         return self.area() == other.area()

#     def __le__(self, other):
#         """
#         Определяет операцию "меньше или равно" для двух прямоугольников.

#         Аргументы:
#         - other (Rectangle): второй прямоугольник

#         Возвращает:
#         - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
#         """
#         return self.area() <= other.area()

#     # def __str__(self):
#     #     """
#     #     Возвращает строковое представление прямоугольника.

#     #     Возвращает:
#     #     - str: строковое представление прямоугольника
#     #     """
#     #     return f"Прямоугольник со сторонами {self._width} и {self._height}"

#     # def __repr__(self):
#     #     """
#     #     Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

#     #     Возвращает:
#     #     - str: строковое представление прямоугольника
#     #     """
#         return f"Rectangle({self._width}, {self._height})"
    

# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(3, 3)

# print(rect1)
# print(rect2)

# print(rect1.perimeter())
# print(rect1.area())
# print(rect2.perimeter())
# print(rect2.area())

# rect_sum = rect1 + rect2
# rect_diff = rect1 - rect2

# print(rect_sum)
# print(rect_diff)

# print(rect1 < rect2)
# print(rect1 == rect2)
# print(rect1 <= rect2)

# print(repr(rect1))
# print(repr(rect2))