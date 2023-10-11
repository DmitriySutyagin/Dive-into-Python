# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import Task_4
from Task_4 import create_file, min_length, max_length, min_bytes, max_bytes, numbeer_of_files
import random as rnd


def gen_diff_faile(numbeer_of_files, diff_extension ):


    
        
    
    Task_4.create_file((rnd.choice(diff_extension) for i in range(numbeer_of_files)), numbeer_of_files, min_length, max_length, min_bytes, max_bytes)



    
extensions = str(input('Enter extensions: ')).split(' ')



print(gen_diff_faile(numbeer_of_files, extensions))