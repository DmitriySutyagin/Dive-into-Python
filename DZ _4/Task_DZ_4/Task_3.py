# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.



MIN_WITHDRAWAL_AND_RELENISHMENT = 50
INTEREST_FOR_OPERATIONS = 0.03
EVERY_THIRD_OPERATION = 3
DIGITS_AFTER_THE_COMMA = 2
MAX_LIMIT = 5_000_000
TAX_ON_WEALTH = 0.1
WITHDRAWAL_PERCENTAGE = 0.015
MIN_WITHDRAWAL = 30
MAX_WITHDRAWAL = 600




print('Доброго времени суток! Вам доступны операции снятия и пополнения, а также завершения сеанса.')
print('Если вы хотите пополнить, снять или завершить сеанс. Наберите пополнить и сумма пополнение, снять и сумма снятия или выход')


def ATM_machine():

    """ The function simulates the operation of an ATM """

    global exit_from_the_program
    global relenishment
    global withdrawal
    global balans 
    global count
    
    while balans >= 0:
        if balans > MAX_LIMIT:
            balans = balans - balans * TAX_ON_WEALTH
            print(f'Удержан налог на богаство в размере 10% и равен:{balans * TAX_ON_WEALTH}')
            print(f'Баланс равен:{balans}')

        relenishment_of_the_client = str(input('Введите название операции: '))

        if  relenishment_of_the_client in exit_from_the_program:
            print('Работа банкомата завершена')
            break

        replenishment_amount = int(input('Введите сумму операции: '))

        if replenishment_amount < MIN_WITHDRAWAL_AND_RELENISHMENT:
            print('Сумма пополнения и снятия кратны 50 у.е.')
            print(f'Баланс равен:{balans}')
            continue

        elif relenishment_of_the_client in relenishment:   # Пополнить
            count += 1
            balans = balans + replenishment_amount
            print(f'Баланс равен:{balans}')
        
            if count % EVERY_THIRD_OPERATION == 0:
                balans = balans + balans * INTEREST_FOR_OPERATIONS
                print(f'Начислен процент по счету за операции: {round(balans * INTEREST_FOR_OPERATIONS, DIGITS_AFTER_THE_COMMA)}')
                print(f'Баланс равен:{balans}')
                continue

        elif relenishment_of_the_client in withdrawal:    # Снять
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




exit_from_the_program = ['Выход', 'выход', 'выхот', 'ВЫХОТ', 'Выхот']
relenishment = ['Пополнить', 'пополнить', 'ПОПОЛНИТЬ', 'ПОПОЛНИТ', 'Пополнит', 'ПАПОЛНИТЬ', 'ПАПОЛНИТ', 'паполнить', 'паполнит']
withdrawal = ['Снять', 'снять', 'снят', 'Снят']
balans = 0
count = 0
ATM_machine()