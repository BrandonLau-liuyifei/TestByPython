# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import python_base.test_framework_foundation.earn_money.money


def send_money():
    earn_money_work = 1000
    saved_money = python_base.test_framework_foundation.earn_money.money.saved_money
    saved_money = saved_money + earn_money_work
    return saved_money
