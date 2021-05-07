# ！/usr/bin/env python
# -*- coding：utf-8 -*-
a = 1


def fun():
    global a
    a = 2
    print(f'"变量:"{a}')
    print(id(a))
    print("这是一个方法")


fun()
print(a)
print(id(a))
