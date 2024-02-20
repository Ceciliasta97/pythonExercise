import timeit

# for loop
def symmetric_diff_for_loops(A, B):
    result = set() # =======
    for item in A:
        if item not in B:
            result.add(item)
    for item in B:
        if item not in A:
            result.add(item)
    return result

# list comprehension
def symmetric_diff_list_comprehension(A, B):
    return set([item for item in A if item not in B] + [item for item in B if item not in A])
# 使用列表推导式来生成两个列表：一个是 AA 中但不在 BB 中的所有元素，另一个是 BB 中但不在 AA 中的所有元素，然后将这两个列表合并并转换为集合。

# set comprehension
def symmetric_diff_set_comprehension(A, B):
    return {item for item in A if item not in B} | {item for item in B if item not in A}
# 使用集合推导式来直接生成对称差集，方法是分别生成 AA 和 BB 的差集，然后使用集合的并操作合并这两个差集。

# filter lambda
def symmetric_diff_filter_lambda(A, B):
    return set(filter(lambda item: item not in B, A)) | set (filter(lambda item: item not in A, B))
# 使用 filter 函数和 lambda 表达式过滤出不在另一个集合中的元素，然后对结果应用集合的并操作以生成对称差集。

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


print("For loops:", timeit.timeit('symmetric_diff_for_loops(A, B)', globals=globals(), number=10000))
print("List comprehension:", timeit.timeit('symmetric_diff_list_comprehension(A, B)', globals=globals(), number=10000))
print("Set comprehension:", timeit.timeit('symmetric_diff_set_comprehension(A, B)', globals=globals(), number=10000))
print("Filter and lambda:", timeit.timeit('symmetric_diff_filter_lambda(A, B)', globals=globals(), number=10000))

# what is the main difference between list comprehension, set comprehension and filter / lambda in python?
