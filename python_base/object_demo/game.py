# ！/usr/bin/env python
# -*- coding：utf-8 -*-
"""
回合制游戏
每个角色：
    --hp血量
    --power攻击力度
    --fight方法：
        my_hp=hp-enemy_power
        enemy_final_power=enemy_hp-my_power
两个血量hp进行对比，血量剩余多的人获胜
"""


# def game():
#     my_hp=10000
#     my_power=200
#     enemy_hp=900
#     enemy_power=199
#     # my_final_hp = my_hp-enemy_power
#     # enemy_final_hp=enemy_hp-my_power
#     # if my_final_hp>enemy_hp:
#     #     print("i win")
#     # else:
#     #     print("i am defeated")
#     # 三目表达式
#     # print("i win") if my_hp>enemy_hp else print("i was defeated")
#     while True:
#         my_hp=my_hp-enemy_power
#         enemy_hp=enemy_hp-my_power
#         if my_hp<=0:
#             print("i was defeated")
#             break
#         if enemy_hp<=0:
#             print("enemy was defeated")
#             break
# game()

class game:
    # my_hp:int=10000
    my_power: int = 200
    # enemy_hp:int=900
    enemy_power: int = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            if self.my_hp <= 0:
                print("i was defeated")
                break
            if self.enemy_hp <= 0:
                print("enemy was defeated")
                break


game_01 = game(10000, 900)
game_01.fight()
