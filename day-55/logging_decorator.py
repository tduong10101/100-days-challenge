def logging_decorator(func):
    def wrap(*args,**kwargs):
        print(func.__name__)
        print(args[0])
        print(func(args[0]))        
    return wrap

@logging_decorator
def hello(name):
    return f"Hello {name}!"

hello("Terry")