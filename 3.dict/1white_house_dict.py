f = open('white_house_2017_salaries_com.csv', 'r')
read = f.readlines()
f.close()

first_line = read[0].split(';')
all_person = []

for line in read[1:]:
	l = line.strip().split(';')
	dic = {}
	for n, name in enumerate(first_line):
		dic[name.strip()] = l[n].strip()
	all_person.append(dic)

def salary_lowest(dic):
	low = 10**6
	per = ''
	for person in dic:
		if float(person['SALARY'][1:].replace(',','')) <= low:
			per = person['NAME']
			low = float(person['SALARY'][1:].replace(',',''))
	return per, low

def salary_high(dic):
	high = 0
	per = ''
	for person in dic:
		if float(person['SALARY'][1:].replace(',','')) >= high:
			per = person['NAME']
			high = float(person['SALARY'][1:].replace(',',''))
	return per, high

def middle_salary(dic):
	return sum([float(per['SALARY'][1:].replace(',','')) for per in dic]) \
	/ len(dic)

def top_10_big_salary(dic):
	top10 = [tuple([float(per['SALARY'][1:].replace(',','')), per['NAME']])\
	 for per in dic]
	return [name for name in sorted(top10, reverse=True)[:10]]
	
def status_per(dic):
	return len([per['NAME']for per in dic if per['STATUS'] == 'Detailee'])
	
def middle_salary_detail(dic):
	count = [float(per['SALARY'][1:].replace(',','')) for per in dic \
	if per['STATUS'] == 'Detailee']
	return sum(count)/len(count)

def staff_assistance(dic):
	return len([per['NAME'] for per in dic if per['POSITION TITLE'] == \
	'STAFF ASSISTANT'])

def mid_sal_staff_assist(dic):
	count = [float(per['SALARY'][1:].replace(',','')) for per in dic \
	if per['POSITION TITLE'] == 'STAFF ASSISTANT']
	return sum(count)/len(count)
	
def zero_salary(dic):
	return [per['NAME'] for per in dic if float(per['SALARY'][1:].replace(',','')) == 0.0]
	
print(salary_lowest(all_person))
print(salary_high(all_person))
print(middle_salary(all_person))
print(top_10_big_salary(all_person))
print(status_per(all_person))
print(middle_salary_detail(all_person))
print(staff_assistance(all_person))
print(mid_sal_staff_assist(all_person))
print(zero_salary(all_person))
