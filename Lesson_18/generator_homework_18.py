# Generator that returns a sequence of even numbers from 0 to N
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i


for num in even_numbers(10):
    print(num)

print("-" * 100)


# A generator that generates a Fibonacci sequence up to a certain number N
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


for num in fibonacci(20):
    print(num)
