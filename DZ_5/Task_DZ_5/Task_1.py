# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


path = str(input('Specify the path to the file with the file name: '))

def file(path):

    *_, suffix = path.split('\\')
    *_, suffix_2 = suffix.split('.')    

    return f'path: {path}', f'name: {suffix}', f'expansion: {suffix_2}'


print(file(path))  
    

