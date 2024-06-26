immutable_var = (1, 'one', False, 5.9, [56, 258, 66, 2])
print('Immutable tuple:', immutable_var)

# immutable_var[1] = 'two'  # вызовет ошибку, т. к. элемент кортежа - строка, неизменяемый объект
# immutable_var[0] = immutable_var[0] + 10  # тоже вызовет ошибку, т. к. элемент кортежа - число, неизменяемый объект
immutable_var[4][3] = immutable_var[4][3] * 2  # здесь ошибки нет, т. к. элемент кортежа - список, изменяемый объект

mutable_list = [1, 'one', False, 5.9, immutable_var]
mutable_list[0] = mutable_list[0] + 10
mutable_list[1] = 'two'
mutable_list[2] = True
mutable_list[3] = 'пять и девять десятых'
print('Mutable list:', mutable_list)
