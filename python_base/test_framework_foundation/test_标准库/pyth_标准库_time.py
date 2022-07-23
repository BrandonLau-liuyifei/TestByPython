# ！/usr/bin/env python
# -*- coding：utf-8 -*-

import time

# 国外的时间格式
print(time.asctime())
# 时间戳
print(time.time())
# 时间戳转换为元祖
print(time.localtime())
# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前现在的时间
now_time = time.time()
ago_time = now_time - 60 * 60 * 24 * 2
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ago_time)))
