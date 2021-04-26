# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import json

# json由字典和列表组成
data = {
    "name": ["tom", "nickname"],
    "age": 26,
    "gender": "male"
}

# 将json转换成字符串
print(type(data))
data1 = json.dumps(data)
print(data1)
print(type(data1))

# 将字符串转换成json
data2 = json.loads(data1)
print(data2)
print(type(data2))
