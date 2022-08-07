# -*- coding: utf-8 -*-
# @Author : Brandon
import pytest


# 使用texture就可以不用setup teardown了
@pytest.fixture
def login():
    print('登录')
    username = 'tom'
    yield username
    print('teardown')


class TestDemo:
    # def setup_class(self):
    #     print("open browser")
    # def teardown_class(self):
    #     print("close browser")
    # def setup(self):
    #     print("set up")
    # def teardown(self):
    #     print("tear down")

    def test_a(self, login):
        print("testcase_01")

    def test_b(self):
        print("testcase_02")
