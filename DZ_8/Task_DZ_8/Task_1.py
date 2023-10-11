# # Решить задания, которые не успели решить на семинаре.
# # Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.

#     # Для дочерних объектов указывайте родительскую директорию.
#     # Для каждого объекта укажите файл это или директория.
#     #  Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# # Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle


def bypas(path: str, dict_: dict)-> None:


    for path_dir, name_dir, name_file in os.walk(path):
        # print(f"{path_dir=},{name_dir=},{name_file=}")
        
        for folder in name_dir:
            if os.path.isdir(path+'\\'+folder):
                # print(os.path.isdir(path+'\\'+folder) )
                # print(dict_.get(f'{folder}'))

                # bypas(path+'\\'+folder, dict_)
                print(dict_.setdefault(folder, {folder:os.listdir(path+'\\'+folder)}))
                

            elif os.path.isfile(path+'\\'+folder):
                bypas(path+'\\'+folder, dict_)
                
    return             
                
         





dict_  = {}
path = "D:\Mytraining\Excel"
print(bypas(path, dict_))

