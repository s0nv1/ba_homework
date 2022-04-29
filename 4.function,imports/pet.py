import dicer

def vpered(n):
	print(f'{n} шагов вперед')

def nazad(n):
	print(f'{n} шагов назад')

def golos(say):
	print(f'{say}!!! {say}!!!')

print(dicer.dice())
print(dicer.grah_dice())
print(dicer.universal_dice(10))
print(dicer.vedro_kubov(k=10))
