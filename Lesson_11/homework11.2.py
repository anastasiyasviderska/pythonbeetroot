def stop_words(words: list):
    def wrapped_function(func):
        def wrapper(arg):
            string = func(arg)
            for word in words:
                string = string.replace(word, "*")
        return wrapper
    return wrapped_function

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('Stteve')

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"