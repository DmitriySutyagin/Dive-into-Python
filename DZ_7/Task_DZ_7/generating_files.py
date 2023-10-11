# 1. Решить задачи, которые не успели решить на семинаре.

# 2. Напишите функцию группового переименования файлов. Она должна:
#     1) принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#     2) принимать параметр количество цифр в порядковом номере.
#     3) принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#     4) принимать параметр расширение конечного файла.
#     5) принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#         К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
# Решить задачи, которые не успели решить на семинаре.

import os
import random as rnd


print(os.getcwd())
# os.mkdir('d:/Mytraining/Dive_into_Python/DZ_7/Task_DZ_7/Work_dir')


def renameming(number_of_file: int, source_extensions: list[str]):
    res = []
    for _ in range(number_of_file):
        name_files = ''.join(chr(rnd.randint(97, 122)) for i in range(rnd.randint(4, 7)))
        file_extension = rnd.choice(source_extensions)
        res.append(f'{name_files}.{file_extension}')
        for file in res:
            with open(file, 'w', encoding='UTF-8'):
                pass
    return res
                                


list_of_source_extensions = ['doc', 'docx', 'pdf', 'xls', 'xlsx', 'zip', 'rar', 'jpg', 'png', 'mp3', 'wav', 'mp4', 'avi', 'txt']


if __name__ == '__main__':
    
    print(renameming(10, list_of_source_extensions))