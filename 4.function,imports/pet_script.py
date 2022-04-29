import pet, random


def pet_script():
	count = 0
	for i in range(10):
		n = random.randint(1, 2)
		if n == 1:
			pet.vpered(10)
		else:
			pet.nazad(10)
		for j in range(10):
			count += 1
			pet.golos(count)

pet_script()


