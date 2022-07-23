# 6.面向对象编程
# 6.1 面向对象编程、类、对象，三大特点：封装、继承、包含
# 6.2.1 定义类
"""
class <类名>(父类名):
    pass
"""


# 空类 会继承内建类
class MyClass:
    pass


print(dir(MyClass))


# 6.2.2 使用类
class MyClass1:
    "MyClass help."


myclass = MyClass1()
print("输出类说明：")
print(myclass.__doc__)
print("显示类帮助信息：")
help(myclass)

# 6.3类的属性和方法
"""
方法的第一个参数必须是self，而且不能省略
方法调用需要实例化类，并以实例名。方法名（参数列表）形式调用
整体进行一个单位的缩进，表示其属于类体中的内容

定义方法时，也可以像定义函数一样声明各种形式的参数；
调用本类中的方法时，self.方法名。
"""


# 6.3.1 类的方法
class SamplClass:
    def info(self):
        print("我定义的类！")

    def mycacl(self, x, y):
        return x + y


sc = SamplClass()
print("调用info方法的结果：")
sc.info()
print("调用mycacl方法的结果：")
print(sc.mycacl(3, 4))


class DemoInit():
    def __init__(self, x, y=0):  # 定义构造方法，具有两个初始化
        self.x = x
        self.y = y

    def mycacl1(self):  # 定义应用初始化数据的方法
        return self.x + self.y


dia = DemoInit(3)
print("调用mycacl1方法结果1：")
print(dia.mycacl1())
dia = DemoInit(3, 7)
print("调用mycacl1方法结果2：")
print(dia.mycacl1())


def coord_chng(x, y):  # 定义一个全局函数，模拟坐标转换
    return (abs(x), abs(y))


"""
__init__()方法，一个特殊的构造方法，用于类实例化时初始化相关数据，如果在这个方法中有
相关参数，则实例化时就必须提供。
"""
"""
self.方法名（参数列表）   方法调用使用要加self
"""


class Ant:  # 定义一个类Ant
    def __init__(self, x=0, y=0):  # 定义一个构造方法
        self.x = x
        self.y = y
        self.disp_point()  # 构造函数中调用类中的方法disp_point

    def move(self, x, y):  # 定义一个方法move
        x, y = coord_chng(x, y)  # 调用全局函数，坐标转换
        self.edit_point(x, y)
        self.disp_point()

    def edit_point(self, x, y):  # 定义一个方法
        self.x += x
        self.y += y

    def disp_point(self):  # 定义一个方法
        print("当前位置：(%d,%d)" % (self.x, self.y))


ant_a = Ant()
ant_a.move(2, 4)
ant_a.move(-9, 6)

# 6.3.2 类的属性
"""
实例属性  self.属性名
类属性 类名.类变量名
"""


class Demo_Property:
    class_name = "Demo_Property"  # 类属性

    def __init__(self, x=0):
        self.x = x

    def class_info(self):
        print("类变量值:", Demo_Property.class_name)
        print("实例变量：", self.x)

    def chng(self, x):  # 修改实例属性的方法
        self.x = x  # 注意实例属性的引用方式

    def chng_cn(self, name):  # 修改类属性的方法
        Demo_Property.class_name = name  # 注意类属性的引用方式


dpa = Demo_Property()
print("初始化实例")
dpa.class_info()
print("修改实例变量")
dpa.chng(3)
dpa.class_info()
print("修改类变量")
dpa.chng_cn("lala")
dpa.class_info()

'''
使用__双下画线的名称，不让某个属性或方法在类外被调用或修改，并不保证一定不能从类外调用
'''

# 6.3.3类成员方法和静态方法
"""
1.实例方法，隐含调用参数是类的实例。
2.类方法   使用@classmethod修饰，默认参数cls，隐含调用参数是类。
3.静态方法 使用@staticmethod修饰，默认无参数，没有隐含调用参数
类方法和静态方法不用实例化就可调用
静态方法和类方法中不能使用实例属性
"""


class DemoMthd:                 # 定义一个类
    @staticmethod               # 静态方法的装饰器
    def static_mthd():          # 静态类定义
        print("调用了静态方法")

    @classmethod                # 类方法装饰器
    def class_mthd(cls):        # 类方法定义，带默认参数cls
        print("调用了类方法")


# 不实例化调用方法
DemoMthd.static_mthd()         # 未实例化类，通过类名调用静态方法
DemoMthd.class_mthd()          # 未实例化类，通过类名调用类方法
# 实例化后调用
dm = DemoMthd()
dm.static_mthd()               # 通过类实例调用静态方法
dm.class_mthd()                # 通过类实例调用类方法

# 6.4 类的继承
"""
继承只能继承父级别的属性和方法。不能继承私有属性和方法,相同的方法谁先继承先用谁
"""

# 单一继承

class Ant:
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def crawl(self, x, y):
        self.x = x
        self.y = y
        print("爬")
        self.info()

    def info(self):
        print("当前位置：(%d,%d)" % (self.x, self.y))

    def attack(self):
        print("用嘴咬")


class fly_Ant(Ant):
    def attack(self):
        print("用嘴咬")
        print("尾巴针")

    def fly(self, x, y):
        self.x = x
        self.y = y
        print("飞")
        self.info()


flyant = fly_Ant(color="red")
flyant.crawl(3, 5)
flyant.fly(6, 8)
flyant.attack()

# 多重继承

class PrntA:  # 定义父类
    namea = "PrintA"

    def set_value(self, a):
        self.a = a

    def set_namea(self, namea):
        PrntA.namea = namea

    def info(self):
        print("prntA:%s,%s" % (PrntA.namea, self.a))


class PrntB:  # 定义父类
    nameb = "PrintB"

    def set_nameb(self, nameb):
        PrntB.nameb = nameb

    def info(self):
        print("prntB:%s" % PrntB.nameb)


class Sub_01(PrntA, PrntB):
    pass


class Sub_02(PrntB, PrntA):
    pass


class Sub_03(PrntA, PrntB):
    pass

    def info(self):  # 修改方法
        PrntA.info(self)
        PrntB.info(self)


print("use first class")
sub_01 = Sub_01()
sub_01.set_value("aaa")
sub_01.info()
sub_01.set_nameb("BBB")
sub_01.info()  # 执行的是PrntA中的
print("use second class")
sub_02 = Sub_02()
sub_02.set_value("aaa")
sub_02.info()
sub_02.set_nameb("BBB")
sub_02.info()
print("use third class")
sub_03 = Sub_03()
sub_03.set_value("aaa")
sub_03.info()
sub_03.set_nameb("BBB")
sub_03.info()

# 6.4.3 方法重载
"""
在子类中定义一个与父类同名的方法，重新进行定义属性和方法
如class_flyAnt 中的attack（）
class_Sub_03中的info()
"""


# 类练习
class MM:
    def __init__(self, x=0, y=0, c=0):
        self.x = x
        self.y = y
        self.c = c

    def add(self, d):
        self.d = d
        sum_01 = self.c + self.x + self.y + self.d
        print(sum_01)


mm = MM(1, 2, 3)
mm.add(5)
