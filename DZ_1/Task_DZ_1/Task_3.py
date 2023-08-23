# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT) 
LIMIT_OF_ATTEMPTS = 11
count = 1

print('Enter a number between', LOWER_LIMIT, 'and', UPPER_LIMIT)

while count < LIMIT_OF_ATTEMPTS:
    print('Attempt', count)
    count += 1

   
    player_number = float(input())
    if LOWER_LIMIT < player_number > UPPER_LIMIT:
        print('Enter a number from the range from 0 to 1000')
        continue
    if player_number > num:
        print('The hidden number is less than yours')
    elif player_number < num:
        print('The hidden number is bigger than yours') 
    else:
        break

else:
    print(f'All attemps have been exhausted. I am sory. The hidden number was: {num}')      
    quit()


print(f'You guessed this number: {num}')