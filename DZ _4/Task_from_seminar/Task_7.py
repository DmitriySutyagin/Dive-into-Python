# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
import random 


firm = ['ООО"Тлл"', 'ООО"Острый глаз"', 'ТОО"Лилия"','ЗАО"Нежность"','ООО"Хозяйка"','ТОО"Ширма"','ЗАО"Дело"','ЗАО"Ленист"']
BALANS = 10
MIN_ = - 1_000_000
MAX_ = 1_000_000

def bizness(firm: list[str]):
    for i in firm:
        a = [random.randint(MIN_, MAX_) for i in range(BALANS)]
        d = {i: sum(a) for i in firm }
        e = [sum(a) for i in d ]


    if all(map(lambda x: x > 0, e)):
        return True
    else:
        return False 
    
       
    return e

print(bizness(firm))
