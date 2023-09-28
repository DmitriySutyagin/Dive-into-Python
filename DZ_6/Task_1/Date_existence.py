from sys import argv

def existence(data: list[int]):
    
    """ This function takes a date as a string as input and checks it for existence according to the Gregorian calendar. """

    res = []
    prefix, *_, suffix = data.split('.')
   
    if int(prefix) in range(1, 32):
        res.append(True)
    else:
        res.append(False)
    if int(*_) in range(1,13):
        res.append(True)
    else:
        res.append(False)
    if int(suffix) in range(1, 10000):
        res.append(True)
    else:
        res.append(False)
       
    return all(map(lambda x: x == True, res))


date = input('Emter date: ')

print(existence(date))