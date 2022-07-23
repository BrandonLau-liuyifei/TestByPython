# ！/usr/bin/env python
# -*- coding：utf-8 -*-

'''
发礼物设计：
1.拥有礼物标识
2.定义发礼物的方法 send_gift
3.展示礼物的方法 show_gift
4.启动方法
'''

having_gift = False


def send_gift():
    print("发礼物啦")
    global having_gift
    having_gift = True


def show_gift():
    if having_gift == True:
        print("收到礼物啦，好开心")
    else:
        print("还没有礼物啦")


print(__name__)
print(locals())

if __name__ == '__main__':
    send_gift()
    show_gift()
