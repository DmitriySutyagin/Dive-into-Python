# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import Task_4
from Task_4 import create_file



extensions, *_ = str(input('Enter extensions: '))
numbeer_of_files = int(input('Eneter number: '))
min_length = int(input('Enter min length name file: '))
max_length = int(input('Enter max length name file: '))
min_bytes = int(input('Eneter min size file: '))
max_bytes = int(input('Eneter max size file: '))


Task_4.create_file(*extensions, numbeer_of_files, min_length, max_length, min_bytes, max_bytes)