import turtle as t 
from random import randint


current_position = -400

def main():
	t.bgcolor('black')
	t.pencolor('white')
	t.up()
	t.setpos(current_position, 0)
	n = [int(i) for i in input()]
	num_dict = {1:one, 
				2:two, 
				3:three, 
				4:four, 
				5:five, 
				6:six,
				7:seven,
				8:eight,
				9:nine,
				0:zero}
	for i in n:
		num_dict[i]()
	t.done()

def one():
	global current_position
	current_position += 70
	t.up()
	t.forward(50)
	t.down()
	t.left(90)
	t.forward(100)
	t.left(135)
	t.forward(50)
	t.up()
	t.left(45)
	t.left(90)
	t.setpos(current_position, 0)

def two():
	global current_position
	current_position += 70
	t.left(90)
	t.forward(100)
	t.down()
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.up()
	t.forward(20)

def three():
	global current_position
	current_position += 70
	t.left(90)
	t.forward(100)
	t.right(90)
	t.down()
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(180)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(180)
	t.up()
	t.forward(70)

def four():
	global current_position
	current_position += 70
	t.forward(50)
	t.down()
	t.left(90)
	t.forward(100)
	t.up()
	t.left(90)
	t.forward(50)
	t.left(90)
	t.down()
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.up()
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(20)

def five():
	global current_position
	current_position += 70
	t.down()
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.up()
	t.forward(100)
	t.left(90)
	t.forward(20)

def six():
	global current_position
	current_position += 70
	t.down()
	for i in range(4):
		t.forward(50)
		t.left(90)
	t.left(90)
	t.forward(100)
	t.right(90)
	t.forward(50)
	t.up()
	t.right(90)
	t.forward(100)
	t.left(90)
	t.forward(20)

def seven():
	global current_position
	current_position += 70
	t.left(90)
	t.forward(100)
	t.right(90)
	t.down()
	t.forward(50)
	t.right(90)
	t.forward(100)
	t.up()
	t.left(90)
	t.forward(20)

def eight():
	global current_position
	current_position += 70
	t.down()
	for i in range(4):
		t.forward(50)
		t.left(90)
	t.left(90)
	t.forward(50)
	for i in range(3):
		t.forward(50)
		t.right(90)
	t.left(90)
	t.up()
	t.forward(50)
	t.left(90)
	t.forward(20)

def nine():
	global current_position
	current_position += 70
	t.down()
	t.forward(50)
	t.left(90)
	t.forward(100)
	for i in range(3):
		t.left(90)
		t.forward(50)
	t.up()
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(20)

def zero():
	global current_position
	current_position += 70
	t.down()
	for i in range(2):
		t.forward(50)
		t.left(90)
		t.forward(100)
		t.left(90)
	t.up()
	t.forward(70)

main()
