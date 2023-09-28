from Date_existence import date


def leap(data_leap: str):
    """   """
    *_, suffix = data_leap.split('.')
    if int(suffix) % 4 == 0 and (int(suffix) % 100 != 0 or int(suffix) % 400 == 0):
        return f"{int(suffix)} является високосным годом"
    else:
        return f"{int(suffix)} не является високосным годом"
    

print(leap(date))