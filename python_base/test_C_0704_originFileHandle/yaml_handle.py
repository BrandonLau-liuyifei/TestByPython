# ！/usr/bin/env python
# -*- coding：utf-8 -*-


# 将yaml数据流转换为python对象
import yaml
print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
""",Loader=yaml.FullLoader))

['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epiplemidae']

print(yaml.load("""
 -
  - Hesperiidae
  - Papilionidae
  - a: 1
 - Apatelodidae
 - Epiplemidae
""",Loader=yaml.FullLoader))
[['Hesperiidae', 'Papilionidae', {'a': 1}], 'Apatelodidae', 'Epiplemidae']

    # 从文本获取yaml数据
print(yaml.load(open('demo.yaml'), Loader=yaml.FullLoader))

# 将python对象转换为yaml格式
print(yaml.dump([{'a': 1}]))
# - a: 1
    #转换值放入文档中
with open("demo2","w") as f:
    yaml.dump(data={'a': [1, 2]},stream=f)



