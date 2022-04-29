f = open('az_morze.txt', 'r')
text = f.readlines()
f.close()

text = dict(tuple(ab.split()) for ab in text)
# Task 1
trans = [text[ab] for ab in input().upper() if ab in text]
print(*trans, sep=' ')
# Task 2
return_trans = [key for ab in input().split() for key,value in text.items() \
				if ab == value]
print(*return_trans, sep=' ')
