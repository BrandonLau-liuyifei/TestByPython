# 1. 单元测试

1. 单元测试概念 单元测试是开发编写的代码，用于检验被测代码的一个很小的功能是否正确，通常一个单元测试是用于判断某个特定条件(或场景)下某个特定函数的行为。
2. 单元测试注意点： 单元测试的时候需要清楚知道自己测试的代码段输入和输出，然后根据这个预期和程序逻辑书写case，case一定要针对需求/设计的逻辑去写，而不是针对程序的实现去写。
3. 单元测试框架：

- Unittest
    - python内置的标准库。它的API与Java的JUnit、.net的NUnit、C++的CppUnit很相似。
- Pytest
    - 丰富、灵活的测试框架，语法简单，可以结合allure生成一个炫酷的测试报告，比较流行。
- Nose
    - Nose是对unittest的扩展，使的python的测试更简单。
- Mock
    - unittest.mock用来测试python的库，这是一个标准库(出现在python3.3及以上版本)。
- 其它

4. 单元覆盖率 单元覆盖用于自动化测试和手工测试来度量测试是否全面的指标之一，应用覆盖率的的思想增强测试用例的设计。 单元测试覆盖类型：
   ![[00021.png]]

- 语句覆盖
    - 通过设计一定的测试用例保证测试的方法每一行代码都会被执行一遍
    - 运行测试用例是被击中行被成为覆盖的语句
    - 测试用例
        - 仅需一条用例即可实现行覆盖
        - a=3,b=0,x=3
        - 漏洞
            - and - > or
    - 行覆盖是一个最基础的覆盖方式，也是最薄弱的，如果完全依赖行副盖，会出现严重的问题。
- 判定覆盖
    - 运行测试用例过程被击中的判定语句
    - 测试用例
      ![[00022.png]]
    - 漏洞
        - 大部分的测试判定语句由多个逻辑条件组合而成，若仅仅判断期整个过程的最终结果，而忽略每个条件的取值情况，必然会造成部分测试路径遗漏。
        - a==2 or x>1 - > a==2 or x<1
- 条件覆盖
    - 条件覆盖和判定覆盖类似，不过判定覆盖关注整个判断语句，而条件覆盖则关注某个判断条件。
    - 测试用例
      ![[00024.png]]
    - 缺陷
        - 测试用例指数级增(2**condition)
- 路径覆盖
    - 覆盖多有可能执行的路径
    - 测试用例
      ![[00023.png]]
    - 应用这些方法设计测试用例

# 2. unittest测试框架

1. unittest 框架介绍
    - python自带的测试框架，用于单元测试中。
    - 在自动化测试中提供用例组织与执行。
    - 提供丰富的断言方法-验证函数等功能。
    - 加上HTMLTestRunner可以生成html报告。
2. unittest编写规范 Unittest提供了test cases、test suites、test fixture、test runner相关的组件。 编写规范：

- 测试模块先导入 import unittest
- 测试类必须继承 unittest.TestCase
- 测试方法必须以“test_”开头
- 模块和类名称没有特殊要求

3. 总结

- setUp用来为测试准备环境，tearDown用来清理环境。
- 执行所有测试用例前后准备一次环境或清理一次环境，可以使用setUpClass()与tearDown()，比如数据库链接及销毁。
- 如果想有些方法不再本次执行使用@unittest.skip
- 各种执行-单一用例、全部用例

3. unittest代码练习：

```
# ！/usr/bin/env python  
# -*- coding：utf-8 -*-  
import unittest  
  
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
        self.assertEqual(1,1,"参数相等")  
  
    def test_demo_02(self):  
        print("this is demo_test_02")  
        self.assertNotEqual(1, 2, "参数不相等")  
  
    @unittest.skipIf(1+1==2,'跳过这条用例')  
    def test_demo_03(self):  
        print("this is demo_test_03")  
  
class demo1(unittest.TestCase):  
  
    def test_demo1_01(self):  
        print("this is demo1_test_01")  
        self.assertIn("h","this","参数包含")  
  
    def test_demo1_02(self):  
        print("this is demo1_test_02")  
        self.assertNotIn("y", "this", "参数不包含")  
  
if __name__ == '__main__':  
    unittest.main()
```

4. unittest断言方法
   ![[00017.png]]
5. unittest执行测试用例 多个测试用例的集合即测试套件TestSuite，测试套件管理测试 用例。 01 测试用例执行方法一：
   ```unittest.main()```
   02 测试用例执行方法二：加入容器中执行
   ```
   suite = unittest.TestSuite()  
   suite.addTest(demo("test_demo_01"))  
   suite.addTest(demo1("test_demo1_01"))  
   unittest.TextTestRunner().run(suite)
   ```
   03 测试用例执行方法三：加入容器中执行
   ```

suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)  
suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)  
suiteall = unittest.TestSuite([suite1,suite2])  
unittest.TextTestRunner().run(suiteall)
```
04 测试用例执行方法四：匹配某个目录下所有test开头的py文件，执行这些测试用例下的所有文件 test_dir = "./test_case"
discover = unittest,defaultTestLoader.discover(test_dir,pattern = "test*.py")

- discover 一次可以执行多个脚本
- test_dir 被测试脚本的路径
- pattern 脚本名称匹配规则

```
discover = unittest.defaultTestLoader.discover("./", 'test_C_0705*.py')  
unittest.TextTestRunner().run(discover)
```

6. 测试用例执行过程
   ![[00018.png]]
7. 测试分析 unittest结合htmltestruner生成带有日志的测试报告

```
# HTMLTestRunner测试报告  
report_title = '测试报告'  
desc = '测试练习使用'  
report_file = './测试报告.html'  
  
with open(report_file,'wb') as report:  
    runner = HTMLTestRunner(stream=report,title=report_title,description=desc)  
    runner.run(discover)
```

![[00020.png]]
添加时间和地址
![[00019 1.png]]