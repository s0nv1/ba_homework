file_his = open('weather_his.csv', 'r', encoding='utf-8')
lines = file_his.readlines()
file_his.close()

sum_pressure = 0

for line in lines:
	sum_pressure += float(line.split()[13])

print(f'Среднее давление за день: {sum_pressure/len(lines):.2f} in')
