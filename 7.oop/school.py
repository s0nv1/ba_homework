class Person:
	def __init__(self, 
				fname, 
				lname, 
				age, 
				num_school, 
				main_class,
				lesson_today, 
				status,
				num_tel,
				home_street):
		self.fname = fname
		self.lname = lname
		self.age = age
		self.num_school = num_school
		self.main_class = main_class
		self.lesson_today = lesson_today
		self.status = status
		self.num_tel = num_tel
		self.home_street = home_street
		
	def change_full_name(self, fname, lname):
		self.fname = fname
		self.lname = lname
	
	def change_age(self, age):
		self.age = age
	
	def change_shcool(self, num):
		self.num_school = num
	
	def change_lessons_today(self, num):
		self.lessons_today = num
	
	def change_status(self, status):
		self.status = status
	
	def change_main_class(self, new_class):
		self.main_class = new_class
	
	def change_num_tel(self, new_tel):
		self.num_telephone = new_tel
	
	def change_home_street(self, new_street):
		self.home_street = new_street
	
	def public_info(self):
		print(f'''Public information.
fname: {self.fname}
lname: {self.lname}
age: {self.age} years
num_school: N{self.num_school}
class: {self.main_class}
lesson_today: {self.lesson_today}
status: {self.status}''')


class Teacher(Person):
	def __init__(self, 
				fname, 
				lname, 
				age, 
				num_school,
				main_class,
				lesson_today,
				status, 
				num_tel,
				home_street,
				subject,
				salary,
				years_of_exp,
				years_of_work_in_sch,):
		super().__init__(fname, 
						lname, 
						age, 
						num_school, 
						main_class, 
						lesson_today,
						status,
						num_tel,
						home_street)
		self.one_year_salary_cons = 50
		self.subject = subject
		self.salary = salary  
		self.full_salary = salary + years_of_exp * self.one_year_salary_cons
		self.years_of_exp = years_of_exp
		self.years_of_work_in_sch = years_of_work_in_sch
	
	def change_stand_salary(self, salary):
		self.salary = salary
		self.full_salary = salary + self.years_of_exp * self.one_year_salary_cons
	
	def change_year_of_exp(self):
		self.years_of_exp += 1
		self.years_of_work_in_sch += 1
		self.full_salary = self.salary + self.years_of_exp * 50
	
	def private_info(self):
		print(f'''Private information.
Standart salary: ${self.salary:.2f}
Full salary: ${self.full_salary:.2f}
Expiriance: {self.years_of_exp} years
Work in school: {self.years_of_work_in_sch} years
Num telefon: {self.num_tel}
Home street: {self.home_street}
''')


class Student(Person):
	def __init__(self, 
				fname, 
				lname, 
				age, 
				num_school, 
				main_class,
				lesson_today, 
				status,
				num_tel,
				home_street
				):
		super().__init__(fname, 
				lname, 
				age, 
				num_school, 
				main_class,
				lesson_today, 
				status,
				num_tel,
				home_street)
	
		def add_parents(self):
			print('Add info about parents')
			self.moth_name = input('Mother name: ')
			self.moth_tell = input('Mother tell: ')
			self.fath_name = input('Father name: ')
			self.fath_tell = input('Mother tell: ')
		add_parents(self)
		
	def change_parents_info(self):
		self.moth_name = input('Mother name: ')
		self.moth_tell = input('Mother tell: ')
		self.fath_name = input('Father name: ')
		self.fath_tell = input('Mother tell: ')
	
	def private_info(self):
		print(f'''Private information
Num telephone: {self.num_tel}
Home address: {self.home_street}
Mother name: {self.moth_name}
Mother tell: {self.moth_tell}
Father name: {self.fath_name}
Father tell: {self.fath_tell}
''')


per = Teacher('John', 'Smith', 45, 55,'9b', 6,'Teacher',
			'123-234-3456', 'Frank 22, h1', 'math', 1000, 20, 5,)

stu = Student('Will', 'Smith', 16, 55, '10a', 7, "Student",
				'234-234-2355', 'Jone 77, h2')

per.private_info()
stu.private_info()
