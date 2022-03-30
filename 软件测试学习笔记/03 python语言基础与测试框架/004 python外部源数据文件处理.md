# 1. python外部源文件处理

1. yaml 可读性高，表达数据序列化的格式，常用于配置文件。
2. json 轻量级别的数据交换语言，易于阅读，用来传输由属性值或者序列性的值组成的数据对象。
3. excel表格。

## 1-1  python-excel

python-excel库：

* xlrd
* xlwt
* Xlutils
* openpyxl
    * https://openpyxl.readthedocs.io/en/stable/usage.html
      示例：以openpyxl为例

01. excel写入：

```
from openpyxl import Workbook  
from openpyxl.utils import get_column_letter  
  
wb = Workbook()  
dest_filename = 'empty_book.xlsx'  
  
ws1 = wb.active  
ws1.title = 'range names'  
for row in range(1,31):  
    ws1.append(range(600))  
  
ws2 = wb.create_sheet(title = 'pi')  
ws2['A1'] = 3.15  
print(ws2['A1'].value)  
  
ws3 = wb.create_sheet(title = 'data')  
for row in range(10,20):  
    for col in range(27,54):  
        _ = ws3.cell(column=col,row=row,value='{0}'.format(get_column_letter(col)))  
print(ws3['AA10'].value)  
  
ws4 = wb.create_sheet(title = 'my_sheet')  
for i in range(1,31):  
    ws4.cell(column=1,row=i).value='test'  
  
wb.save(filename=dest_filename)
```

02. excel读取：

```
from openpyxl import load_workbook  
wb = load_workbook(filename = 'empty_book.xlsx')  
sheet_ranges = wb['range names']  
print(sheet_ranges['D18'].value)  
  
for i in range(1,31):  
    print(sheet_ranges.cell(column=18, row=i).value)
```

## 1-2 python-json

json库

* dumps
* loads
* 示例，以json库为例 json格式：

```
# json由字典和列表组成  
data = {  
    "name": ["tom", "nickname"],  
    "age": 26,  
    "gender": "male"  
}
```

01. 将json转换成字符串

```
print(type(data))  
data1 = json.dumps(data)  
print(data1)  
print(type(data1))
```

02. 将字符串转换成json

```
data2 = json.loads(data1)  
print(data2)  
print(type(data2))
```

## 1-3 python-yaml

python-yaml库:

* PyYAML
    * yaml.load
    * yaml.dump
* https://pypi.org/project/PyYAML/
  示例：以PyYAML例

01. yaml格式转为python对象：

```
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
```

02. python对象转换为yaml格式

```
print(yaml.load(open('demo.yaml'), Loader=yaml.FullLoader))  
  
# 将python对象转换为yaml格式  
print(yaml.dump([{'a': 1}]))  
# - a: 1  
 #转换值放入文档中
with open("demo2","w") as f:  
	yaml.dump(data={'a': [1, 2]},stream=f)
```