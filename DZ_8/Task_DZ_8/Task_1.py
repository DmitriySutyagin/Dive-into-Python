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


# os.mkdir('D:\Mytraining\Storage_file')
os.chdir('D:\Mytraining\Storage_file')


def bypas(path: str, res: list)-> None:

    for path_dir, name_dir, name_file in os.walk(path):
        res.append({'path_dir': path_dir, 
                    'folder':f'{os.path.split(path_dir)[1]}, {os.path.isdir(path_dir)}',
                    'file': name_file,
                    'size': os.path.getsize(path_dir)})
     
 
res= []

bypas("D:\Mytraining\Excel", res)


with open('json_file.json', 'w', encoding='utf-8') as j:
    json_file = json.dump(res, j, ensure_ascii=False,indent=2)

with open('csv_file.csv', 'w', encoding='utf-8') as c:
    csv_file = csv.DictWriter(c, fieldnames=res[0].keys())
    csv_file.writeheader()
    csv_file.writerows(res)

with open("pickle_pickle.pickle", "wb") as pickle_file:
    pickle.dump(res, pickle_file)