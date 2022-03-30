# 1. pytest测试框架

## 1.1 pytest介绍

01. 测试用例安装与依赖
    - pip install -U pytest U表示升级
    - pip install pytest-sugar 界面美化
    - pip install pytest-rerunfailures 重新执行失败的用例
    - pip install pytest-xdisk 并发执行测试用例
    - pip install pytest-assume 添加断言
    - pip install pytest-html
    - pytest -h 帮助查看
    - ......

## 1.2 测试用例的识别与运行

1. 测试文件 test_*.py 或*_test.py
2. 用例识别

- Test*类包含所有的test_*的方法(测试类不能带有__init__方法)
- 不在class中的所有的test_*.py  
  pytetst也可以执行unittest框架写的用例和方法

3. 终端测试运行：

```
pytest 运行参数：  
 pytest --help查看帮助文档 
 pytest 无参数 读取路径下符合规则的文件，类，方法，函数并全部执行 pytest -v   打印详细日志，方便定位问题 
 pytest -s   打印print输出的语句 
 pytest -k   跳过指定测试类、测试方法、某个测试类中的某个测试方法的运行 
 pytest -k '类名' 
 pytest -k '方法名' 
 pytest -k '类名 and not 方法名' 
 pytest -x   遇到用例失败立即停止 
 pytest --maxfail=[num]  失败用例量到阀值立即停止 
 pytest -m [标记名]  运行@pytest.mark.[标记名]的测试用例 如  @pytest.mark.login 
 def test_add(): 
 	assert add(1,10) == 11 
	assert add(1,1) == 2 
	assert add(1,99) ==100    pytest运行模式  
 pytest 文件名.py   #运行文件 
 pytest 文件名.py::类名   #运行文件中的类 
 pytest 文件名.py::类名::方法名  #运行文件中的类的方法 
 ```

场景： 测试失败后要重新运行n次，在重新运行之间添加延迟时间，间隔n秒运行

- pip install pytest-rerunfailures
- pytst --reruns 3 -v -s test.py
- pytst --reruns 3 -v -s test.py --delays 1

场景： 用例存在多条断言时，一条报错，其他的也能继续执行。

- pip install pytest-assume
- pytst --assume(1 == 4)
- pytst --assume(2 == 4)

pycharm 中执行
![[00025.png]]

```
if __name__ == '__main__':  
    # 执行当前所有test  
 pytest.main()  
    # 执行方式一  
 pytest.main('-v -s TestDemo')  
    # 执行方式二  
 pytest.mian(['-v','-s','test_C_0707_pytest.py'])
```

## 1.3 pytest框架结构

import pytest 类似的setup,teardown同样更灵活，

- 模块级(setup_module /teardown_module)模块始末，全局的（优先最高）
- 函数级(setup_function/ teardown_function)只对函数用例生效（不在类中）
- 类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
- 方法级(setup_method /teardown, methond)开始于方法始未（在类中）
- 类里面的(setup/teardown）运行在调用方法的前后

__pytest-fixture的用法__
场景： 用例1需要先登录 用例2不需要登录 用例3需要登录 这种场景无法用setup与teardown实现 用法： 在方法前面加@pytest.fixture()

1. 例子1:前端自动化中应用
   __场景:__
   测试用例执行时，有的用例需要登陆才能执行，有些用例不需要登陆。 setup和teardown无法满足。fixture可以。默认scope（范围)function
   __步骤:__

