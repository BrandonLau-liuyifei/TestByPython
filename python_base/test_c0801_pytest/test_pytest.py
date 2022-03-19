# -*- coding: utf-8 -*-
# @Author : Brandon
import pytest

from python_base.test_c0801_pytest.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()
        print("this is start")

    def teardown(self):
        print("this is end")

    def test_add(self):
        result = self.calc.add(1, 2)
        assert result == 3

    def test_div(self):
        result = self.calc.div(6, 2)
        assert result == 3


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])
