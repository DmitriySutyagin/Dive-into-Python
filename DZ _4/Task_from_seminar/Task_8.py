# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replacement(**a):
   
    e = { k : v for k, v in a.items()}
    d = {k : None for k, v in a.items()  if k.endswith('s')}   

    
    return e , d 




runs = ['str']
bag = 67
let = True
murs = False
     
print(replacement(runs=['str'], bag=67, let=True, murs=False))