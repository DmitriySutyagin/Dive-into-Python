# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def slovar(**a):
    d = {k: str(v) for k, v in a.items()}

<<<<<<< HEAD
def slovar(*, a, b):
    for i in b_1:
        {b[i] : a[i]}
        
    return {b : a}



a_1, *_ = input('Enter a nember and a value separated by a space: ').split()
b_1, *_ = input('Enter a nember and a value separated by a space: ').split()
# print(c, *_)
print(slovar(a=a_1, b=b_1))
=======
    e = {}
 
    for key, value in d.items():
        if value in e:
            e[value].append(key)
        else:
            e[value] = [key]
        
            
    return e


print(slovar(chemistry=5, Biology=3, Physics=5, Mathematics=4))
>>>>>>> 35560218d1e670ca88ae89d8ba0b9e06e8dd3f0c
