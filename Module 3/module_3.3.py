def print_params(a = 1, b = 'Cтрока', c = True):
    print(a, b, c)

print_params()

print_params(b = 25, c = [1, 2, 3])

values_list = [1.1, 'Hi' , False]
values_dict = {'a': 1.2, 'b': 'Bye', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1.3, 'Hello']

print_params(*values_list_2, 42)