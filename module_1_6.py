my_dict = {'Olga': 1980, 'Konstantin': 1984, 'Vika': 2002}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Saha'))
my_dict['Lena'] = 1997
my_dict['Ilya'] = 1998
print(my_dict)
a = my_dict.pop('Ilya')
print(my_dict)
print(a)
