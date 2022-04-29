class Dog:
	age_factor = 7
	
	def __init__(self, age):
		self.dog_age = age
	
	def human_age(self):
		return self.dog_age * self.age_factor


dog = Dog(3)
print(dog.human_age())

