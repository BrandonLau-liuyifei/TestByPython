import json
import os
import shutil

# 读取json文件路径及文件目录
file_path = os.path.abspath("data.json")
src_dir = os.path.dirname(file_path)
file_full_name = os.path.basename(file_path)
file_name = str(file_full_name).replace('.json','')
# 复制多个文件到目标目录，且重新命名
os.makedirs(os.path.join(src_dir, 'fake_data'))
dst_dir = os.path.abspath("fake_data")
print(dst_dir)
# 创建文件数量n,单位万
n = 5
for i in range(n):
    shutil.copy(file_path, dst_dir)
    new_file_full_name = file_name + f"{str(i).rjust(2, '0')}"+'.json'
    os.rename(os.path.join(dst_dir, file_full_name), os.path.join(dst_dir, new_file_full_name))
    fake_data_file_path = os.path.abspath(os.path.join(dst_dir, new_file_full_name))
    # 读取json文件
    with open(fake_data_file_path, 'r') as file:
        data = json.load(file)
        list1 = data["dependencies"]
        for j in range(i*10000,(i+1)*10000):
            ele = {"a": f"{str(j).rjust(5, '0')}"}
            list1.append(ele)
        print(data)

    # 将文件写入json文件
    with open(fake_data_file_path, 'w') as file:
        json.dump(data, file, indent=4)
