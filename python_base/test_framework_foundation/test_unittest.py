# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import unittest

from python_base.test_framework_foundation.HTMLTestRunner_PY3 import HTMLTestRunner


class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_demo_01(self):
        print("this is demo_test_01")
        self.assertEqual(1, 1, "参数相等")

    def test_demo_02(self):
        print("this is demo_test_02")
        self.assertNotEqual(1, 2, "参数不相等")

    @unittest.skipIf(1 + 1 == 2, '跳过这条用例')
    def test_demo_03(self):
        print("this is demo_test_03")


class demo1(unittest.TestCase):

    def test_demo1_01(self):
        print("this is demo1_test_01")
        self.assertIn("h", "this", "参数包含")

    def test_demo1_02(self):
        print("this is demo1_test_02")
        self.assertNotIn("y", "this", "参数不包含")


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_demo_01"))
    # suite.addTest(demo1("test_demo1_01"))
    # unittest.TextTestRunner().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suiteall)

    discover = unittest.defaultTestLoader.discover("../", 'test_C_0705*.py')
    # unittest.TextTestRunner().run(discover)

    # HTMLTestRunner测试报告
    report_title = '测试报告'
    desc = '测试练习使用'
    report_file = '../测试报告.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
