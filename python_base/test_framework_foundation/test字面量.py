name = 'lili'
age = 20
# 格式化输出
# print("my name is %s,my age is %d" % (name, age))
# string.format
# print("my name is {},my age is {}".format(name, age))
# formatted string literals
dict1 = {'name1': 'tom', 'gender': 'male'}
list1 = [1, 2, 3, 4]
print({f'my name is {name},my age is {age},my list is {list1},my dict is {dict1}'})
print({f'my name is {name},my age is {age},my list is {list1[1]},my dict is {dict1["name1"]}'})
