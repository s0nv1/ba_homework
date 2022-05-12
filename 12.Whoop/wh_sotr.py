
class Person:
    count = 0
    staff = 0
    all_salary = 0
    
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.new_person(self.status, self.salary)

        
    @classmethod
    def new_person(cls, status, salary):
        cls.count += 1
        cls.staff += 1 if status != 'Detailee' else 0
        cls.all_salary += salary
    

    
    def del_person(self):
        del self
    
    def __repr__(self):
        return f'{self.name}'


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
wh.rep()

print(Person.count)
print(Person.staff)
print(Person.all_salary)
print(len(wh.sotr))

wh.sotr[1].del_person()
print(Person.count)
print(Person.staff)
print(Person.all_salary)
print(len(wh.sotr))

