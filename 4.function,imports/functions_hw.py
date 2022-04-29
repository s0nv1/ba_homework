import random

def squer(a):
	return (a * 4, a**2, a*2**0.5)

def season(num):
	sea = {'зима':(12, 1, 2), 
	'весна':(3, 4, 5), 
	'лето':(6, 7, 8),
	'осень':(9, 10, 11)}
	return [key for key in sea if num in sea[key]]

def dice():
	return random.randint(1, 6)

def grah_dice():
	dice = {1:'⚀', 2:'⚁', 3:'⚂', 4:'⚃', 5:'⚄', 6:'⚅'}
	return dice[random.randint(1, 6)]

def universal_dice(n=6):
	return random.randint(1, n)
	
def vedro_kubov(n=6,k=1):
	return [random.randint(1, n) for i in range(k)]

print(squer(5))
print(season(1))
print(dice())
print(grah_dice())
print(universal_dice(10))
print(vedro_kubov(k=10))
