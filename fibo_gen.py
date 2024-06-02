from typing import Generator

# Creating an infinity Fibonacci iterator
class InfinityFibonacci:

    def __init__(self):
        self._start = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibonacci = self._start
        self._start, self._next = self._next, self._start + self._next
        return fibonacci


fibo = InfinityFibonacci()


# for numbers in range(10):   # printing 10 fibonacci numbers
#     print(next(fibo))




# Creating an infinity Fibonacci generator

def infinity_fibonacci_generator() -> Generator[int]:

    current, next_num = 0, 1
    while True:
        yield current
        current, next_num = next_num, next_num + current


fibo_gen = infinity_fibonacci_generator()


#
# for i in range(10):
#     print(next(fibo_gen))



