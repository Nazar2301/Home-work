first = input('Ввидите первое число: ')
second = input('Видите второе число: ')
third = input('Ввидите третье число: ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)
