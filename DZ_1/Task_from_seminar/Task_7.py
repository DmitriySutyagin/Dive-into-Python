#Задание №7
#Пользователь вводит число от 1 до 999. Используя операции с числами
#сообщите что введено: цифра, двузначное число или трёхзначное число.
#Для цифры верните её квадрат, например 5 - 25
#Для двузначного числа произведение цифр, например 30 - 0
#Для трёхзначного числа его зеркальное отображение, например 520 - 25
#Если число не из диапазона, запросите новое число
#Откажитесь от магических чисел
#В коде должны быть один input и один print


import math


MIN_NUM = 1
THE_FIRST_CUTOFF = 9
SECOND_CUTOFF = 100
MAX_NUM = 999

#num = int(input('Введите любое целое число: '))
while MIN_NUM < num > MAX_NUM:
    num = int(input('Введите любое целое число: '))
    continue
if num >= MIN_NUM and num <= THE_FIRST_CUTOFF:
    print(f'Вы ввели цифру ее квадрат равен {num**2}')
elif num > THE_FIRST_CUTOFF and num < SECOND_CUTOFF:
  #  print(f'Вы ввели двухзначное число! Произведение цифр данного числа равно {}')