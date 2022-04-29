file_t = open('weather.log', 'r', encoding='utf-8')
temp = file_t.readlines()
file_t.close()
sum_t = 0 # Сумма темп.
count_line = 0 # Количество дней
for line in temp:
	if '-10-' in line:
		count_line += 1
		temp_int = int(line.split()[2].replace('°C,',''))
		sum_t += temp_int
print(f'Средняя температура за Сентябрь: {sum_t/count_line:.2f}°C',
		f'\nКоличество дней с Сентября было взято: {count_line}')


