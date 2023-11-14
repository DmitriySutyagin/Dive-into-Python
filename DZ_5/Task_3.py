# # ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fiba(n):
    # fibas_2 =[0, 1, 1]



    # if 
    # for i in fibas_2 :
    for i in range(2, n):
        n = n-1+ n-2
        print(i)

        yield n
        
        

    



fiba(10)

