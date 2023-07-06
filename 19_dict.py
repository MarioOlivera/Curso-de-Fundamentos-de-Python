my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict = {
    'avion' : 'bla bla bla',
    'name' : 'Mario',
    'last_name': 'Olivera',
    'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('no_existe'))

print('avion' in my_dict)
print('no_existe' in my_dict)