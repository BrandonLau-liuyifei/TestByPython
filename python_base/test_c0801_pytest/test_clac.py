# -*- coding: utf-8 -*-
# @Author : Brandon
import sys
import unittest

print(sys.path)
sys.path.append("..")
sys.path.append("/Users/liuyifei/PycharmProjects/TestByPython")
from python_base.test_c0801_pytest.calc import Calc


class TestCal(unittest.TestCase):
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
