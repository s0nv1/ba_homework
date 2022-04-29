import random

def dice():
	return random.randint(1, 6)

def grah_dice():
	dice = {1:'⚀', 2:'⚁', 3:'⚂', 4:'⚃', 5:'⚄', 6:'⚅'}
	return dice[random.randint(1, 6)]

def universal_dice(n=6):
	return random.randint(1, n)
	
def vedro_kubov(n=6,k=1):
	return [random.randint(1, n) for i in range(k)]

