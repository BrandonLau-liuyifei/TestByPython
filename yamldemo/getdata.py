import yaml


# save_load将yaml数据流准成python对象
# save_dump将python对象转换成yanl格式
def get_data():
    with open('yaml01.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


def get_yaml():
    aa = {'language': ['ruby', 'python', 'java'], 'websites': {'yaml': 'YAML', 'python': 'PYTHON'}}
    yamlstr = yaml.safe_dump(aa)
    return yamlstr


print(get_data())
# print(get_yaml())
