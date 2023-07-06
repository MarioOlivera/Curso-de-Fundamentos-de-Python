# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 10
print(numbers)

'''AGREGANDO ELEMENTO AL FINAL'''
numbers.append(700)
print(numbers)

'''AGREGANDO ELEMENTO AL PRINCIPIO'''
numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, '"change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

'''FUSIONANDO'''
new_list = numbers + tasks

print(new_list)

'''OBTENIENDO POSICION DE UN ELEMENTO'''
index = new_list.index('todo 2')
new_list[index] = 'todo 2 changed'
print(new_list)

'''ELIMINANDO ELEMENTO'''
new_list.remove('todo 1')
print(new_list)

'''ELIMINANDO ULTIMO ELEMENTO DE LA LISTA'''
new_list.pop()
print(new_list)

'''ELIMINANDO PRIMERA POSICION'''
new_list.pop(0)
print(new_list)

'''DANDO VUELTA EL ORDENAMIENTO DE LA LISTA'''
new_list.reverse()
print(new_list)

'''ORDENANDO LISTA'''
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()
print(new_list)