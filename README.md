## main difference between Iterator and generator in python
    迭代器（Iterator）：
        迭代器是一个对象，它实现了__iter__()和__next__()方法，可以按需生成值。
        迭代器一次性产生一个值，然后在下一次调用__next__()方法时产生下一个值。
        迭代器可以用于遍历一系列数据，但它们不保存整个序列在内存中，因此节省了内存空间。
        当迭代器耗尽所有值时，会引发StopIteration异常。

    生成器（Generator）：
        生成器是一种特殊的迭代器，它使用yield语句来产生值，而不是__next__()方法。
        生成器函数在调用时并不立即执行，而是返回一个生成器对象，只有在迭代时才会执行函数体。
        每次调用生成器的__next__()方法时，生成器会执行一次函数体，直到遇到yield语句，然后暂停并返回值。
        生成器可以像迭代器一样用于遍历序列，但由于其惰性计算的特性，生成器通常更加高效。


## ReadCSV: what is the difference between read() and readlines() in python?
    read() returns the entire content of the file as a single string (or bytes object), 
    while readlines() returns a list of strings, each representing a single line from the file.

    read() loads the entire content into memory at once, which can be inefficient for large files, 
    while readlines() allows you to process the file line by line, which is more memory-efficient.
