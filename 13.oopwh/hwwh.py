class Person:

    count = 0
    staff = 0
    all_salary = 0
    staff_salary = 0
    staff_assistants = []
    
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.__class__.count += 1
        self.__class__.all_salary += self.salary
        if self.status != "Detailee":
            self.__class__.staff += 1
            self.__class__.staff_salary += self.salary
        if self.position_title == 'STAFF ASSISTANT':
            self.__class__.staff_assistants.append(self)

    # 1 task
    @classmethod
    def report(cls):
        print(f'''Всего {cls.count} сотрудников, 
Общая зарплата ${cls.all_salary}, 
Средняя зарплата ${cls.all_salary // cls.count}, 
Средняя зарплата штатных сотрудников ${cls.staff_salary // cls.staff}
        ''')
    # 3 task
    @classmethod
    def assistants_report(cls):
        for per in cls.staff_assistants:
            print(f'assistant: {per.name} / salary: ${per.salary}')
    
    def __repr__(self):
        return self.name
    
    def __del__(self):
        person = self.__class__
        person.count -= 1
        person.all_salary -= self.salary
        if self.status != "Detailee":
            person.staff -= 1   
        if self.position_title == 'STAFF ASSISTANT':
            index = self.__class__.staff_assistants.index(self)
            self.__class__.staff_assistants = self.__class__.staff_assistants[:index] \
            + self.__class__.staff_assistants[index + 1:]
    
class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)
        
    def get_sotr(self, name_file):
        f = open(name_file, 'r')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$','').replace(',',''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)
    
    def recount(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        Person.all_salary = su
        
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        return su/len(self.sotr)
        
    def top10(self):
        def sal(i):
            return i.salary
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse = True)
        return top2[:10]

    def detailees(self):        
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):        
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT'])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
    def count_sotr(self):
        print(f'''Всего {Person.count} сотрудников, 
из них {Person.staff} на постоянной основе
общий заработок {Person.all_salary}''')

    # 4 task
    @staticmethod 
    def sum_salary(lis):
        return sum([per.salary for per in lis])
    
    # 5 task
    @staticmethod
    def avg_salary(lis):
        zp = [per.salary for per in lis]
        return sum(zp) // len(zp)
    
wh = WH('white_house_2017_salaries_com.csv')
Person.report()
#Person.assistants_report()
#print(wh.sum_salary(Person.staff_assistants[1:5]))
#print(wh.avg_salary(Person.staff_assistants[1:5]))
print(wh.sotr[-1])
print(len(wh.sotr))
del wh.sotr[-1]
print(len(wh.sotr))
print(Person.staff_assistants)
