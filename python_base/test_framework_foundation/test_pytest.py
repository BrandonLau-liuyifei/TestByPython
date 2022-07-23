# ！/usr/bin/env python
# -*- coding：utf-8 -*-

import pytest


class TestDemo():
    def test_one(self):
        print("开始执行 test_one方法")
        x = 'this'
        assert 'h' in x
        # pytest.assume(1 == 2)
        # pytest.assume('a' in 'hello')

    def test_two(self):
        print("开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b


class TestDemo1():
    def test_a(self):
        print("开始执行 test_a方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行 test_b方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行 test_c方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b


if __name__ == '__main__':
    # 执行当前所有test
    pytest.main()
    # 执行方式一
    pytest.main('-v -s TestDemo')
    # 执行方式二
    pytest.main(['-v', '-s', 'test_pytest.py'])
