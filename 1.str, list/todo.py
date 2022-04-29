# Задайте переменную todo
todo = ['поспать', 'проснуться', 'зарядка', 'утренние процедуры', 
		'завтрак', 'учеба', 'сон'] 

# 1.2 Распечатайте первый, третий, четвертый, 
# и последний элементы списка.
print(todo[0], todo[2], todo[3], todo[-1], end='\n\n')

# 1.3 Разбейте с помощью срезов список на две части - 
# в первой части три элемента, во второй - четыре.
print(todo[:3], todo[3:], sep='\n', end='\n\n')

# 1.4. Добавьте к списку дел еще одно или два (через append).
todo.append('работа')
todo.append('кино')
print(todo, end='\n\n')

# (*) Поменяйте местами первое и последнее дело в списке.
todo[0], todo[-1] = todo[-1], todo[0]
print(todo, end='\n\n')

# (*) Спросите пользователя про следующее дело и добавьте его в список.
todo.append(input('Введите ваше следущее дело: '))
print(todo, end='\n\n')

# (**) Скопируйте список todo в четыре других списка
todo2 = todo
todo3 = list(todo)
todo4 = todo.copy()
todo5 = todo[:]

print(f'id todo: {id(todo)}')
print(f'id todo2: {id(todo2)}')
print(f'id todo3: {id(todo3)}')
print(f'id todo4: {id(todo4)}')
print(f'id todo5: {id(todo5)}')





