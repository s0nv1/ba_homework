
def arg_rules(type_: str, max_length: int, contains: list):
    def function(func):
        def wrapper(*args, **kwgs):
            word, = args
            if type(word) != type_:
                print(f'Не тот тип! {word}')
                return False
            for sim in contains:
                if sim not in word:
                    print(f'Нет такого "{sim}" символа в строке!')
                    return False
            if len(word) > max_length:
                print(f'Превышает количество символов {max_length}! {word}')
                return False
            else:
                return func(*args, **kwgs)
        return wrapper
    return function


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

