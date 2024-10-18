# A decorator that logs the arguments and results of the called function
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"It is called {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b

add(3, 5)

print("-" * 100)


# A decorator that catches and handles exceptions
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper


@exception_handler
def divide(a, b):
    return a / b

divide(4, 2)

# An error will occur, but it will be handled by the decorator
divide(4, 0)
