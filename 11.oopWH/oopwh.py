

class Employee:
    def __init__(self, lis: list):
        self.lis = [i.strip() for i in lis]
        self.name, self.status, self.salary, self.pay_basis, self.position_title = self.lis
        self.salary = float(self.salary.replace(',', '').replace('$',''))
    
    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        return f'{self.name}'
    
    def get_salary(self):
        return self.salary
    
    def get_position_title(self):
        return self.position_title
    
    def get_name(self):
        return self.name
        
        
class WH:
    def __init__(self, fil):
        self.fil = fil
        self.sort_list = []
        self.__open_fil()
    
    def __open_fil(self):
        with open(self.fil) as f:
            read = f.readlines()
        l = []
        for line in read[1:]:
            line = line.split(';')
            l.append(Employee(line))
        self.sort_list = l
        self.amount_sotr = len(self.sort_list)
        
    def middle_salary(self):
        all_salary = 0
        for per in self.sort_list:
            all_salary += per.salary
        return all_salary / self.amount_sotr
        
    def top10_most_reach(self):
        new_list = sorted(self.sort_list, key=Employee.get_salary, reverse=True)[:10]
        return new_list
    
    def middle_sal_stass(self):
        all_salary = 0
        for per in self.sort_list:
            if per.position_title == "STAFF ASSISTANT":
                all_salary += per.salary
        return all_salary / self.staffass_amount()
    
    def amount_per_on_work_title(self):
        list_title = list(set(i.position_title for i in wh.sort_list))
        list_title.sort()
        text = ''
        text += f'Количество должностей: {len(list_title)}\n'
        for line in list_title:
            text += f'{line}\n'
        return text
    
    def position_st(self):
        s, text = {}, ''
        new_list = sorted(self.sort_list, key=Employee.get_position_title)
        for per in new_list:
            if per.position_title in s:
                s[per.position_title] += 1
            else:
                s[per.position_title] = 1
        for k, v in s.items():
            text += f'Amount: {v}, title: {k}\n'
        return text
            
    def detailee_amount(self):
        amount = 0
        for per in self.sort_list:
            if per.status == 'Detailee':
                amount += 1
        else:
            return amount
    
    def staffass_amount(self):
        amount = 0
        for per in self.sort_list:
            if per.position_title == "STAFF ASSISTANT":
                amount += 1
        else:
            return amount


wh = WH('wh.csv')

print(wh.middle_salary())
print(wh.top10_most_reach())
print(wh.detailee_amount())
print(wh.staffass_amount())
print(wh.middle_sal_stass())
print(wh.amount_per_on_work_title())
print(wh.position_st())

