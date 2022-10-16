# -*- coding: utf-8 -*-
# @Author : Brandon
# yield + 函数 == 生成器

def provider():
    for i in range(5):
        print("before")
        yield i  # 生成器 return i
        print("after")


def test_yield():
    p = provider()
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
