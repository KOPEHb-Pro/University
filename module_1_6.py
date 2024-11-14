my_dict = {'Kostya': 1995, 'Dasha':1994, 'Ivan': 2001, 'Vasya': 1993 }
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Kolya', 'Год рождения не найден.'))
my_dict.update({'Kolya': 2003, 'Dima': 2023})
V = my_dict.pop('Vasya')
print(V)
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 3, True, False, True, (1,2,3,4), (1,2,3), (1,2,3)}
print(my_set)
my_set.add('Hello')
my_set.add(12.45)
my_set.discard((1,2,3))
print(my_set)