- 导入pytest
- 在登陆的函数上面加@pytest.fixture(）
- 在要使用的测试方法中传入(登陆函数名称），就先登陆
- 不传入的就不登陆直接执行测试方法

2. 例子2:前端自动化中应用-conftest
   __场景:__
   你与其他测试工程师合作一起开发时,公共模块要在不同文件中,要在大家都访问到的地方。
   __解决:__
   conftest.py这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用。
   __执行:__
   系统执行到参数login时先从本文件中查找是否有这个名字的变量，之后在conftest.py中找是否有
   __步骤:__
   将登陆模块带@pytest.fixture写在conftest.py

conftest.py配置需要注意：

* conftest文件名是不能换的
* conftest.py与运行的用例要在同一个package下，并且有_init_py文件
* 不需要import导入conftset.py，pytest用例会自动查找
* 全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方。

3. 例子3:前端自动化中应用-yield
   __场景：__
   你已经可以将测试方法前要执行的或依赖的解决了，测试方法后销毁清除数据的要如何进行呢?范围是模块级别的。类似 setupClass
   __解决：__
   通过在同一模块中加入 yield关键字，yield是调用第一次返 回结果，第二次执行它下面的语句返回。
   __步骤：__
   在@pytest.fixture(scope=module)
   在登陆的方法中加yield，之后加销毁清除的步骤.注意，这种方式没有返回值，如果希望返回使用addfinalizer

```
@pytest.fixture(scope="module")  
def open():  
    print("打开浏览器")  
    yield  
	print("执行teardown")  
    print("最后关闭浏览器")
# fixture默认是方法级，使用模块级需要scope指定module，关键字yield决定了首次执行第一条用例执行"打开浏览器"，最后一条用例执行"执行teardown"和"最后关闭浏览器"。
```

4. 例子4：fixture的自动应用
   __场景：__
   不想原测试方法有任何改动，或全部都自动实现自动应用，没特例，也都不需 要返回值时可以选择自动应用
   __解决：__使用fixture中参数autouse=True实现
   __步骤：__
   在方法上面加@pytest.fixture(autouse=True)
   在测试方法上加@pytest.mark.usefixtures("start")

```
*参数组合
@pytest.mark.parametrize("x", [1,2))
@pytest.mark.parametrize("y", [8, 10,11])
def test_foo(x,y)：
	print(f"测试数据组合x：{x}，y:{y)”）

#、方法名作为參数
test_user_data = ['Tome' "Jerry']
@pytest.fixture(scope="module
def Login_r(request):
	#这是接收井传入的參数
	user = request.param
	print(f"ln 打开首页准备登录，登录用户：{user）”）
	return user
# indirect-True，可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
	def test_Login(Logime.r)：
	a = Login.r
	print(f测试用例中1ogin的返回值； {a)”)
	assert a !=W
```

__mark中的skip与xfail__
__skip 使用场景__

* 调试时不想运行这个用例
* 标记无法在某些平台上运行的测试功能
* 在某些版本中执行，其他版本中跳过
* 当前的外部资源不可用时跳过(如果测试数据是从数据库中取到的，连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错）

__解决：__
@pytest.mark.skip跳过这个测试用例，可以加条件skipif，在满足某些条件下才希望通过，否则跳过这个测试。
__sfail 场景：__
功能测试尚未实施或尚未修复的错误，当测试通过时尽管会失败(标记为pytest.mark.xfail)，它是一个xpass,将在测试摘要中报告。你希望测试由于某种情况而就应该失败。
__解决：__
@pytest.mark.xfail

```
# @pytest.mark.skipif(sys.platform =. "darwin", reason="不在macos上执行"）
# @pytest.mark.skip(”此次测试不执行登录”）
# xpass 功能尚未实施或修复时使用，不确定是否pass
@pytest.mark.xfail
```

__使用自定义标记mark只执行某部分用例__
__场景：__
只执行符合要求的某一部分用例 可以把一个web项目划分多个模块，然后指定模块名称执行。
App自动化时，如果想Android和I0S公用一套代码时，也可以使用标记功能、标明哪些是IOS的用例，哪些是Android的、运行代码时指定mark名称运行就可以。
__解决：__
在测试用例方法上加@pytest.mark.webtest
__执行：__

* -s参数：输出所有测试用的print信息
* -m:执行自定义标记的相关用例 pytest-s test. mark_zi.09.py pytest-s test. mark_zi.09.py-m=webtest pytest-s test. mark_zi.09.py-m
  apptest pytest-s test. mark_zi09.py-m ”not ios"

注意：执行时会报warning，unknown pytest.mark.website等，需要在confest.py文件中添加以下解决：

```
def pytest_configure(config):
	markef_List ["search", "Login”] # 标签名集合
	for markers in marker_list:
		config. addinivalue_Line("markers", markers)
```

5. 例子5： 多线程并行与分布式执行
   __场景：__
   测试用例1000条，一个用例执行1钟，一个测试人员执行需要1000分 钟。通常我们会用人力成本换取时间成本，加几个人一起执行，时间就会缩短。如果10人一起执行只需要100分钟，这就是一种并行测试，分布式场景。
   __解决：__
   pytest分布式执行插件：pytest-xdist，多个CPU或主机执行 前提：用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不影响其他用例。
   __安装：__
   pip3 install pytest-xdist 多个CPU并行执行用例，直接加-n3是并行数量：pytest-n 3 在多个终端下一起执行
6. pytest-html生成报告

* 安装： pip install pytest-html
* 生成html报告 pytest -v -s --html=report.html --self-contained-html --capture=sys testxxx文件
* 报告效果
  ![[00026.png]]
