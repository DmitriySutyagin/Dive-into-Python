# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


def _bin(a, b):
    result = ' '
    while a > 0:
        result = str(a % b) + result
        a = a // b
    return result

a = int(input('Enter the number: '))
b = int(input('Enter the value of the string representation of the number '))
print(_bin(a, b))
