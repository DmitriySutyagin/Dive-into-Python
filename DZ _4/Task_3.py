# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.



RELENISHMENT = 'Пополнить', 'пополнить', 'gjgjkybnm', 'Gjgjkybnm'
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


while balans >= 0:

    def nalog():
        if balans > MAX_LIMIT:
            balans = balans - balans * TAX_ON_WEALTH
        return f'Удержан налог на богаство в размере 10% и равен:{balans * TAX_ON_WEALTH}'  \
                f'Баланс равен:{balans}
    
    
    print(nalog())


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
