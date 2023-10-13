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
        for file in name_file:
            res.append({'path_dir': path_dir, 
                        'folder':os.path.split(path_dir)[1], 
                        'is_folder' : os.path.isdir(path_dir),
                        'size_folder' : os.path.getsize(path_dir),
                        'file': file,
                        'is_file': os.path.isfile(path_dir+'\\'+file),
                        'size_file': os.path.getsize(path_dir+'\\'+file)})
     
 
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