def devide(first, second):
    from math import inf
    try:
        result = first / second
    except ZeroDivisionError:
        return print(inf)
    else:
        return print(round(result, 5))

