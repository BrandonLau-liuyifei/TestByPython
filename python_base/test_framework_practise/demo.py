# -*- coding: utf-8 -*-
# @Author : Brandon
# from python_base.testing1.demo1 import Demo1
# from python_base.testing2 import demo2
# from python_base.testing2.demo2 import Demo2
#
# Demo1()
# Demo2()
# print(demo2.hello)
# demo2.f()

# # 使用这种方式可以使用demo2中__all__中对外开发的内容
# from python_base.testing2.demo2 import *
# print(hello)

# 使用这种方式可以使用__init__中__all__中对外demo2和demo3的内容
from python_base.test_framework_practise.testing2 import *

print(demo2.hello)
print(demo3.hello3)
