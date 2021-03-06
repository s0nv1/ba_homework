
class Person:
    count = 0
    staff = 0
    all_salary = 0
    st_ass = []
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.new_person(self.status, self.salary)
        if self.position_title == 'STAFF ASSISTANT':
            self.__class__.st_ass.append(self)
        
    @classmethod
    def new_person(cls, status, salary):
        cls.count += 1
        cls.staff += 1 if status != 'Detailee' else 0
        cls.all_salary += salary

    def __repr__(self):
        return f'{self.name}'
    
    def __del__(self):
        self.__class__.count -= 1
        self.__class__.staff -= 1 if self.status != 'Detailee' else 0
        self.__class__.all_salary -= self.salary
        if self.position_title == 'STAFF ASSISTANT':
            del self.__class__.st_ass[self.__class__.st_ass.index(self)]
    
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
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
    def recount(self):
        Person.all_salary = sum((per.salary for per in self.sotr))
        return Person.all_salary
    
        
wh = WH('wh.csv')

print(Person.count)
print(len(Person.st_ass))

del wh.sotr[-1]
wh.rep()
print(len(Person.st_ass))
print(Person.st_ass)

print(Person.count)



