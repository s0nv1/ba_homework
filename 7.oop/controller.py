
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
	def __init__(self, channels):
		self.channels = channels
		self.curr_channel = 0
	
	def first_channel(self):
		self.curr_channel = 0
		return self.channels[self.curr_channel]
	
	def last_channel(self):
		self.curr_channel = 2
		return self.channels[self.curr_channel]
	
	def turn_channel(self, n):
		self.curr_channel = n - 1
		return self.channels[self.curr_channel]
	
	def next_channel(self):
		self.curr_channel = 0 if self.curr_channel + 1 > 2 else self.curr_channel + 1
		return self.channels[self.curr_channel]
	
	def previous_channel(self):
		self.curr_channel = 2 if self.curr_channel - 1 < 0 else self.curr_channel - 1
		return self.channels[self.curr_channel]
	
	def current_channel(self):
		return self.channels[self.curr_channel]
	
	def is_exist(self, n):
		if n == str(n):
			return 'YES' if n in self.channels else 'NO'
		else:
			return 'YES' if 1 <= n <= 3 else 'NO'


cont = TVController(CHANNELS)

print(cont.first_channel())
print(cont.last_channel())
print(cont.turn_channel(3))
print(cont.next_channel())
print(cont.previous_channel())
print(cont.current_channel())
print(cont.is_exist(4))
print(cont.is_exist('BBC'))
