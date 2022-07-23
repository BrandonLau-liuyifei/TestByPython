# ！/usr/bin/env python
# -*- coding：utf-8 -*-
"""
Bicycle自定车类
 run方法 调用时显示骑行里程km
Ebicycle电动自行车类，继承Bicycle自行车类，添加电池battery_level属性通过参数传入，同时有两个方法：
    fill_charge(vol) 充电方法，vol为电量
    run(km) 方法用于骑行，每骑行10Km消耗1度电，当电量耗尽时调用Bicycle的run方法骑行
通过传入的里程数，显示骑行结果（当电量耗尽，需要你真正骑行的里程数）
"""


class Bicycle:
    def run(self, km):
        print(f"健康环保，骑行的里程数：{km}km")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化电量
        self.battery_level = battery_level

    def fill_charge(self, vol):
        # 充电
        self.battery_level = self.battery_level + vol

    def run(self, km):
        # 先用电，后用脚蹬
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"已经用电行驶距离：{self.battery_level * 10}km")
            # # 子类调用父类的方法1 使用super方法
            # super().run(miles)
            # 子类调用父类的方法2 实例化父类,再调用父类方法
            bicycle = Bicycle()
            bicycle.run(miles)
        else:
            print(f"已经使用电行驶：{km}km")


if __name__ == '__main__':
    eb = EBicycle(10)
    eb.run(150)
