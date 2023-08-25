# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

a, b, = str(input('Enter the first fraction in the format a / b: ')
            ), str(input('Enter the second fraction in the format a / b: '))
c = str(f'Your fractions: {a} and {b}')
print(c)
if a.find('/'):
    list_a = list(map(int, a.split('/')))
    list_b = list(map(int, b.split('/')))
    numerator = list_a[0] * list_b[1] + list_a[1] * list_b[0]
    denominator = list_a[1] * list_b[1]
    numerator2 = list_a[0] * list_b[0]

print(str(f'Сумма дробей равна:{numerator}/{denominator}'))
print(str(f'Произведение дробей равно:{numerator2}/{denominator}'))