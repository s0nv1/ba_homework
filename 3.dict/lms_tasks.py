# Task 1
import string 


text = [word if word[-1] not in string.punctuation \
		else word[:-1] for word in input().lower().split()]

count = 1
dicto = {}

for word in text:
	if word in dicto:
		dicto[word] += count 
	else:
		dicto[word] = count

for k, v in dicto.items():
	print(k, v)

# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def summa_stock(stock, price):
	return sum([stock[item] * price[item] for item in stock])

print(f'Total price: ${summa_stock(stock, prices):.2f}')
