import functools


def stop_words(words: list):
    def function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            string = (f'{func(*args, **kwds)}')[:]
            for word in words:
                if word in string:
                    string = string.replace(word, '*')
            return string
        return wrapper
    return function


@stop_words(['drinks', 'his', 'pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve * * in * brand new *!"
