# 1 allure测试报告美化和定制

## 1.1 allure测试报告

### 1.1.1 allure介绍

1. allure 介绍

- allure是一个轻量级，灵活的，支持多语言的测试报告工具；
- 多平台的,奢华的report框架；
- 可以为dev/qa提供详尽的的测试报告、测试步骤、log;
- 也可以为管理理层提供high level统计报告;
- Java语言开发的，支持pytest, JaveScript, PHP, ruby 等
- 可以集成到Jenkins

2. allure 报告预览
3. allure安装

- __windows/mac通用安装方法__
  $ https: //github.com/allure-framework/allure2/releases 下载allure2.7.zip包， alure-2.7.0.zip 解压->进入bin目录->运行allure.bat
  把bin目录加入PATH环境变量
- __Mac 可以使用brew安装：__
  brew install allure 官网：http:// allure.qatools.ru/ 文档：https://docs.qameta.io/allure /

### 1.1.2 使用allure2生成精美报告

- 安装allure-pytest插件 pip instal allure-pytest
- 运行： 在测试执行期间收樂结果 pytest [测试文件] -s -q -alluredir=./result/(—alluredir这个选项用于指定存儲测试结果的路径）
- 查看测试报告 方式一：测试完成后查看实际报告，在线看报告，会直接打开默认浏览器展示当前报告 allure serve ./ result/（注意这里的serve 书写）
  方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告 生成报告 allure generate ./ result/ -o ./ report/ -clean(注意：覆盖路径加-clean） 打开报告
  allure open -h 127.0.0.1-p 8883./ report/

### 1.1.3 allure特性-features&story

- 场景：
    - 希望在报告中看到测试功能，子功能或场景，测试步骤，包括测试附加信息
- 解决：
    - @feature, @story, @step, @attach
- 步骤：
    - import allure
    - 功能上加@allure.feature(“功能名称）
    - 子功能上加@allure.story(子功能名称）
    - 步骤上加@allure.step(“步骤细节”）
    - @allure.attach'具体文本信息”，需要附加的信息，可以是数据，文本，图片．视频，网页
    - 如果只测试登录功能运行的时候可以加限制过滤：
    - pytest 文件名 -allure_features 购物车功能” -allure_stories 加入购物车（注意这里一allure features中间是下划线）
- 注解@allure.feature 与@allure.story的关系
    - feature相当于一个功能，一个大的模块，将case分类到某个feature中，报告中behavior中显示，相当于testsuite。
    - story相当于对应这个功能或者模块下的不同场景，分支功能，属于feature之下的结构，报告在features中显示，相当于testcase。
    - feature与story类似于父子关系

### 1.3.4 allure特性-step

- 测试过程中每个步骤，一般放在具体逻辑方法中
- 可以放在关键步骤中，在报告中显示在app
- web自动测试当中，建议每切换到一个新的页面当做一个step
- 用法：
    - @allure.step()只能以装饰器的形式放在类或者方法上面
    - with allure step()：可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含。

### 1.3.4 allure特性-issue, testcase

- 关联测试用例（可以直接给测试用例的地址链接）
- 关联bug
    - 执行的时候需要加个参数
        - allure-link-pattern=issue:http: / /www.mytesttracker.com/issue/f
- 代码：

```
@allure.issue('140', "Pytest-faky test retries shows like test steps")
def test_with_issue_link(:
	pass

TEST_CASE_LINK = 'https ://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637
@allure.testcase(TEST_CASE_ LINK, Test case title")
def test_with_testcase_link0):
	pass
```

### 1.3.5 按重要性级别进行一定范围测试

- 场景
    - 通常测试有PO、冒烟测试、验证上线测试。按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
- 解决：
    - 通过附加pytest.mark标记，
    - 通过allure.feature, allure.story
    - 也可以通过 allure.severity来附加标记
        - 级别：Trivial;不重要，Minor不太重要，Normal:正常问题，Critical: 严重，Blocker:阻塞
        - Critical级别：临界缺陷（功能点缺失）
        - Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
        - Normal级别：普通缺陷（数值计算错误）
        - Minor级别：次要缺陷（界面错误与UI需求不符）
        - Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
- 步骤：
    - 在方法,函数和类上面加
        - @allure.severity(allure.severity_level.TRIVIAL)
    - 执行时
        - pytest -s -Y 文件名 -allure-severities normal critical

### 1.3.5 前端自动化测试-截图

- 场景： •前端自动化测试经常需要附加图片或html，在适当的地方，适当的时机截图
- 解决： @allure.attach显示许多不同类型的提供的附件，可以补充测试、步骤或测试结果。
- 步骤：
    - 在测试报告里附加网页： allure.attach(body(内容), name, attachment_type, extension):
      allure.attach('chead></head>cbody> 首页</body>，这是错误页的结果信息’allure.attachment_type.HTML)
    - 在测试报告里附加图片： allure.attach.file(source, name, attachment_type, extension):
      allure.attach.file("./ result /b.png', attachment type=allure.attachment_ type.PNG)

### 1.4 百度搜索页面结合allure

![[截屏2022-01-23 下午6.50.43.png]]