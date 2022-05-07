# 1 task
def fun():
    a = 1
    b = 2
    c = 3

print(fun.__code__.co_nlocals) # круто)

# 2 task

def change_text(n):
    def text_lower(text): # n=1
        return text.lower() 
    def text_upper(text): # n=2
        return text.upper()
    def text_swapcase(text):# n!=1 and n!=2
        return text.swapcase()
    if n == 1:
        return text_lower
    elif n == 2:
        return text_upper
    else:
        return text_swapcase

textlow = change_text(1)
textup = change_text(2)
textscase = change_text(3)

print(textlow('Hello World!'))
print(textup('Hello World!'))
print(textscase('Hello World!'))
