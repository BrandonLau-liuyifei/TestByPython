# -*- coding: utf-8 -*-
# @Author : Brandon

# yield+函数
def provider():
    for i in range(5):
        print('before')
        yield i  # 生成器 return i
        print('after')


p = provider()
print(next(p))
print(next(p))
print(next(p))
