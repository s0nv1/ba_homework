f = open('wh_salaries.csv', 'r')
t = f.readlines()
f.close()

hr = []
headers = t[0].split(';')

salary_summe = 0

names = []
salary = []

for i in t[1:]:
	s = i.split(';')
	k = {}
	for n,h in enumerate(headers):
		if h == 'SALARY':
			k[h] = float(s[n][1:].replace(',',''))
		else:
			k[h] = s[n]
		
	hr.append(k)

print(hr)


