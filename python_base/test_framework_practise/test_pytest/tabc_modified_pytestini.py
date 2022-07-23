# -*- coding: utf-8 -*-
# @Author : Brandon
import pytest


class Login01():
    def case01(self):
        print('我是有个修改之后的方法')

    def test01(self):
        print('我是有个没有修改之后的方法')


if __name__ == '__main__':
    pytest.main(['-vs'])
