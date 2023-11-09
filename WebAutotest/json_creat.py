import json
import os
import shutil

# 读取json文件路径及文件目录
file_path = os.path.abspath("data.json")
print(file_path)
src_dir = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
file_list = []
# 复制多个文件到目标目录，且重新命名
dst_dir = os.makedirs(os.path.join(src_dir, 'fake_data'))
print(dst_dir)
for i in range(5):
    shutil.copy(file_path, str(dst_dir))
    new_file_name = file_name + f"{str(i).ljust(2, '0')}"
    file_list.append(new_file_name)
    os.rename(os.path.join(dst_dir, file_name), os.path.join(dst_dir, new_file_name))

# 读取json文件
with open(file_path, 'r') as file:
    data = json.load(file)
    list1 = data["dependencies"]
    for i in range(10):
        ele = {"a": f"{str(i).ljust(3, '0')}"}
        list1.append(ele)
    print(data)

# 将文件写入json文件
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
