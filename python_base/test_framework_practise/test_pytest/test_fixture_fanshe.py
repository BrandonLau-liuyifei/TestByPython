class Person:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

p = Person('jerry')
# hasattr 判断实力中有没有属性或方法
print(hasattr(p, 'name'))
print(hasattr(p, 'eat'))
print(hasattr(p, 'run'))
# 获取实例中的属性或方法
f = getattr(p,'eat')
f()
f = getattr(p,'name')
print(f)
# 判断是否具备这个属性，不具备给一个默认值
f = getattr(p,'age',20)
print(f)

# 色了牛奶的固定色股市大幅hi分估算的分手否认凤凰机密结尾飞机范文芳