# Создайте строку fio ФИО
fio = 'Иванов Иван Иванович'

# Длина 
print(len(fio), end='\n\n')

# С помощью функции .split() получите список
fio_list = fio.split()
print(fio_list, end='\n\n')

# Создайте переменные name, fam, otch
fam, name, otch = fio_list[0], fio_list[1], fio_list[2]
print(f'''Fam: {fam}
Name: {name}
Otch: {otch}
''') 

# Посчитайте с помощью функции count() количество букв о, е
print(f'Количество о: {fio.count("о")}', 
	f'Количество е: {fio.count("е")}', sep='\n', end='\n\n')

# Создайте новую переменную fio_s
fio_s = 'Сапко\nИгорь\tЕвгеньевич'
print(fio_s)
