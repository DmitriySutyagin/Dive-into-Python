# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import os
import random as rnd


def create_file(file_extension: str, number_of_files: int, min_len: int, max_len: int, min_bytes: int, max_bytes: int):
    res = []
    for i in range(number_of_files):
        name_files = ''.join(chr(rnd.randint(97, 122)) for i in range(rnd.randint(min_len, max_len)))
        res.append(f'{name_files}.{file_extension}')
        for file in res:
            with open(file, 'wb') as f:
                f.truncate(rnd.randint(min_bytes, max_bytes))
    return res


numbeer_of_files = int(input('Eneter number: '))
min_length = int(input('Enter min length name file: '))
max_length = int(input('Enter max length name file: '))
min_bytes = int(input('Eneter min size file: '))
max_bytes = int(input('Eneter max size file: '))
       
if __name__ == '__main__':
    
    print(create_file('txt', numbeer_of_files, min_length, max_length, min_bytes, max_bytes))