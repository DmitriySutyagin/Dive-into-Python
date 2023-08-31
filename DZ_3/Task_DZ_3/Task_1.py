# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

import random



n = int(input('Введите количество элементов для формирования спика: '))
a = int(input('Введите минимальное число: '))
b = int(input('Введите максимальное число: '))

my_list = [random.randint(a, b) for i in range(n)]
print(my_list)
new_my_list = list(set(( i for i in my_list if my_list.count(i) == 2)))
print(new_my_list)