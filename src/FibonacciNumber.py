# use iterator
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > 10000:  # prevent infinite loop
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
    
    ############################################

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# usage
fib_iter = FibonacciIterator()
for _ in range(10):
    print(next(fib_iter))


# usage
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))


