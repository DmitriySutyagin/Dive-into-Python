# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет".
# "Зачет" ставится, если Слушатель успешно выполнил задание.
# "Незачет" ставится, если Слушатель не выполнил задание.
# Критерии оценивания: 1 - Слушатель написал корректный код для задачи, добавил к ним логирование ошибок и полезной информации.

from sys import argv
import logging
import os
import argparse


os.chdir('D:\Mytraining\Dive_into_Python\DZ_15\Task_DZ_15')


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
'в строке {lineno:03d} функция "{funcName}()" ' \
'в {created} секунд записала сообщение: {msg}'


logging.basicConfig(format=FORMAT, style='{', filename='Final_work.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class NegativeValueError(ValueError):
      pass


class Rectangle:
    
    def __init__(self, width: int, height: int = None):
        logger.info('Запуск программы прошел успешно. Тестирование значения ширины.')

        if width <= 0:
            logger.info('Программа завершилась ошибкой')
            logger.error(f"Ширина должна быть положительной, а не {width}")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        else:
            self._width = width
            logger.info('Завершение программы прошело успешно. Значение ширины в допустимых параметрах.')
        
        logger.info('Запуск программы прошел успешно. Тестирование значения высоты.')
        if height is None:
            self._height = width
            logger.info('Завершение программы прошело успешно. Значение высоты в допустимых параметрах.')
        else:
            if height <= 0:
                logger.info('Программа завершилась ошибкой')
                logger.error(f'Высота должна быть положительной, а не {height}')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            else:
                self._height = height
                logger.info('Завершение программы прошело успешно. Значение высоты в допустимых параметрах.')
                
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
        logger.info('Запуск программы прошел успешно. Тестирование значения ширины.')

        if value > 0:
            self._width = value
            logger.info('Завершение программы прошело успешно. Значение ширины в допустимых параметрах.')

        else:
            logger.info('Программа завершилась ошибкой')
            logger.error(f"Ширина должна быть положительной, а не {value}")
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')  
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        logger.info('Запуск программы прошел успешно. Тестирование значения высоты.')
        if value > 0:
            self._height = value
            logger.info('Завершение программы прошел успешно. Значение высоты в допустимых параметрах.')

        else:
            logger.info('Программа завершилась ошибкой')
            logger.error(f'Высота должна быть положительной, а не {value}')
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

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

       Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self._width}, {self._height})"

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('-a', metavar='a', type=float, help='enter a b c separated by a space', default=0)
    parser.add_argument('-b', metavar='b', type=float, help='enter a b c separated by a space', default=0)
    args = parser.parse_args()
    Rectangle(args.a, args.b)