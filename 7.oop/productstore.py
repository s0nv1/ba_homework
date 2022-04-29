class Product:
	def __init__(self, info):
		self.typ, self.name, self.price = info


class ProductStore:
	def __init__(self):
		self.all_products = {}
		self.income = 0
	
	def add(self, product, amount):
		self.all_products[product.name] = \
		[product.typ, product.price + product.price * 0.3, product.amount + amount \
		 if len(self.all_products[product.name]) == 3 else amount]
	
	def set_discount(self, percent, identifier='name', identifier_type='name'):
		flag = True
		for name, info in self.all_products.items():
			if name == identifier or info[0] == identifier_type:
				self.all_products[name][1] = \
				self.all_products[name][1] - self.all_products[name][1] * percent / 100
				flag = False
		if flag:
			raise ValueError('Нет такого названия или типа товара')
			
	def sell_product(self, name, amount):
		if amount <= self.all_products[name][2]:
			self.all_products[name][2] -= amount
			self.income += amount * self.all_products[name][1]
		else:
			raise ValueError('Превышает количество на складе')
		
	def get_income(self):
		return self.income
	
	def get_all_products(self):
		if len(self.all_products) > 0:
			for name, info in self.all_products.items():
				print(f'Name: {name}, type: {info[0]}, price: {info[1]}, amount: {info[2]}')
		else:
			raise ValueError("На данный момент склад пуст")
	
	def get_product_info(self, name):
		if name in self.all_products:
			return (name, self.all_products[name][2])
		else:
			raise ValueError('Нет такого товара')
 
p = Product(('Sport', 'Football T-Shirt', 100))
p2 = Product(('Food', 'Ramen', 1.5))
p3 = Product(('Sport', 'Adidas', 80))

shop = ProductStore()

shop.add(p, 100)
shop.add(p2, 300)
shop.add(p3, 100)

print(shop.__dict__)
