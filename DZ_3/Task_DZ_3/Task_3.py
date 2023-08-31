# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import random

backpack = {'Палатка': 7,
            'Котелок': 0.7*2,
            'Топор': 3*2,
            'Консервы' : 0.4*15,
            'Крупа' : 0.5*4,
            'Хлеб' : 0.4*3,
            'Сахар' : 0.5*2,
            'Чай' : 0.1*3,
            'Сгущенка' : 0.45*5
            }
BACKPACK_SIZE = 20.4
filling_the_backpack = 0
things_in_a_backpack = {}


for key, value in backpack.items(): 
        if filling_the_backpack < BACKPACK_SIZE:
            things_in_a_backpack.setdefault(key, value)
            filling_the_backpack = filling_the_backpack + backpack[key]
        else:
            i =+ 1 
            
print(things_in_a_backpack)    
print(filling_the_backpack)

