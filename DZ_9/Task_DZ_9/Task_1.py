# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
#  Функция принимает два аргумента:

# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах 
# и результатах вычислений для каждой строки данных из CSV-файла.

import os
from random import randint as rnd
import json
import csv
import numpy as np
write_to_code = 'def save_to_json , def find_roots, def generate_csv_file'


os.chdir('D:\Mytraining\Storage_file')

def generate_csv_file(file_name: str, rows: int):
    """ The function generates three random numbers in each line, from 100-1000 lines, and writes them to a CSV file """
    
    with open(file_name, 'w', newline='') as c:
        csv_file = csv.writer(c)
        for i in range(rows):
            stroka =[rnd(100, 1000) for y in range(NAMBER_OF_A_ROW)]
            csv_file.writerow(stroka)
  




NAMBER_OF_A_ROW = 3
MIN_NUMBER = 100
MAX_NUMBER = 1000
number_of_rows = rnd(MIN_NUMBER, MAX_NUMBER)

generate_csv_file('csv_file_3.csv',number_of_rows)


def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open('csv_file_3.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                result_list.append({'args_a': row[0],
                                    'args_b': row[1],
                                    'args_c': row[2],
                                    'result': result})
        
        with open('results.json', 'w') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=2)
        return result
    return wrapper


@save_to_json
def find_roots(file_name: str='csv_file_3.csv', a: int=1, b: int=1, c: int=1):
    """ The function is to find the roots of a quadratic equation of the form ax^2 + bx + c = 0. """
   
    D = b**2 - 4 * a * c
    if D < 0:
        return None
    if D == 0:
        return - b / 2 * a
    if D > 0:
        x_1 =  (- b - np.sqrt(D)) / 2 * a
        x_2 =  (- b + np.sqrt(D)) / 2 * a
        return x_1, x_2 


find_roots()  


with open("__init__.py", "w") as init:
    list_of_function = write_to_code.split(',')
    for i in list_of_function:
        code = init.writelines(i)
