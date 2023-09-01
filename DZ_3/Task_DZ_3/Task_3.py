# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
from random import choice

backpack = {'Палатка': 7,
            'Котелок': 0.7*2,
            'Топор': 3*2,
            'Консервы' : 0.4*15,
            'Крупа' : 0.5*4,
            'Хлеб' : round(0.4*3, 2),
            'Сахар' : 0.5*2,
            'Чай' : round(0.1*3, 2),
            'Сгущенка' : 0.45*5
            }
BACKPACK_SIZE = float(input('Enter the size of your backpack. Not more than 27.15 kg: '))
filling_the_backpack = 0
things_in_a_backpack = {}


for key, value in backpack.items(): 
        if filling_the_backpack + backpack[key] < BACKPACK_SIZE:
            things_in_a_backpack.setdefault(key, value)
            filling_the_backpack = filling_the_backpack + backpack[key]
     
            
print(f'In your backpack:{things_in_a_backpack}')    
print(f'The weight of your backpack: {(round(filling_the_backpack, 2))} kg')

