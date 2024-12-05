def devide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        print('Ошибка!')
    else:
       return print(round(result, 5))

