# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonachi(n):
    fiba = []            
    for i in range(n):
        if (i)+(i-1) <= 0:
            fiba.append(i)
            yield fiba
        elif (i)+(i-1) == 1:
            fiba.append(i)
            yield fiba
        else:
            fiba.append(fiba[i-2]+fiba[i-1])
            yield fiba

        
 
fib_digit = int(input('Enter number: '))
a = fibonachi(fib_digit)
while fib_digit != 0:
    print(next(a))   
    fib_digit =-1 
                            # Функция next() применена для демострации решения