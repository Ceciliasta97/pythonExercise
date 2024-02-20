import timeit
from functools import reduce
from math import prod

# for loop implementation
def double_factorial_for_loop(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

# list comprehension implementation
def double_factorial_list_comprehension(n):
    if n== 0 or n == 1:
        return 1
    return prod([i for i in range(n, 0, -2)])
                # 这是一个列表推导式，它生成一个序列，序列中的每个元素都是从 n 开始，以 -2 为步长递减到 0（不包括0）
            # prod([...])：用于计算一个可迭代对象中所有元素的乘积

# using functools.reduce
def double_factorial_reduce(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(n, 0, -2))
# reduce函数接收两个参数：一个函数和一个可迭代对象。reduce 函数会重复应用这个函数到可迭代对象的元素上，从而将一个可迭代对象缩减为单一的累积结果。
# lambda 表达式定义了一个匿名函数，接收两个参数 x 和 y，并返回它们的乘积



# performance investigation
n = 10

# measure time taken by each method
time_for_loop = timeit.timeit('double_factorial_for_loop(n)', globals = globals(), number = 10000)
time_list_comprehension = timeit.timeit('double_factorial_list_comprehension(n)', globals = globals(), number = 10000)
time_reduce = timeit.timeit('double_factorial_reduce(n)', globals = globals(), number = 10000)

print(f"Time for loop: {time_for_loop} seconds")
print(f"Time list comprehension: {time_list_comprehension} seconds")
print(f"Time reduce: {time_reduce} seconds")
