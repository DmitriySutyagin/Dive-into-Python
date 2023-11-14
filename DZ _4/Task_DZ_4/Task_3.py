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


def ATM_machine(balans, count, entrance, withdrawal_):

    relenishment_of_the_client = str(input('Введите название операции: '))       # Ввод команды
    

    if  relenishment_of_the_client in exit_from_the_program:    # Выход
        return exit('Работа банкомата завершена')
    
    replenishment_amount = int(input('Введите сумму операции: '))       # Ввод суммы

 
    def relenishment_(relenishment_of_the_client, replenishment_amount):

        global balans
        global count
        global entrance
        
        if relenishment_of_the_client in relenishment and replenishment_amount % MIN_WITHDRAWAL_AND_RELENISHMENT == 0:   # Пополнить
        
           
                    


            if balans  > MAX_LIMIT:
                

                count += 1
                nalog = balans * TAX_ON_WEALTH
                balans = balans - balans * TAX_ON_WEALTH
               
                if count % EVERY_THIRD_OPERATION == 0:
                    balans = balans + balans * INTEREST_FOR_OPERATIONS
                    return f'Начислен процент по счету за операции: {(balans * INTEREST_FOR_OPERATIONS):.2f} ' \
                        f'Удержан налог на богаство в размере 10% и равен:{nalog:.2f} Баланс равен:{balans:.2f}', entrance
                return f'Удержан налог на богаство в размере 10% и равен:{nalog:.2f} Баланс равен:{balans:.2f}', entrance
            
            if MAX_LIMIT > balans>= 0:
                
                count += 1
                balans = balans + replenishment_amount
                entrance.append(replenishment_amount)

                if count % EVERY_THIRD_OPERATION == 0:
                    balans = balans + balans * INTEREST_FOR_OPERATIONS
                    return f'Баланс равен:{balans:.2f}. Начислен процент по счету за операции: {(balans * INTEREST_FOR_OPERATIONS):.2f}', entrance
                return f'Баланс равен:{balans:.2f}', entrance
                
               
        if relenishment_of_the_client in withdrawal and replenishment_amount % MIN_WITHDRAWAL_AND_RELENISHMENT == 0:    # Снять
            count += 1
            if replenishment_amount > balans:             # Нельзя снять больше чем на счете
                return f'Нельзя снять больше чем на счете Баланс равен:{balans}'
            else:
                if replenishment_amount * WITHDRAWAL_PERCENTAGE < MIN_WITHDRAWAL:
                    withdrawal_.append(replenishment_amount)
                    balans = balans - MIN_WITHDRAWAL - replenishment_amount
                    return 'Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.' '\n'\
                            f'Процент снятия равен: {MIN_WITHDRAWAL}' '\n'\
                            f'Баланс равен:{balans:.2f}' '\n'\
                            f'{withdrawal_}'
                    
                elif replenishment_amount * WITHDRAWAL_PERCENTAGE > MAX_WITHDRAWAL:
                    withdrawal_.append(replenishment_amount)
                    balans = balans - MAX_WITHDRAWAL - replenishment_amount
                    return 'Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.' '\n'\
                            f'Процент снятия равен: {MAX_WITHDRAWAL}' '\n'\
                            f'Баланс равен:{balans:.2f}', withdrawal_
                            


                else:
                    withdrawal_.append(replenishment_amount)
                    balans = balans - balans * WITHDRAWAL_PERCENTAGE  
                              
                    
            
            if count % EVERY_THIRD_OPERATION == 0:
                    if balans  > MAX_LIMIT: 
                        nalog = balans * TAX_ON_WEALTH
                        balans = balans - balans * TAX_ON_WEALTH
                        return f'Начислен процент по счету за операции: {(balans * INTEREST_FOR_OPERATIONS):.2f}' '\n'\
                            f'Баланс равен:{(balans + balans * INTEREST_FOR_OPERATIONS):.2f}''\n'\
                            'Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.' '\n'\
                            f'Процент снятия равен: {(replenishment_amount * WITHDRAWAL_PERCENTAGE):.2f}' '\n'\
                            f'Удержан налог на богаство в размере 10% и равен:{nalog:.2f}.' '\n'\
                            f'Баланс равен:{balans:.2f}', withdrawal_   
                    else:
                        return f'Начислен процент по счету за операции: {(balans * INTEREST_FOR_OPERATIONS):.2f}' f'Баланс равен:{(balans + balans * INTEREST_FOR_OPERATIONS):.2f}'
                
            if balans  > MAX_LIMIT: 
                    nalog = balans * TAX_ON_WEALTH
                    balans = balans - balans * TAX_ON_WEALTH
                    return f'Удержан налог на богаство в размере 10% и равен:{nalog:.2f}.' '\n'\
                       'Удержан процент за снятие  в размере 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.' '\n'\
                       f'Процент снятия равен: {(replenishment_amount * WITHDRAWAL_PERCENTAGE):.2f}' '\n'\
                       f'Баланс равен:{balans:.2f}',withdrawal_ 
                
           
                

            
        else:
            if balans  > MAX_LIMIT: 
                nalog = balans * TAX_ON_WEALTH
                balans = balans - balans * TAX_ON_WEALTH
                return f'Сумма пополнения и снятия кратны 50 y.e. Удержан налог на богаство в размере 10% и равен:{nalog:.2f} Баланс равен:{balans:.2f}'
            else:
                return f'Сумма пополнения и снятия кратны 50 y.e. Баланс равен:{balans:.2f}'
        



        return f'Баланс равен:{balans:.2f}' '\n'\
                f'{entrance}' '\n'\
                f'{withdrawal_}'
                
    
    print(relenishment_(relenishment_of_the_client, replenishment_amount))
                    
    return ATM_machine(balans, count, entrance, withdrawal_)


exit_from_the_program = 'Выход', 'выход', 'выхот', 'ВЫХОТ', 'Выхот', 'ds[jl', 'Ds[jl'
relenishment = 'Пополнить', 'пополнить', 'ПОПОЛНИТЬ', 'ПОПОЛНИТ', 'Пополнит', 'ПАПОЛНИТЬ', 'ПАПОЛНИТ', 'паполнить', 'паполнит', 'gjgjkybnm', 'Gjgjkybnm'
withdrawal = 'Снять', 'снять', 'снят', 'Снят'
balans = 0
count = 0
entrance = []
withdrawal_= []
print(ATM_machine(balans, count, entrance, withdrawal_))