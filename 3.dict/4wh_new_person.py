s = open('white_house_2017_salaries_com.csv')
read = s.readlines()
s.close()

people = []
fline = read[0].strip().split(';')

for line in read[1:]:
	l = line.split(';')
	d = {}
	for num, title in enumerate(fline):
		d[title] = l[num]
	people.append(d)


def new_person():
	s = open('white_house_2017_salaries_com.csv', 'a')
	dict_per = {}
	for i in fline:
		info = input(f'{i}:')
		dict_per[i] = info
		if fline.index(i) == len(fline) -1:
			s.write(f'{info}\n')
		else:
			s.write(f'{info};')
	people.append(dict_per)
	s.close()

new_person()
	
