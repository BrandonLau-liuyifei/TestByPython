# -*- coding: utf-8 -*-
# @Author : Brandon
def func():
    yield (x for x in range(3))


for x in func():
    print(tuple(x))

print(1 / 12)

a = ['a', 'b', 'c', ['d', 'e']]
