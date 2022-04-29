class White_house_salaries:
	'''Only for mod read!'''
	def __init__(self, file1):
		file_wh = open(file1, 'r', encoding='utf-8')
		lines_read = [line.split(';') for line in file_wh.readlines()[1:]]
		file_wh.close()
		self.__list_s = lines_read
	
	def put_new_file(self, new_file):
		file_wh = open(new_file, 'r', encoding='utf-8')
		lines_read = [line.split(';') for line in file_wh.readlines()[1:]]
		file_wh.close()
		self.__list_s = lines_read
	
	def get_files(self):
		return self.__list_s
		
	def the_lowest_salary(self):
		lowest = 10**6
		name = ''
		lowest_s = ''
		for line in self.__list_s:
			if int(line[2][1:-4].replace(',','')) <= lowest:
				name, lowest = line[0], int(line[2][1:-4].replace(',',''))
				lowest_s = line[2]
		return f'Lowest salary, Name: {name}, the lowest salary: {lowest_s[:-1]}'

	def the_biggest_salary(self):
		biggest = 0
		name = ''
		biggest_s = ''
		for line in self.__list_s:
			if int(line[2][1:-4].replace(',','')) >= biggest:
				name, biggest = line[0], int(line[2][1:-4].replace(',',''))
				biggest_s = line[2]
		return f'Biggest salary, Name: {name}, the biggest salary: {biggest_s[:-1]}'
	
	def middle_salary(self):
		sum_s = [int(line[2][1:-4].replace(',','')) for line in self.__list_s]
		return f'Middle salary: ${sum(sum_s)/len(sum_s):.2f}'
		
	def ten_biggest_salaries(self):
		all_sel = {line[0]: int(line[2][1:-4].replace(',','')) \
		for line in self.__list_s}
		ten_bidsel = sorted(list(all_sel.values()), reverse=True)[:10]
		ten_person = []
		count = 0
		while count < 11:
			for key, value in all_sel.items():
				if value in ten_bidsel:
					ten_person.append(key)
					count += 1
		return  f'List top10 big salaries: {ten_person[:10]}'
	
	def detailee_people(self):
		detailee = [person[0] for person in self.__list_s if 'Detailee' in person]
		return f'Detailee {len(detailee)} person'
	
	def salaries_detailee_people(self):
		sal_detailee = [int(person[2][1:-4].replace(',',''))  \
		for person in self.__list_s if 'Detailee' in person]
		return f'Middle salary detailees: ${sum(sal_detailee)/len(sal_detailee):.2f}'
		
	def count_staff_assistance(self):
		count_s_a = [person[0] for person in self.__list_s \
		if 'STAFF ASSISTANT' in person[4]]
		return f'There are {len(count_s_a)} staff assistants'
	
	def middle_salary_staff_ass(self):
		mid_sal = [int(person[2][1:-4].replace(',',''))  \
		for person in self.__list_s if 'STAFF ASSISTANT' in person[4]]
		return f'Middle salary staff assistant: ${sum(mid_sal)/len(mid_sal):.2f}'
		
	def zero_salary(self):
		zero_salary = [int(person[2][1:-4].replace(',','')) \
		for person in self.__list_s if int(person[2][1:-4].replace(',','')) == 0]
		return f'Don\'t pay for {len(zero_salary)} person'
		
s = White_house_salaries('wh_salaries.csv')
print(s.the_lowest_salary())
print(s.the_biggest_salary())
print(s.middle_salary())
print(s.detailee_people())
print(s.salaries_detailee_people())
print(s.count_staff_assistance())
print(s.middle_salary_staff_ass())
print(s.zero_salary())
print(s.ten_biggest_salaries())



