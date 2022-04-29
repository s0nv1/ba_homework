class Mathematician:
	def square_nums(self, lis):
		return [num**2 for num in lis]
	
	def remove_positives(self, lis):
		return [num for num in lis if num < 0]
	
	def filter_leaps(self, lis):
		return [year for year in lis \
		if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
