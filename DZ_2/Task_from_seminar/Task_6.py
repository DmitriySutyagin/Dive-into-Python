# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


RELENISHMENT = 'Пополнить'
WITHDRAWAL = 'Снять'
EXIT_FROM_THE_PROGRAM = 'Выход'
MIN_WITHDRAWAL_AND_RELENISHMENT = 50
INTEREST_FOR_OPERATIONS = 0.03
EVERY_THIRD_OPERATION = 3
DIGITS_AFTER_THE_COMMA = 2
MAX_LIMIT = 5_000_000
TAX_ON_WEALTH = 0.1
WITHDRAWAL_PERCENTAGE = 0.015
MIN_WITHDRAWAL = 30
MAX_WITHDRAWAL = 600

balans = 0
count = 0


print('Доброго времени суток! Вам доступны операции снятия и пополнения, а также завершения сеанса.')
print('Если вы хотите пополнить, снять или завершить сеанс. Наберите пополнить и сумма пополнение, снять и сумма снятия или выход')


while balans == 0 or balans > 0:
    if balans > MAX_LIMIT:
        balans = balans - balans * TAX_ON_WEALTH
        print(f'Удержан налог на богаство в размере 10% и равен:{balans * TAX_ON_WEALTH}')
        print(f'Баланс равен:{balans}')


    RELENISHMENT_OF_THE_CLIENT = str(input('Введите название операции: '))

    if RELENISHMENT_OF_THE_CLIENT == EXIT_FROM_THE_PROGRAM:
        print('Работа банкомата завершена')
        break

    replenishment_amount = int(input('Введите сумму операции: '))

    if replenishment_amount < MIN_WITHDRAWAL_AND_RELENISHMENT:
        print('Сумма пополнения и снятия кратны 50 у.е.')
        print(f'Баланс равен:{balans}')
        continue

    elif RELENISHMENT_OF_THE_CLIENT == RELENISHMENT:
        count += 1
        balans = balans + replenishment_amount
        print(f'Баланс равен:{balans}')
        
        if count % EVERY_THIRD_OPERATION == 0:
           balans = balans + balans * INTEREST_FOR_OPERATIONS
           print(f'Начислен процент по счету за операции: {round(balans * INTEREST_FOR_OPERATIONS, DIGITS_AFTER_THE_COMMA)}')
           print(f'Баланс равен:{balans}')
        continue

    elif RELENISHMENT_OF_THE_CLIENT == WITHDRAWAL:
        count += 1
        if replenishment_amount > balans:
            print('Нельзя снять больше чем на счете')
            print(f'Баланс равен:{balans}')
            continue
        else:
            balans = balans - replenishment_amount
            if replenishment_amount * WITHDRAWAL_PERCENTAGE < MIN_WITHDRAWAL:
                balans = balans - MIN_WITHDRAWAL
                print('Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.')
                print(f'Процент снятия равен: {MIN_WITHDRAWAL}')
                print(f'Баланс равен:{balans}')

            elif replenishment_amount * WITHDRAWAL_PERCENTAGE > MAX_WITHDRAWAL:
                balans = balans - MAX_WITHDRAWAL
                print('Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.')
                print(f'Процент снятия равен: {MAX_WITHDRAWAL}')
                print(f'Баланс равен:{balans}')

            else:
                balans = balans - balans * WITHDRAWAL_PERCENTAGE  
                print('Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.')
                print(f'Процент снятия равен: {replenishment_amount * WITHDRAWAL_PERCENTAGE}')
                print(f'Баланс равен:{balans}')            
            
            if count % EVERY_THIRD_OPERATION == 0:
                balans = balans + balans * INTEREST_FOR_OPERATIONS
                print(f'Начислен процент по счету за операции: {round(balans * INTEREST_FOR_OPERATIONS, DIGITS_AFTER_THE_COMMA)}')
                print(f'Баланс равен:{balans}')
            continue
  
else:

    quit()
