import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)


def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(5000))

## Use timeit when comparing two ways of doing same code
import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))