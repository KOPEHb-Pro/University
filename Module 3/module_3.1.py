calls = 0

def string_info(string):
    tuple_ = len(string), string.upper(), string.lower()
    print(tuple_)
    count_calls()
    return

def  is_contains(string, list_to_search):
    list_to_search_lower = [s.lower() for s in list_to_search]
    if string.lower() in list_to_search_lower:
        print(True)
    else:
        print(False)
    count_calls()
    return

def count_calls():
    global calls
    calls += 1
    return

string_info('Hello')
string_info('Whats yor name')
string_info('Whats up?')

is_contains('WinD', ['wind', 'plane', 'trees'])
is_contains('Vasya', ['Petya', 'Kolya', 'VASya'])
is_contains('Book', ['noTeBook', 'pRIntbook', 'GROSbook'])

print('Количество выполненных операций: ', calls)
