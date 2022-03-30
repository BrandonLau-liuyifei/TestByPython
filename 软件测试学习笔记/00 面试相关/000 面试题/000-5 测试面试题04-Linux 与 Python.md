# 测试面试题集锦（四）| Linux 与 Python 编程篇（附答案）

原创 ling_tianxia 霍格沃兹测试学院  _2020-07-30 07:58_

收录于话题

# 测试面试28个内容

# Linux5322个内容

# Python11021个内容

# 测试面试真题汇总|霍格沃兹53个内容

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ervTCibwaujEkqICe4EhDyqZs9TFvD2kJlddp2UFRn18tHWaeVE1msjIOB4dmoEfia1LyYdX8jibyXOEZ0VdmDYSQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 本文为霍格沃兹测试学院学员学习笔记，进阶学习文末加群。

本系列文章总结归纳了一些软件测试工程师常见的面试题，主要来源于个人面试遇到的、网络搜集（完善）、工作日常讨论等，分为以下十个部分，供大家参考。如有错误的地方，欢迎指正。有更多的面试题或面试中遇到的坑，也欢迎补充分享。希望大家都能找到满意的工作，共勉之！~

#### 软件测试工程师面试题

1. [**
   测试常见问题与流程篇**](http://mp.weixin.qq.com/s?__biz=MzU3NDM4ODEzMg==&mid=2247489415&idx=1&sn=d936c2f4a43deebeff02a4a20a1b67df&chksm=fd32754cca45fc5ae55afcdfe9bc85a6d699b39cbfa0fb621e7d1054f7809274113d2e77765a&scene=21#wechat_redirect)

2. [**
   测试工具篇**](http://mp.weixin.qq.com/s?__biz=MzU3NDM4ODEzMg==&mid=2247489444&idx=1&sn=bfeeea24db2678fd9801cdbcf8a2017c&chksm=fd32756fca45fc799f88dc9139196aef2d6058c049d43c10febee08f49a06d48938a85d289d4&scene=21#wechat_redirect)

3. [**
   计算机网络知识与数据库篇**](http://mp.weixin.qq.com/s?__biz=MzU3NDM4ODEzMg==&mid=2247489477&idx=1&sn=ecfb85a81726b7944de54f1142d7e364&chksm=fd32750eca45fc182f369380c4adbef9f10e29bf79cf149b7ed766384a2f4e0ac9c0aceaa9cb&scene=21#wechat_redirect)

4. Linux 与 Python 编程技能篇

5. 自动化测试（Selenium、Appium 和接口测试）与性能测试篇

6. 软素质篇（10 大灵魂拷问）与反问面试官篇

---

### Linux 技能篇

1. **工作中常用的 Linux 命令有哪些？**

   ```
   awk、sed、vim、iotop、dstat、cp、top、ifconfig、pwd、cd、ll、ls、cat、tail、grep、mv、rm、mkdir、df、du
   ```

2. **什么命令可以帮助 Linux 执行 Windows 上传的脚本?**


- 改变编码格式

- vim test.sh

- :set ff?// 显示dos的话

- :set ff=unix:wq


4. **简述 Linux 三剑客**


- grep 命令


- 根据用户指定的模式 pattern 对目标文本进行过滤，显示被模式匹配到的行；

- `grep [options] pattern [file]`

- 常用参数：


- -v 显示不被pattern匹配到的行

- -i 忽略字符的大小写

- -n 显示匹配的行号

- -c 统计匹配的行数

- -o 仅显示匹配到的字符串

- -E 使用ERE，相当于egrep（可以识别更多的正则表达式规则）


- sed 命令


- 流编辑器，用来处理一行数据。将一行数据存储在模式空间中->用sed命令处理->送入屏幕->清空空间。

- 常用参数：


- -h 显示帮助

- -n 仅显示script处理后的结果

- -e 指定的脚本来处理输入的文本文件

- -f 以指定的脚本文件来处理


- 常用动作：


- a: 新增 sed -e '4 a newline'

- c: 取代 sed -e '2,5c No 2-5 number'

- d: 删除 sed -e '2,5d'

- i: 插入 sed -ed '2i newline'

- p: 打印 sed -n '/root/p'

- s: 取代 sed -e 's/old/new/g'

- g: 代表全局


- awk 命令


- 把文件逐行的读入，以空格为默认分隔符将每行切片。把行作为输入，并赋值给`$0`->将行切段，从`$1`开始->对行匹配正则/执行动作->打印内容；

- `awk 'pattern + action' [filenames]`

- 常用语法：


- filename awk 浏览的文件名

- begin 处理文本前要执行的操作

- end 处理文本之后要执行的操作

- fs 设置输入域分隔符，等价于命令行-F选项

- nf 浏览记录的域的个数（列数）

- nr 已读的记录数（行数）


- 常用参数：


- ofs 输出域分隔符

- ors 输出记录分隔符

- rs 控制记录分隔符，换行标志

- `$0` 整条记录

- `$1` 第一条分隔后的记录


6. **如何通命令定位 Linux 服务器下的日志？**


- 如果要监控日志，那么使用 `tail -f | grep xxx` 命令，过滤需要的字段；

- 如果在完整日志中查看内容，使用 `cat xxx.log | grep xxxx | awk '{print $1}'` 等命令过滤自己需要的内容；


8. **简述项目中的环境搭建和维护**


- 结合自身经验先从系统安装开始，如常用的 CentOS 和 Ubuntu 说起，系统安装主要是磁盘分区和磁盘阵列问题；

- 基础环境依赖，如 MySQL、Redis、Jenkins、Docker、项目中用到的其他依赖环境等；

- 维护方便主要从遇到的错误说起，如无法远程连接、服务器加固等；

---

### Python 编程篇

1. **Python 中类方法，类实例方法，静态方法的区别**


- 实例方法：由对象调用；至少一个 self 参数；执行普通方法时，自动将调用该方法的对象赋值给 self；

- 类方法：由类调用；至少一个 cls 参数；执行类方法时，自动将调用该方法的类复制给 cls；

- 静态方法：由类调用；无默认参数；


3. **dict 和 tuple 及 list 的区别（这里列的是主要区别，面试足够）**


- tuple 是不可变对象，list 和 dict 都是可变对象，这里的不可变指的是指向地址不可变；

- list 是有序的，dict 是无序的，不可存放有序集合；

- dict 查找速度快，不管有多少个元素时间都一样，list 查找速度慢，需要有序查找；

- dict 的 key 为不可变对象，且不可重复，list 则可以重复，存放任意对象；


5. **JSON 和 dict 的区别**


- JSON 是一种数据格式，纯字符串。dict 是一种完整的数据结构；

- dict 是一个完整的数据结构，是对 Hash Table 这一数据结构的一种实现，是一套从存储到提取都封装好了的方案。它使用内置的哈希函数来规划 key 对应 value 的存储位置，从而获得O（1）的数据读取速度；

- JSON 的 key 只能是字符串，Python 的 dict 可以是任何可 hash 对象（不可变对象）；

- JSON 的 key 可以是有序、可重复的；dict 的 key 不可重复，且无序；

- JSON 任意 key 存在默认值 undefined，dict 默认没有默认值；

- JSON 访问方式可以是[],也可以是.，遍历方式分 in、of；dict 的 value 仅可以下标访问；

- dict 可以嵌套 tuple，JSON 里只有数组；


7. **Python 会不会出现内存泄漏，为什么？**


- 当对象之间互相引用的时候再删除的时候，可能会造成无法释放对象的情况，出现泄漏；

- 上面为个人了解，如有其它请补充；


9. **Python 的同步和异步**


- 直接得到最终结果的结果，就是同步调用。

- 不直接得到的最终的结果，就是异步调用。

- 同步与异步区别在于：调用者是否得到了想要的最终结果。


11. **常见手撕代码题**


- **两个列表提取作为字典**

```
dict(zip(list1, list2))
```

- **字符串反转输出**

```
str = '1234567890'print(str[::-1])l = list(str)l.reverse()print(''.join(l))
```

- **实现斐波那契数列**

```
def Fibonacci(loop):    if loop == 0:        return '无效参数'    elif loop == 1:        return 0    l = [0, 1]    for i in range(2, loop):        l.append(l[i - 1] + l[i - 2])    return l
```

- **找出驼峰数组的最大值**

```
li = [1, 2, 10, 10, 2, 1]print([v for v in li if v == max(li)])
```

- **水仙花数**

```
sxh = []for i in range(100, 1000):    s = 0    for j in str(i):        s += int(j)**3    if i == int(j)**3:        sxh.append(i)print(sxh)
```

- **完全数**

```
a = []for i in range(1, 1000):    s = 0    for j in range(1, i):        if i % j == 0 and j < i:            s += j    if s == i:        a.append(i)
```

- **幂的递归**

```
def mi(a, n):    if n == 0:        return 1    else:        return a * mi(a, n - 1)
```

- **目录遍历**

```
import osdef get_file(path, rule=''):    files = []    for fpath, dirs, fs in os.walk(path):        for f in fs:            if os.path.join(fpath, f).endswith(rule):                files.append(f)    return files
```

  
  

