immutable_var = 1, 3, False, 'Hey dude'
print(immutable_var)
print('Изменение кортежа невозможно, т.к это хранилище неизменяемых данных, кроме случаев, когда кортеж включает всебя список.')
immutable_var_1 = ([1, 3, False], 'Hey dude')
immutable_var_1[0][2] = True
print('Например: ',immutable_var_1 )
muttable_list = [1, 2, False, 'whats up?']
muttable_list [3] = 'good luck!'
print(muttable_list)