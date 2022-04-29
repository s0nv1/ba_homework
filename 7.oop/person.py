class Person:
	def __init__(self, name, fam, age):
		self.firstname = name
		self.lastname = fam
		self.age = age
		
	def talk(self):
		print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old!')


s = Person('Vasya', 'Pypkin', 23)
s.talk()
