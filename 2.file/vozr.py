fio = open('fio.txt', 'r')
line = fio.read().split()
fio.close()

print(f'Добрый день {line[1]}! Ваш возраст {2022 - int(line[3])} лет!')
