def fibonacci_generator(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=' ')