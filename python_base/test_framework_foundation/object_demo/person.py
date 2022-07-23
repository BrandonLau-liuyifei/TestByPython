# ！/usr/bin/env python
# -*- coding：utf-8 -*-

# class 类名：
#     静态属性
#     动态属性
# 属性：姓名，性别，年龄，存款金额。。。
# 方法：吃，睡，跑。。。
class PersonDemo:
    name: str = None
    age: int = 0
    gender: str = "男"
    __money: float = 0  # 私有属性

    def __init__(self, name, age, gender, money):
        print("构造函数")
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def get_money(self):
        return self.__money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("sleeping")

    @classmethod
    def run(self):
        print("runnung")


class FunnyMan(PersonDemo):
    skill: str = ""

    def __init__(self, skill, name, age, gender, money):
        self.skill = skill
        super().__init__(name, age, gender, money)  # 等同于将参数赋予类变量

    def fun(self):
        print(f"{self.name} is funny，his skill is {self.skill}")


if __name__ == '__main__':
    # 实例化
    # p_zs=PersonDemo()
    # print(p_zs.name)
    # p_zs.run()
    # 类
    # print(PersonDemo.name)
    # PersonDemo.run() #不可以通过类直接调用方法，可以通过类方法@classmethod调用
    # p_ls=PersonDemo()
    # print(p_ls.name)
    # p_ls.name="老狼"

    # PersonDemo.name="defaultName"
    # print(PersonDemo.name)
    # print(p_ls.name)
    #
    # p_zl=PersonDemo()
    # p_zl.name="老网"
    # print(p_zl.name)

    # p_lyf=PersonDemo("liuyifei",25,"male",20000000)
    # print(p_lyf.name)
    # # print(p_lyf.__money) 私有属性不能直接调用，可以创建方法调用
    # print(p_lyf.get_money())
    # print(dir(p_lyf))
    # print(p_lyf._PersonDemo__money)

    st = FunnyMan("说笑话", "shenteng", 40, "male", 10000)
    print(st.name)
    st.fun()
    print(st.get_money())
