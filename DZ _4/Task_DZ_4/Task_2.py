# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def slovar(**a):
    d = {k: str(v) for k, v in a.items()}

    e = {}
 
    for key, value in d.items():
        if value in e:
            e[value].append(key)
        else:
            e[value] = [key]
        
            
    return e


print(slovar(chemistry=5, Biology=3, Physics=5, Mathematics=4))
