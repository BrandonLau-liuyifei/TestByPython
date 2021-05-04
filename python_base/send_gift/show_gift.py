# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import gift


def show_gift():
    having_gift = gift.having_gift
    if having_gift == True:
        print("收到礼物啦，好开心")
    else:
        print("还没有礼物啦")
