# ！/usr/bin/env python
# -*- coding：utf-8 -*-
## HJ01.计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。
# a=input("请输入：")
# list_01=a.split()
# print(list_01)
# b=list_01[-1]
# c=len(b)
# print(c)

# #HJ02.写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写，字符串长度小于500。
# str_01=input()
# a=input()
# str_02=str_01.lower()
# b=a.lower()
# count_01=str_02.count(b)
# print(count_01)

"""HJ03.明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。
注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。
当没有新的输入时，说明输入结束。"""
# 做不出来的
# while True:
#     try:
#         a = int(input())
#         res = set()
#         for i in range(a):
#             res.add(int(input()))
#         for i in sorted(res):
#             print(i)
#     except:
#         break
# 我的答案
# while True:
#     try:
#         num=int(input())
#         list01=[]
#         list02=[]
#         for i in range(num):
#             list01.append(int(input()))
#         for i in list01:
#             if i not in list02:
#                 list02.append(i)
#                 list02.sort()
#         for j in list02:
#             print(j)
#     except:
#         break
"""HJ04.连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
 •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理"""
# while True:
#     try:
#         s=input()
#         while len(s)>8:
#             print(s[:8])
#             s=s[8:]
#         else:
#             print(s.ljust(8,"0"))
#     except:
#         break
# 我的答案
# while True:
#     try:
#         str01=input()
#         while len(str01)>8:
#             print(str01[:8])
#             str01=str01[8:]
#         else:
#             print(str01+"0"*(8-len(str01)))
#     except:
#         break
"""
HJ05题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
"""
# while True:
#     try:
#         s=input()
#         s=int(s,base=16)
#         print(s)
#     except:
#         break
"""
HJ07题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""
# a=float(input())
# b=a+0.5
# print(int(b))
"""
题目描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出描述:
输出合并后的键值对（多行）
"""
# while True:
#     try:
#         dict_01={}
#         for i in range(int(input())):
#             ele_01=input()
#             list_01=ele_01.split()
#             key_01,value_01=int(list_01[0]),int(list_01[1])
#             if key_01 not in dict_01.keys():
#                 dict_01[key_01]=value_01
#             else:
#                 dict_01[key_01]=dict_01[key_01]+value_01
#         for key in sorted(dict_01.keys()):
#             print(key,dict_01[key])
#     except:
#         break
"""
HI31.题目描述
对字符串中的所有单词进行倒排。
说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；
"""
# sen_01=input()
# for i in sen_01:
#     if not i.isalpha():
#         sen_01=sen_01.replace(i," ")
# list_01=sen_01.split()
# list_01.reverse()
# sen_02=" ".join(list_01)
# print(sen_02)

