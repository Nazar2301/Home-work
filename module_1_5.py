immutable_var = 1, 2, 3, True, "helloy"
print(immutable_var)
print(type(immutable_var)) # Класс 'tuple' - неизменяемый кортеж
mutable_list = [1, 2, 'a', 'b', 'text']
print(mutable_list)
mutable_list[0] = 9
print(mutable_list)
print(type(mutable_list)) # Класс 'list' - изменяемый список