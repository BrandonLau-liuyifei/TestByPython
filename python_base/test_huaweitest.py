# ！/usr/bin/env python
# -*- coding：utf-8 -*-
'''HJ01.计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。'''
# a=input("请输入：")
# list_01=a.split()
# print(list_01)
# b=list_01[-1]
# c=len(b)
# print(c)
# 简写1行 print(len(input().split()[-1]))
'''#HJ02.写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写，字符串长度小于500。'''
# str_01=input()
# a=input()
# str_02=str_01.lower()
# b=a.lower()
# count_01=str_02.count(b)
# print(count_01)
# 简写1行
# print(input().lower().count(input().lower()))
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
# 简写
# while True:
#     try:
#         print((int(input(),16)))
#     except:
#         break
"""
HJ07题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""
# a=float(input())
# b=a+0.5
# print(int(b))
# 简写
# print(int(float(input())+0.5))
"""
HJ08题目描述
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
HJ09题目描述：提取不重复数
描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
输入描述：
输入一个int型整数
输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""
# a = str(input())
# list_01 = list(a)
# list_01.reverse()
# list_02 = []
# for i in list_01:
#     if i not in list_02:
#         list_02.append(i)
# str_02 = "".join(list_02)
# b=int(str_02)
# print(b)

# str = ''
# numb = input()
# for i in range(len(numb)):
#     if numb[-(i+1)] not in str:
#         str = str + numb[-(i+1)]
# print(str)

"""
HJ10 字符个数统计
编写一个函数，计算字符串中含有的不同字符的个数。字符在ASCII码范围内(0~127，包括0和127)，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串abaca而言，有a、b、c三种不同的字符，因此输出3。
输入描述：
输入一行没有空格的字符串。abc
输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。3
"""
# str_01 = input()
# str_02 = ""
# for i in range(len(str_01)):
#     if str_01[i] not in str_02:
#         str_02 = str_02 + str_01[i]
# print(len(str_02))

# str_01 = input()
# set_02 = set(str_01)
# print(len(set_02))

# 简写
# print(len(set(input())))

"""
HJ11 数字颠倒
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
输入描述：
输入一个int整数 1516000
输出描述：
将这个整数以字符串的形式逆序输出 0006151
"""
# num_01= input()
# str_01 = str(num_01)
# str_02=''
# for i in range(len(str_01)):
#     str_02 = str_02 + str_01[-(i+1)]
# print(str_02)

# num_01= input()
# str_01 = str(num_01)
# print(str_01[::-1])

"""
HJ12 字符串反转
描述

接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
输入描述：
输入一行，为一个只包含小写字母的字符串。abcd
输出描述：
输出该字符串反转后的字符串。dcba
同HJ11
"""
# str_01= input()
# str_02=''
# for i in range(len(str_01)):
#     str_02 = str_02 + str_01[-(i+1)]
# print(str_02)

# str_01= input()
# print(str_01[::-1])

"""
HJ13 句子逆序
描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
输入描述：
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。 i am a boy
输出描述：
得到逆序的句子boy a am i
"""
# sen_01 = input()
# list_01 = sen_01.split(" ")
# list_01.reverse()
# sen_02 = " ".join(list_01)
# print(sen_02)
"""
HJ14 字符串排序
描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
9
cap
to
cat
card
two
too
up
boat
boot
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
boat
boot
cap
card
cat
to
too
two
up
"""
# num1 = int(input())
# s = []
# for i in range(num1):
#     s.append(input())
# s.sort()
# for j in s:
#     print(j)
"""
HJ15 求int型整数在内存中存储时1的个数
描述

输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
输入描述：
 输入一个整数（int类型）5
输出描述：
 这个数转换成2进制后，输出1的个数 2
"""
# conv_b = int(input())
# conv_a = bin(conv_b)
# print(conv_a.count('1'))

"""
HJ17 坐标移动
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）

注意请处理多组输入输出
输入描述：A10;S20;W10;D30;X;A1A;B10A11;;A10;
一行字符串
输出描述：10,-10
最终坐标，以逗号分隔
"""
# while True:
#     try:
#         s = input()
#         list_01 = list(s.split(";"))
#         x,y = 0,0
#         for i in list_01:
#             if not i:
#                 continue
#             elif i[0] == 'A' and i[1:].isdigit():
#                 loc_01 = int(i[1:])
#                 x-=loc_01
#             elif i[0] == 'D' and i[1:].isdigit():
#                 loc_02 = int(i[1:])
#                 x+=loc_02
#             elif i[0] == 'W' and i[1:].isdigit():
#                 loc_02 = int(i[1:])
#                 y+=loc_02
#             elif i[0] == 'S' and i[1:].isdigit():
#                 loc_02 = int(i[1:])
#                 y-=loc_02
#             else:
#                 continue
#         print(str(x) + "," + str(y))
#     except:
#         break
"""
HJ19 简单错误记录
描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是”相同“的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
输入描述：
每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637  
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631
输出描述：
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：
rzuwnjvnuz 633 1
atl 637 1
rwyfvzsopsuiqjnr 647 1
eez 648 1
fmwafhhgeyawnool 649 1
c 637 1
f 633 1
ywzqaop 631 2
"""

# log_list = []
# dict01 = {}
# while True:
#     try:
#         s = input()
#         path,error_code = map(str,s.split())
#         file_name = path.split('\\')[-1][-16:]
#         key01 = file_name + ' ' + error_code
#         if key01 not in dict01.keys():
#             dict01[key01] = 1
#         else:
#             dict01[key01] = dict01[key01] + 1
#         if key01 not in log_list:
#             log_list.append(key01)
#     except:
#         break
# for i in log_list[-8:]:
#     print(i + ' ' + str(dict01[i]))
"""
HJ20 密码验证合格程序
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复
输入描述：
一组或多组长度超过2的字符串。每组占一行
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出描述：
如果符合要求输出：OK，否则输出NG
OK
NG
NG
OK
"""
# import re
# try:
#     while True:
#         s=input()
#         a1 = re.findall(r"\d",s)
#         a2 = re.findall(r"[a-z]",s)
#         a3 = re.findall(r"[A-Z]",s)
#         a4 = re.findall(r"[A-Za-z0-9]",s)
#         a5 = re.findall(r"(.{3,}).*\1",s)
#         list_01 = [a1,a2,a3,a4]
#         if list_01.count([])<=1 and a5==[] and len(s)>8:
#             print("OK")
#         else:
#             print("NG")
# except:
#     pass
"""
HJ21 简单密码
描述
密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
输入描述：
输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾
YUANzhi1987
输出描述：
zvbo9441987
输出渊子真正的密文
"""
# while True:
#     try:
#         s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
#         s2 = 'bcdefghijklmnopqrstuvwxyza222333444555666777788899990123456789'
#         p1 = input()
#         p2 = ''
#         for i in p1:
#             index01 = s1.find(i)
#             p2 = p2 + s2[index01]
#         print(p2)
#     except:
#         break
"""
HJ22 汽水瓶
描述
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？ 
输入描述：
输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=100），表示小张手上的空汽水瓶数。n=0表示输入结束，你的程序不应当处理这一行。
3
10
81
0
输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
1
5
40
"""
# while 1==1:
#     N = int(input())
#     if N == 0:
#         break
#     else:
#         print(int(N/2))
# while True:
#     try:
#         n = int(input())
#         num = 0
#         while n > 2:
#             a = n // 3
#             b = n % 3
#             num = num + a
#             n = a + b
#         if n == 2:
#             num = num+1
#         if num == 0:
#             break
#         print(num)
#     except:
#         break
# 重写
# while True:
#     try:
#         n1 = int(input())
#         he = 0
#         while n1 >=3:
#             n2 = n1//3
#             he = he+n2
#             n3 = n1%3
#             n1 = n2+n3
#         else:
#             if n1 == 2:
#                 he = he+1
#             if n1 == 0:
#                 continue
#         print(he)
#     except:
#         break
"""
HJ23 删除字符串中出现次数最少的字符
描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述：
abcdd
aabcddd
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
输出描述：
删除符串中出现次数最少的字符后的字符串
dd
aaddd
"""
# while True:
#     try:
#         a = input()
#         num = []
#         for word in a:
#             num.append(a.count(word))
#         for word in a:
#             if a.count(word) == min(num):
#                 a = a.replace(word, '')
#         print(a)
#     except:
#         break
"""
HJ26 字符串排序
描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
输入描述：
输入字符串
A Famous Saying: Much Ado About Nothing (2012/8).
输出描述：
输出字符串
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
"""
# try:
#     while True:
#         s = input()
#         a = []
#         for i in s:
#             if i.isalpha():
#                 a.append(i)
#         a.sort(key = lambda k:k.lower()) 不太能理解
#         res = ''
#         for i in s:
#             if i.isalpha():
#                 res += a.pop(0)
#             else:
#                 res += i
#         print(res)
# except:x
#     pass
"""
HJ29 字符串解密
描述
1、对输入的字符串进行加解密，并输出。
2、加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
本题含有多组样例输入。
输入描述：
输入说明
输入一串要加密的密码
输入一串加过密的密码
abcdefg
BCDEFGH
输出描述：
输出说明
输出加密后的字符
输出解密后的字符
BCDEFGH
abcdefg
"""
# a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# b = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
#
# def transfer(s, a, b):
#     output = ""
#     for c in s:
#         if c.isalnum():
#             output += b[a.index(c)]
#         else:
#             break
#     return output
#
# while True:
#     try:
#         s = input()
#         print(transfer(s, a, b))
#         s = input()
#         print(transfer(s, b, a))
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
"""
HJ33 整数与IP地址间的转换
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。
输入描述：
输入 
1 输入IP地址
2 输入10进制型的IP地址
10.0.3.193
167969729
输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址
167773121
10.3.3.193
"""
# def ip_to_num(a):
#     list_01 = a.split('.')
#     str_02 = ''
#     for i in list_01:
#         str_01 = bin(int(i))[2:].zfill(8)
#         str_02 = str_02+str_01
#     convert_num = int(str_02,2)
#     return convert_num
# def num_to_ip(b):
#     str_03 = bin(int(b))[2:].zfill(32)
#     list_02 = []
#     part_01,part_02,part_03,part_04 = str_03[0:8],str_03[8:16],str_03[16:24],str_03[24:32]
#     for i in [part_01,part_02,part_03,part_04]:
#         str_04 = str(int(i,2))
#         list_02.append(str_04)
#     convert_ip = '.'.join(list_02)
#     return convert_ip
# while True:
#     try:
#         a=input()
#         print(ip_to_num(a))
#         b=input()
#         print(num_to_ip(b))
#     except:
#         break
"""
HJ34 图片整理
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过C语言解决。
本题含有多组样例输入。
输入描述：
Lily使用的图片包括"A"到"Z"、"a"到"z"、"0"到"9"。输入字母或数字个数不超过1024。
Ihave1nose2hands10fingers
输出描述：
Lily的所有图片按照从小到大的顺序输出
0112Iaadeeefghhinnnorsssv
"""
# while True:
#     try:
#         str_01 = input()
#         num_list = []
#         upper_list = []
#         lower_list = []
#         for i in str_01:
#             if i.isalnum():
#                 num_list.append(str(i))
#             elif i.isupper():
#                 upper_list.append(i)
#             elif i.lower():
#                 lower_list.append(i)
#         print("".join(num_list) + "".join(upper_list) + "".join(lower_list))
#     except:
#         break
"""
HJ35 蛇形矩阵
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
请注意本题含有多组样例输入。
输入描述：
输入正整数N（N不大于100）
4
输出描述：
输出一个N行的蛇形矩阵。
1 3 6 10
2 5 9
4 8
7
"""
# while True:
#     try:
#         num_01 = int(input())
#         s = 1
#         for i in range(num_01):
#             s = s + i
#             print(s, end=' ')
#             p = s
#             for j in range(i + 1, num_01):
#                 p = p + j + 1
#                 print(p, end=' ')
#             print()
#     except:
#         break
"""
HJ36 字符串加密
描述
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，其余几个丢弃。现在，修改过的那个单词属于字母表的下面，如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。因此，使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
本题有多组输入数据。
输入描述：
先输入key和要加密的字符串
nihao
ni
输出描述：
返回加密后的字符串
le
"""
# while True:
#     try:
#         key = input()
#         pass_01 = input()
#         alpha = 'abcdefghijklmnopqrstuvwxyz'
# #                nihaobcdefgjklmpqrstuvwxyz
#         pass_02 = ''
#         alpha_conv = ''
#         for i in key:
#             if i not in alpha_conv:
#                 alpha_conv += i
#         for i in alpha:
#             if i not in alpha_conv:
#                 alpha_conv += i
#         for i in pass_01:
#             num_01 = alpha.find(i)
#             pass_02 = pass_02 + alpha_conv[num_01]
#         print(pass_02)
#     except:
#         break
"""
HJ37 统计每个月兔子的总数
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
本题有多组数据。
输入描述：
输入int型表示month
9
输出描述：
输出兔子总数int型
34
"""
# while True:
#     try:
#         month=int(input())
#         n=month-1
#         def func(n):
#             if n<2:#基线条件
#                 return 1
#             else:#递归条件
#                 return func(n-1)+func(n-2)
#         print(func(n))
#     except:
#         break
"""
HJ38 求小球落地5次后所经历的路程和第
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
最后的误差判断是小数点6位
输入描述：1
输入起始高度，int型
输出描述：2.875
0.03125
分别输出第5次落地时，共经过多少米第5次反弹多高
"""
# h_01 = int(input())
# dist = h_01
# distance = h_01
# last = 0.0
# for i in range(4):
#     dist = dist / 2
#     distance = distance + dist * 2
# dist = dist / 2
# print('%.6f' % distance)
# print('%.6f' % dist)
"""
HJ40 统计字符
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
本题包含多组输入。
输入描述：
输入一行字符串，可以有空格
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数
26
3
10
12
"""
# while True:
#     try:
#         s = input()
#         en_str = ''
#         spa_str = ''
#         num_str = ''
#         oth_str = ''
#         for i in s:
#             if i.isalpha():
#                 en_str += i
#             elif i.isspace():
#                 spa_str += i
#             elif i.isdigit():
#                 num_str += i
#             else:
#                 oth_str += i
#         print(len(en_str))
#         print(len(spa_str))
#         print(len(num_str))
#         print(len(oth_str))
#     except:
#         break
"""
HJ41 称砝码
描述
现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：
称重重量包括0
输入描述：
输入包含多组测试数据。
对于每组测试数据：
第一行：n --- 砝码数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
2
1 2
2 1
输出描述：
利用给定的砝码可以称出的不同的重量数
5
"""
# while True:
#     try:
#         a = int(input())
#         weight = list(map(int,input().split()))
#         count = list(map(int,input().split()))
#         fm,tmp,ans = [],[],[0]
#         # 将所有的砝码放入列表
#         for i in range(a):
#             for j in range(count[i]):
#                 fm.append(weight[i])
#         # 称重
#         for i in fm:
#             tmp = set(ans)
#             for j in tmp:
#                 ans.append(i+j)
#         #去重
#         res = set(ans)
#         print(len(res))
#     except:
#         break
"""
HJ45 名字的漂亮度
描述
给出一个名字，该名字有26个字符组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。 
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。
本题含有多组数据。
输入描述：
整数N，后续N个名字
2
zhangsan
lisi
输出描述：
每个名称可能的最大漂亮程度
192
101
"""
# while True:
#     try:
#         times = int(input().strip())
#         for i in range(times):
#             name = input().strip()
#             char_dict = {}
#             for key in name:
#                 if key in char_dict.keys():
#                     char_dict[key] += 1
#                 else:
#                     char_dict[key] = 1
# #             print(char_dict)
#             value_list = []
#             for key in char_dict.keys():
#                 value_list.append(char_dict[key])
#             beauty_value = 26
#             total_value = 0
#             value_list.sort(reverse = True)
# #             print(value_list)
#             for num in value_list:
#                 total_value += beauty_value * num
#                 beauty_value -= 1
#             print(total_value)
#     except:
#         break
"""
HJ46 截取字符串
描述
输入一个字符串和一个整数k，截取字符串的前k个字符并输出
本题输入含有多组数据
输入描述：
1.输入待截取的字符串
2.输入一个正整数k，代表截取的长度
abABCcDEF
6
输出描述：
截取后的字符串
abABCc
"""
# while True:
#     try:
#         a = input()
#         b = int(input())
#         print(a[0:b])
#     except:
#         break
"""
HJ49 多线程
问题描述：有4个线程和1个公共的字符数组。线程1的功能就是向数组输出A，线程2的功能就是向字符输出B，线程3的功能就是向数组输出C，线程4的功能就是向数组输出D。要求按顺序向数组赋值ABCDABCDABCD，ABCD的个数由线程函数1的参数指定。[注：C语言选手可使用WINDOWS SDK库函数]
接口说明：
void init();  //初始化函数
void Release(); //资源释放函数
unsignedint__stdcall ThreadFun1(PVOID pM)  ; //线程函数1，传入一个int类型的指针[取值范围：1 – 250，测试用例保证]，用于初始化输出A次数，资源需要线程释放
unsignedint__stdcall ThreadFun2(PVOID pM)  ;//线程函数2，无参数传入
unsignedint__stdcall ThreadFun3(PVOID pM)  ;//线程函数3，无参数传入
Unsigned int __stdcall ThreadFunc4(PVOID pM);//线程函数4，无参数传入
char  g_write[1032]; //线程1,2,3,4按顺序向该数组赋值。不用考虑数组是否越界，测试用例保证
输入描述：
本题含有多个样例输入。
输入一个int整数10
输出描述：
对于每组样例，输出多个ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD
"""
# import threading
# while True:
#     try:
#         arr = []
#         def add_char(char):
#             # global arr
#             arr.append(char)
#         for i in range(int(input())):
#             for j in 'ABCD':
#                 t = threading.Thread(target = add_char,args = (j))
#                 t.start()
#                 t.join()
#         print(''.join(arr))
#     except:
#         break
"""
HJ50 四则运算
描述
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法
输入描述：
输入一个算术表达式3+2*{1+2*[-4/(8-6)+7]}
输出描述：
得到计算结果25
"""
s = input()
s = s.replace('[', '(')
s = s.replace(']', ')')
s = s.replace('{', '(')
s = s.replace('}', ')')
r = eval(s)
print(int(r))
"""
HJ51 输出单向链表中倒数第k个结点
描述

输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。
链表结点定义如下：
struct ListNode
{
int       m_nKey;
ListNode* m_pNext;
};
正常返回倒数第k个结点指针，异常返回空指针
本题有多组样例输入。
输入描述：
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值
输出描述：
输出一个整数
"""
# while True:
#     try:
#         n1 = int(input())
#         l1 = input().strip()
#         n2 = int(input())
#         l2 = l1.split(" ")
#         if n2 !=0:
#             print(l2[-n2])
#         else:
#             print(0)
#     except:
#         break
"""
HJ53 杨辉三角的变形
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。
输入n(n <= 1000000000)
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)等方式读入
输入描述：
输入一个int整数
输出描述：
输出返回的int值
"""
# while True:
#     try:
#         a = int(input())
#         if a%2 == 1:
#             b = 2
#         elif a%4 == 0:
#             b= 3
#         elif a < 3:
#             b= -1
#         else:
#             b= 4
#         print(b)
#     except:
#         break
"""
HJ54 表达式求值
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过100，合法的字符包括”+, -, *, /, (, )”，”0-9”，字符串内容的合法性及表达式语法的合法性由做题者检查。本题目只涉及整型计算。
输入描述：
输入算术表达式400+5
输出描述：
计算出结果值405
"""
print(eval(input()))
"""
HJ55 挑7
描述
输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数（一组测试用例里可能有多组数据，请注意处理）
输入描述：
一个正整数N。(N不大于30000)
20
10
输出描述：
不大于N的与7有关的数字个数，例如输入20，与7有关的数字包括7,14,17.
3
1
"""
# while True:
#     try:
#         s = int(input())
#         s01 = set()
#         for i in range(s+1):
#             if i == 0:
#                 continue
#             if i%7 == 0:
#                 s01.add(i)
#             if '7' in str(i):
#                 s01.add(i)
#         print(len(s01))
#     except:
#         break
"""
HJ56 完全数计算
描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s
输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
本题输入含有多组样例。
输入描述：
输入一个数字n
1000
7
100
输出描述：
输出不超过n的完全数的个数
3
1
2
"""
# while True:
#     try:
#         n = int(input())  # 输入
#         m = 0  # 输出，即个数
#         for i in range(2,n+1):  # 第一重循环，遍历从2-n的数，每一次遍历都是判断是否存在
#             s = 1   # 总和，1必定是因子，所以先加上
#             for j in range(2,i):  # 第二重循环，为了找因子，从2开始遍历
#                 if i % j ==0:
#                     s += j  # 是的话，就加上
#             if s == i:  # 最后判断是否是完全数，如果是就计上
#                 m += 1
#         print(m)
#     except:
#         break
"""
HJ57 高精度整数加法
描述
输入两个用字符串表示的整数，求它们所表示的数之和。
字符串的长度不超过10000。
本题含有多组样例输入。
输入描述：
输入两个字符串。保证字符串只含有'0'~'9'字符
9876543210
1234567890
输出描述：
输出求和后的结果
11111111100
"""
# while True:
#     try:
#         s1 = int(input())
#         s2 = int(input())
#         n3 = s1+s2
#         print(str(n3))
#     except:
#         break
"""
HJ58 输入n个整数，输出其中最小的k个
描述
输入n个整数，输出其中最小的k个。
本题有多组输入样例，请使用循环读入，比如while(cin>>)等方式处理
输入描述：
第一行输入两个整数n和k
第二行输入一个整数数组
5 2
1 3 5 7 2
输出描述：
输出一个从小到大排序的整数数组
1 2
"""
# while True:
#     try:
#         s = input()
#         list_01 = s.split(" ")
#         n = int(list_01[0]) if int(list_01[0]) < int(list_01[1]) else int(list_01[1])
#         s2 = input().strip()
#         list_02 = s2.split(" ")
#         list_04 = []
#         for i in list_02:
#             list_04.append(int(i))
#         list_04.sort()
#         list_03 = list_04[0:int(n)]
#         list_05 = []
#         for i in list_03:
#             list_05.append(str(i))
#         s3 = " ".join(list_05)
#         print(s3)
#     except:
#         break
"""
HJ59 找出字符串中第一个只出现一次的字符
输入描述：
输入几个非空字符串
asdfasdfo
aabb
输出描述：
输出第一个只出现一次的字符，如果不存在输出-1
o
-1
"""
# while True:
#     try:
#         s = input()
#         n1 = 0
#         n2 = -1
#         list1 = []
#         for i in s:
#             if s.count(i) == 1:
#                 n1 = n1 + 1
#                 list1.append(i)
#         if n1 ==0:
#             print(n2)
#         else:
#             print(list1[0])
#     except:
#         break
"""
HJ60 查找组成一个偶数最接近的两个素数
描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。
本题含有多组样例输入。
输入描述：
输入一个偶数
20
输出描述：
输出两个素数
7
13
"""
# def is_prime(x):
#     if x < 2:
#         return False
#     for n in range(2, x):
#         if x % n == 0:
#             return False
#     return True
#
# while True:
#     try:
#         n = int(input())
#         for i in range(n//2, 1, -1):
#             if is_prime(i) and is_prime(n-i):
#                 print(i,n-i,sep='\n')
#                 break
#     except:
#         break
"""
HJ61 放苹果
描述
题目描述
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
数据范围：0<=m<=10，1<=n<=10。
本题含有多组样例输入。
输入描述：
输入两个int整数
7 3
输出描述：
输出结果，int型
8
"""
'''
解题思路：
f(m,n)表示将m个苹果放入n个盘子中的摆放方法总数，
放苹果分为两种情况，一种是有1个盘子为空 f(m,n-1)，另一种是每个盘子上至少有1个苹果f(m-n,n)，
递推关系：f(m,n) = f(m,n-1) + f(m-n,n)
边界条件：当m==1 or n==1时，f(m,n) =1
'''
# def f(m,n):
#     if m<0 or n<0:
#         return 0
#     elif m==1 or n==1:
#         return 1
#     else:
#         return f(m,n-1) + f(m-n,n)
#
# while 1:
#     try:
#         m,n = map(int,input().strip().split())
#         print(f(m,n))
#     except:
#         break
"""
HJ62 查找输入整数二进制中1
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！
输入描述：
输入一个整数5
输出描述：
计算整数二进制中1的个数2
"""
# while True:
#     try:
#         n1 = int(input())
#         s1 = bin(n1)
#         n2 = s1.count('1')
#         print(n2)
#     except:
#         break
"""
HJ63 DNA序列
描述
一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
给定一个很长的DNA序列，以及限定的子串长度N，请帮助研究人员在给出的DNA序列中从左往右找出GC-Ratio最高且长度为N的第一个子串。
DNA序列为ACGT的子串有:ACG,CG,CGT等等，但是没有AGT，CT等等
输入描述：
输入一个string型基因序列，和int型子串的长度
ACGT
2
输出描述：
找出GC比例最高的子串,如果有多个则输出第一个的子串
CG
"""
# while True:
#     try:
#         s1 = input()
#         n1 = int(input())
#         list01 = []
#         for i in range(len(s1)-n1+1):
#             list01.append(s1[i:i+n1])
#         list_02 = [i.count('C')+i.count('G') for i in list01]
#         n = max(list_02)
#         index_01 = list_02.index(n)
#         print(list01[index_01])
#     except:
#         break
"""
HJ65 查找两个字符串a,b中的最长公共子串
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
本题含有多组输入数据！
输入描述：
输入两个字符串
输出描述：
返回重复出现的字符
"""
# while True:
#     try:
#         s1 = input()
#         s2 = input()
#         if len(s1) <= len(s2):
#             sho = s1
#             lon = s2
#         else:
#             sho = s2
#             lon = s1
#         s3 = ""
#         for i in range(0,len(sho)):
#             for j in range(1,len(sho) + 1):
#                 if sho[i:j] in lon:
#                     if len(sho[i:j]) > len(s3):
#                         s3 = sho[i:j]
#         print(s3)
#     except:
#         break
"""
HJ66 配置文件恢复
描述

有6条配置命令，它们执行的结果分别是：
命   令	执   行
reset	reset what
reset board	board fault
board add	where to add
board delete	no board at all
reboot backplane	impossible
backplane abort	install first
he he	unknown command
注意：he he不是命令。
为了简化输入，方便用户，以“最短唯一匹配原则”匹配：
1、若只输入一字串，则只匹配一个关键字的命令行。例如输入：r，根据该规则，匹配命令reset，执行结果为：reset what；输入：res，根据该规则，匹配命令reset，执行结果为：reset what； 
2、若只输入一字串，但本条命令有两个关键字，则匹配失败。例如输入：reb，可以找到命令reboot backpalne，但是该命令有两个关键词，所有匹配失败，执行结果为：unknown command 
3、若输入两字串，则先匹配第一关键字，如果有匹配但不唯一，继续匹配第二关键字，如果仍不唯一，匹配失败。例如输入：r b，找到匹配命令reset board 和 reboot backplane，执行结果为：unknown command。
4、若输入两字串，则先匹配第一关键字，如果有匹配但不唯一，继续匹配第二关键字，如果唯一，匹配成功。例如输入：b a，无法确定是命令board add还是backplane abort，匹配失败。
5、若输入两字串，第一关键字匹配成功，则匹配第二关键字，若无匹配，失败。例如输入：bo a，确定是命令board add，匹配成功。
6、若匹配失败，打印“unknown command”
输入描述：
reset
reset board
board add
board delet
reboot backplane
backplane abort
多行字符串，每行字符串一条命令
输出描述：
reset what
board fault
where to add
no board at all
impossible
install first
执行结果，每条命令输出一行
"""
# invalid = 'unknown command'
# while True:
#     try:
#         dd = {'reset': 'reset what',
#               'reset board': 'board fault',
#               'board add': 'where to add',
#               'board delete': 'no board at all',
#               'reboot backplane': 'impossible',
#               'backplane abort': 'install first',
#               'he he': 'unknown command'
#               }
#         out = ''
#         i = input().split()
#         count = 0
#         for j in dd:
#             if len(i) == 2:
#                 if i[0] in j and i[1] in j:
#                     count += 1
#                     out = dd[j]
#             elif len(i) == 1:
#                 if i[0] in j:
#                     if len(j.split()) == 1:
#                         count += 1
#                         out = dd[j]
#         if count == 1:
#             print(out)
#         else:
#             print(invalid)
#     except:
#         break
"""
HJ84 统计大写字母个数
描述
找出给定字符串中大写字符(即'A'-'Z')的个数。
输入描述：
本题含有多组样例输入
对于每组样例，输入一行，代表待统计的字符串
add123#$%#%#O
150175017(&^%&$vabovbao
输出描述：
对于每组样例，输出一个整数，代表字符串中大写字母的个数
1
0
"""
# while True:
#     try:
#         s = input()
#         n = 0
#         for i in s:
#             if i.isupper():
#                 n = n + 1
#             else:
#                 continue
#         print(n)
#     except:
#         break
"""
HJ68 成绩排序
描述
查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
例示：
jack      70
peter     96
Tom       70
smith     67
从高到低  成绩 
peter     96 
jack      70 
Tom       70 
smith     67
从低到高
smith     67
jack      70
Tom       70 
peter     96
注：0代表从高到低，1代表从低到高
本题含有多组输入数据！
输入描述：
输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开
输出描述：
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
"""
# while True:
#     try:
#         n1 = int(input())
#         n2 = int(input())
#         list01 = []
#         for i in range(n1):
#             ele01 = input().split(" ")
#             list01.append(ele01)
#         for i in sorted(list01,key = lambda e:int(e[1]),reverse = 1-n2):
#             print(" ".join(i))
#     except:
#         break
"""
HJ71 字符串通配符
描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（字符由英文字母，数字0-9和 '.' 组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
输入：
通配符表达式；
一组字符串。
输出：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
本题含有多组样例输入！
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串
te?t*.*
txt12.xls
输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
false
"""
# import re
# while True:
#     try:
#         p, s = str(input()), str(input())
#         a = "[a-zA-Z0-9.]{0,}"
#         b = "[a-zA-Z0-9.]{1}"
#         p = p.replace('*', a)
#         p = p.replace('?', b)
#         x = re.search(p, s, re.I) #忽略大小写
#         if not x: #如果没有匹配的则结束
#             print('false')
#             continue
#         elif s in x.group(): # 有匹配项则判断匹配项是否存在s
#             print('true')
#         else:
#             print('false')
#     except:
#         break
# import re
# while True:
#     try:
#         reg01 = str(input())
#         sen01 = str(input())
#         prin01 = '[a-zA-Z0-9.]{0,}'
#         prin02 = '[a-zA-Z0-9.]{1}'
#         reg01 = reg01.replace('*', prin01)
#         reg01 = reg01.replace('?', prin02)
#         res01 = re.search(reg01, sen01, re.I)
#         if not res01:
#             print('false')
#             continue
#         elif sen01 in res01.group():
#             print('true')
#         else:
#             print('false')
#     except:
#         break
"""
HJ72 百钱买百鸡问题
描述
公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
详细描述：
接口说明
原型：
int GetResult(vector &list)
输入参数：
        无
输出参数（指针指向的内存区域保证有效）：
    list  鸡翁、鸡母、鸡雏组合的列表
返回值：
     -1 失败     
     0 成功
输入描述：
输入任何一个整数，即可运行程序。
1
输出描述：
0 25 75
4 18 78
8 11 81
12 4 84
"""
# n1 = input()
# for i in range(20):
#     for j in range(33):
#         if 5*i + 3*j + 1/3*(100-i-j) == 100:
# #             print('{} {} {}'.format(i,j,100-i-j))
#             print('%d %d %d' % (i,j,100-i-j))
"""
HJ73 计算日期到天数转换
描述
根据输入的日期，计算是这一年的第几天。
输入描述：
输入一行，每行空格分割，分别是年，月，日
输出描述：
输出是这一年的第几天
"""
# while True:
#     try:
#         in01 = input()
#         year, month, day = map(int, in01.split(' '))
#
#         if year <= 0 or month <= 0 or month > 12 or day <= 0 or day > 31:
#             continue
#         else:
#             month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#             if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#                 days = sum(month_day[0:(month - 1)]) + day
#                 print(days)
#             else:
#                 month_day[1] = 28
#                 days = sum(month_day[0:(month - 1)]) + day
#                 print(days)
#     except:
#         break
"""
HJ74 参数解析
描述
在命令行输入如下命令：
xcopy /s c:\ d:\，
各个参数如下：
参数1：命令字xcopy
参数2：字符串/s
参数3：字符串c:\
参数4: 字符串d:\
请编写一个参数解析程序，实现将命令行各个参数解析出来。
解析规则：
1.参数分隔符为空格 
2.对于用""包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy /s "C:\program files" "d:\"时，参数仍然是4个，第3个参数应该是字符串C:\program files，而不是C:\program，注意输出参数时，需要将""去掉，引号不存在嵌套情况。
3.参数不定长 
4.输入由用例保证，不会出现不符合要求的输入
输入描述：
输入一行字符串，可以有空格
xcopy /s c:\\ d:\\
输出描述：
输出参数个数，分解后的参数，每个参数都独占一行
4
xcopy
/s
c:\\
d:\\
"""
# import re
# while True:
#     try:
#         s = input()
#         reg01 = r'([^ "]+)|(".+?")'
#         list01 = list(re.finditer(reg01, s))
#         print(len(list01))
#         for i in list01:
#             print(i.group().strip('"'))
#     except:
#         break
# import re

# params = list(re.finditer(r'([^ "]+)|(".+?")', input()))
# print(len(params))
# for p in params:
#     print(p.group().strip('"'))
"""
HJ75 公共子串计算
描述
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
输入描述：
输入两个只包含小写字母的字符串
asdfas
werasdfaswer
输出描述：
输出一个整数，代表最大公共子串的长度
6
"""
# while True:
#     try:
#         s1 = input()
#         s2 = input()
#         if len(s1) <= len(s2):
#             min_str = s1
#             max_str = s2
#         else:
#             min_str = s2
#             max_str = s1
#         s3 = ""
#         for i in range(0,len(min_str)):
#             for j in range(1,len(min_str)+1):
#                 if min_str[i:j] in max_str:
#                     if len(min_str[i:j]) > len(s3):
#                         s3 = min_str[i:j]
#         print(len(s3))
#     except:
#         break
"""
HJ76 尼科彻斯定理
描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
本题含有多组输入数据。
输入描述：
输入一个int整数
输出描
输出分解后的string
"""
# 第一个是我的答案，借鉴了代码3的字符串的倒序比较，字符串1/2比较法难度较大
# while True:
#     try:
#         m = int(input())
#         m3 = m**3
#         list01 = []
#         for i in range(1,m3,2):
#             list01.append(i)
#         for i in range(len(list01)-m):
#             list02 = list01[i:m+i]
#             s = sum(list02[0:m])
#             if s != m3:
#                 continue
#             else:
#                 list03 = [str(j) for j in list02]
#                 print('+'.join(list03))
#     except:
#         break
# while True:
#     try:
#        a=int(input())
#        num=[]
#        b=a**2-a+1
#        for i in range(a):
#            c=b+2*i
#            num.append(str(c))
#        print("+".join(num))
#     except:
#        break
#
# while True:
#     try:
#         m = int(input())
#         s = []
#         for i in range(1, m**3):  # 最大基数一定小于基数之和，即:m**3
#             if i%2 != 0:
#                 s.append(i)  # 将1到m**3的基数，从小到大逐一追加到列表 s
#                 if m ** 3 == sum(s[-m:]):
#                     s = s[-m:]  # 如果追加某个基数后，列表最后m位之和正好等于 m**3 时，将列表 s 重新赋值为所要找的那 m 个基数
#                     break   # 找到那 m 个基数结束当前循环以节约时间
#         result = str(s[0])  # 输出结果初始赋值列表s的第一个数
#         for k in range(1, m):
#             result += '+'+str(s[k])
#         print(result)
#     except:
#         break
"""
HJ80 整型数组合并
描述
题目标题：
将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。
请注意本题有多组样例。
输入描述：
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值
3
1 2 5
4
-1 0 3 2
输出描述：
输出合并之后的数组
-101235
"""
# while True:
#     try:
#         set01 = set()
#         str01 = ''
#         s1 = int(input())
#         list01 = input().strip().split()
#         list02 = [int(i) for i in list01]
#         for j in range(s1):
#             set01.add(list02[j])
#         s2 = int(input())
#         list03 = input().strip().split()
#         list04 = [int(i) for i in list03]
#         for j in range(s2):
#             set01.add(list04[j])
#         for i in sorted(set01):
#             str01=str01+str(i)
#         print(str01)
#     except:
#         break
"""
HJ81 字符串字符匹配
描述
判断短字符串S中的所有字符是否在长字符串T中全部出现。
请注意本题有多组样例输入。
数据范围:1<=len(S),len(T)<=200
输入描述：
输入两个字符串。第一个为短字符串，第二个为长字符串。两个字符串均由小写字母组成。
bc
abc
apgmlivuembu
tyjmrcuneguxmsqwjslqvfmw
bca
abc
输出描述：
如果短字符串的所有字符均在长字符串中出现过，则输出字符串"true"。否则输出字符串"false"。
true
false
true
"""
# while True:
#     try:
#         s1 = input()
#         s2 = input()
#         list1 = []
#         for i in s1:
#             if i in s2:
#                 list1.append("0")
#             else:
#                 list1.append("1")
#         if "1" in list1:
#             print('false')
#         else:
#             print('true')
#     except:
#         break
"""
HJ83 二维数组操作
描述

有一个大小的数据表，你会依次进行以下5种操作：
1.输入和，初始化大小的表格。
2.输入
x
1
x 
1
​	
 、
y
1
y 
1
​	
 、
x
2
x 
2
​	
 、
y
2
y 
2
​	
 ，交换坐标在
(
x
1
,
y
1
)
(x 
1
​	
 ,y 
1
​	
 )和
(
x
2
,
y
2
)
(x 
2
​	
 ,y 
2
​	
 )的两个数。
3.输入，在第行上方添加一行。
4.输入，在第列左边添加一列。
5.输入、，查找坐标为的单元格的值。
请编写程序，判断对表格的各种操作是否合法。
详细要求:
1.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误。
2.对于插入操作，如果插入后行数或列数超过9了则应返回错误。如果插入成功了则将数据表恢复至初始化的大小，多出的数据则应舍弃。
3.所有输入坐标操作，对大小的表格，行号坐标只允许0~m-1，列号坐标只允许0~n-1。超出范围应该返回错误。
本题含有多组样例输入！
输入描述：

输入数据按下列顺序输入：
1 表格的行列值
2 要交换的两个单元格的行列值
3 输入要插入的行的数值
4 输入要插入的列的数值
5 输入要查询的单元格的坐标
4 9
5 1 2 6
0
8
2 3
4 7
4 2 3 2
3
3
4 7
输出描述：
输出按下列顺序输出：
1 初始化表格是否成功，若成功则返回0， 否则返回-1
2 输出交换单元格是否成功
3 输出插入行是否成功
4 输出插入列是否成功
5 输出查询单元格数据是否成功
0
-1
0
-1
0
0
-1
0
0
-1

"""
# while True:
#     try:
#         m,n = map(int,input().split())
#         if m < 0 and m > 9 and n < 0 and n > 9:
#             print('-1')
#         else:
#             print('0')
#             x1,y1,x2,y2 = map(int,input().split())
#             if (0<=x1<m) and (0<=y1<n) and (0<=x2<m) and (0<=y2<n):
#                 print('0')
#             else:
#                 print('-1')
#             i_m=int(input())
#             if (0<=i_m<m) and m<9 :
#                 print('0')
#             else:
#                 print('-1')
#             i_n=int(input())
#             if (0<=i_n<n) and n<9:
#                 print('0')
#             else:
#                 print('-1')
#             x,y = map(int,input().split())
#             if (0<=x<m) and (0<=y<n):
#                 print('0')
#             else:
#                 print('-1')
#     except:
#         break
"""
HJ84 统计大写字母个数
描述
找出给定字符串中大写字符(即'A'-'Z')的个数。
输入描述：
本题含有多组样例输入
对于每组样例，输入一行，代表待统计的字符串
add123#$%#%#O
150175017(&^%&$vabovbao
输出描述：
对于每组样例，输出一个整数，代表字符串中大写字母的个数
1
0
"""
# while True:
#     try:
#         s = input()
#         n = 0
#         for i in s:
#             if i.isupper():
#                 n = n + 1
#             else:
#                 continue
#         print(n)
#     except:
#         break
"""
HJ85 最长回文子串
描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
（注意：记得加上while处理多个测试用例）
输入描述：
输入一个仅包含小写字母的字符串
输出描述：
返回最长回文子串的长度
"""
# while True:
#     try:
#         s1 = input()
#         s2 = ''
#         for i in range(0,len(s1)):
#             for j in range(i,(len(s1)+1)):
#                 s3 = s1[i:j]
#                 if s3==s3[::-1] and len(s3)>len(s2):
#                     s2 = s3
#         print(len(s2))
#     except:
#         break
"""
HJ86 求最大连续bit数
描述
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
本题含有多组样例输入。
输入描述：
输入一个int类型数字
3
5
200
输出描述：
输出转成二进制之后连续1的个数
2
1
2
"""
# while True:
#     try:
#         n1 = int(input())
#         s2 = str(bin(n1)[2:])
#         list1 = s2.split('0')
#         n1 = 0
#         for i in list1:
#             if len(i) > n1:
#                 n1 = len(i)
#         print(n1)
#     except:
#         break
"""
HJ87 密码强度等级
描述

密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符
二、字母:
0 分: 没有字母
10 分: 全都是小（大）写字母
20 分: 大小写混合字母
三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字
四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号
五、奖励:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号
最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱

对应输出为：
VERY_SECURE

SECURE

VERY_STRONG

STRONG

AVERAGE

WEAK

VERY_WEAK


请根据输入的密码字符串，进行安全评定。
注：
字母：a-z, A-Z
数字：0-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
!"#$%&'()*+,-./     (ASCII码：0x21~0x2F)
:;<=>?@             (ASCII码：0x3A~0x40)
[\]^_`              (ASCII码：0x5B~0x60)
{|}~                (ASCII码：0x7B~0x7E)


提示:
1 <= 字符串的长度<= 300
输入描述：

本题含有多组输入样例。
每组样例输入一个string的密码
38$@NoNoNo
123
输出描述：

每组样例输出密码等级
VERY_SECURE
WEAK
"""
# 思路：将统计情况放主函数中一起写，避免分开写时多次遍历密码字符串。

# while True:
#     try:
#         password = input().strip()
#         score = 0  # 初始化得分为0
#         # 长度得分
#         if len(password) <= 4:
#             score += 5
#         elif 5 <= len(password) <= 7:
#             score += 10
#         else:
#             score += 25
#         # 字母、数字、符号统计(是否出现过、出现的个数)
#         alpha, Alpha, digit, digit_num, symbol, symbol_num = 0, 0, 0, 0, 0, 0
#         for ch in password:
#             if ch.islower():
#                 alpha = 1
#             elif ch.isupper():
#                 Alpha = 1
#             elif ch.isdigit():
#                 digit = 1
#                 digit_num += 1
#             else:
#                 symbol = 1
#                 symbol_num += 1
#         # 字母得分
#         if (alpha and not Alpha) or (Alpha and not alpha):
#             score += 10
#         elif alpha and Alpha:
#             score += 20
#         # 数字得分
#         if digit_num == 1:
#             score += 10
#         elif digit_num > 1:
#             score += 20
#         # 符号得分
#         if symbol_num == 1:
#             score += 10
#         elif symbol_num > 1:
#             score += 25
#         # 奖励得分
#         # 此写法错误，本该属于第三种加分的情况被第二种加分情况拦截住了，加成了第二种情况的分数。
#         # if (alpha or Alpha) and digit and not symbol:
#         #     score += 2
#         # elif (alpha or Alpha) and digit and symbol:
#         #     score += 3
#         # elif alpha and Alpha and digit and symbol:
#         #     score += 5
#         if alpha and Alpha and digit and symbol:
#             score += 5
#         elif (alpha or Alpha) and digit and symbol:
#             score += 3
#         elif (alpha or Alpha) and digit:
#             score += 2
#         # 分数等级
#         if score >= 90:
#             print('VERY_SECURE')
#         elif score >= 80:
#             print('SECURE')
#         elif score >= 70:
#             print('VERY_STRONG')
#         elif score >= 60:
#             print('STRONG')
#         elif score >= 50:
#             print('AVERAGE')
#         elif score >= 25:
#             print('WEAK')
#         else:
#             print('VERY_WEAK')
#     except:
#         break

# while True:
#     try:
#         s = input()
#         score = 0
#         if len(s) <= 4:
#             score += 5
#         elif 5 <= len(s) <= 7:
#             score += 10
#         else:
#             score += 25
#         b_alpha,s_alpha,dig,dig_num,sym,sym_num = 0,0,0,0,0,0
#         for i in s:
#             if i.isupper():
#                 b_alpha = 1
#             elif i.islower():
#                 s_alpha = 1
#             elif i.isdigit():
#                 dig = 1
#                 dig_num += 1
#             else:
#                 sym = 1
#                 sym_num += 1
#         if (b_alpha and not s_alpha) or (s_alpha and not b_alpha):
#             score += 10
#         elif b_alpha and s_alpha:
#             score += 20
#         else:
#             score += 0
#         if dig_num > 1:
#             score += 20
#         elif dig_num == 1:
#             score += 10
#         else:
#             score += 0
#         if sym_num > 1:
#             score += 25
#         elif sym_num == 1:
#             score += 10
#         else:
#             score += 0
#         if b_alpha and s_alpha and dig and sym:
#             score += 5
#         elif (b_alpha or s_alpha) and dig and sym:
#             score += 3
#         else:
#             score +=2
#         if score >= 90:
#             print('VERY_SECURE')
#         elif score >= 80:
#             print('SECURE')
#         elif score >= 70:
#             print('VERY_STRONG')
#         elif score >= 60:
#             print('STRONG')
#         elif score >= 50:
#             print('AVERAGE')
#         elif score >= 25:
#             print('WEAK')
#         else:
#             print('VERY_WEAK')
#     except:
#         break
"""
HJ88 扑克牌大小
描述
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A、2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）：
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如：4 4 4 4-joker JOKER。
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR。
基本规则：
（1）输入每手牌可能是个子、对子、顺子（连续5张）、三个、炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）；
（3）大小规则跟大家平时了解的常见规则相同，个子、对子、三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。
输入描述：
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如 4 4 4 4-joker JOKER。
4 4 4 4-joker JOKER
输出描述：
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。
joker JOKER
"""
# while True:
#     try:
#         p1,p2 = input().split('-')
#         list1 = p1.split()
#         list2 = p2.split()
#         pai = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,'J':11,'Q':12,'K':13,'A':14,'2':15,'joker':16,'JOKER':17}
#         if p1 == 'joker JOKER':
#             print('joker JOKER')
#         elif p2 == 'joker JOKER':
#             print('joker JOKER')
#         elif len(list1) == 4 and len(list2) != 4:
#             print(p1)
#         elif len(list2) == 4 and len(list1) != 4:
#             print(p2)
#         elif len(list1) != len(list2):
#             print('ERROR')
#         else:
#             print(p1) if pai[list1[0]] > pai[list2[0]] else print(p2)
#     except:
#         break
"""
HJ90 合法IP
描述
现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此不需要用正号出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
现在需要你用程序来判断IP是否合法。
注意本题有多组样例输入。
输入描述：
输入一个ip地址，保证是xx.xx.xx.xx的形式（xx为整数）
10.138.15.1
255.0.0.255
255.255.255.1000
输出描述：
返回判断的结果YES or NO
YES
YES
NO
"""
# while True:
#     try:
#         ip = input().strip()
#         list1 = [int(i) for i in ip.split('.')]
#         list2 = []
#         for i in list1:
#             if 0 <= i <= 255:
#                 list2.append('0')
#             else:
#                 list2.append('1')
#         if '1' in list2:
#             print('NO')
#         else:
#             print('YES')
#     except:
#         break
"""
HJ91 走方格的方案数
描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
本题含有多组样例输入。
输入描述：
每组样例输入两个正整数n和m，用空格隔开。(1≤n,m≤8)
2 2
1 2
输出描述：
每组样例输出一行结果
6
3
"""
# 没有做出来的题
# while True:
#     try:
#         n,m=map(int,input().split())
#         c=[[1 for i in range(m+1)] for j in range(n+1)] #初始化边界全为1
#         print(c)
#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                  #大家会奇怪为啥第三个c[i][j-1]的是j-1，根据动态规划法C[I][J]=C[I-1][J]+C[I][J+1]才对啊
#                  #这是因为两层for的原因，都是从1 起步。所以就相当于从右上角到左下角的向下走法，两种走法的结果一致
#                 c[i][j]=c[i-1][j]+c[i][j-1]
#         print(c[n][m])
#     except:
#         break
"""
HJ92 在字符串中找出连续最长的数字串
描述
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
本题含有多组样例输入。
输入描述：
输入一个字符串。1<=len(字符串)<=200
abcd12345ed125ss123058789
a8a72a6a5yy98y65ee1r2
输出描述：
输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。
123058789,9
729865,2
"""
# while True:
#     try:
#         s1 = input().strip()
#         for i in s1:
#             if i.isalpha():
#                 s1 = s1.replace(i, ' ')
#         list1 = s1.split()
#         n1 = max(len(i) for i in list1)
#         list2 = []
#         for i in list1:
#             if len(i) == n1:
#                 list2.append(i)
#         n2 = len(list2[0])
#         print(''.join(list2) + ',' + str(n2))
#     except:
#         break
"""
HJ94 记票统计
描述
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
本题有多组样例输入。
输入描述：
输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），第三行输入投票人的人数，第四行输入投票。
4
A B C D
8
A D E CF A GG A B
输出描述：
按照输入的顺序，每行输出候选人的名字和得票数量，最后一行输出不合法的票数。
A : 3
B : 1
C : 0
D : 1
Invalid : 3
 """
# 第一次做错了，理解为候选人只有ABCD，只通过了示例的调试
# while True:
#     try:
#         n1 = int(input())
#         s1 = input()
#         list1 = s1.split()
#         n2 = int(input())
#         s2 = input()
#         list2 = s2.split()
#         list3 = []
#         for i in list1:
#             n3 = list2.count(i)
#             list3.append(n3)
#             print(i + ' : ' + str(n3))
#         print('Invalid' + ' : ' + str(n2 - sum(list3)))
#     except:
#         break
"""
HJ96 表示数字
描述
将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。
注意：本题有多组样例输入。
输入描述：
输入一个字符串
Jkdi234klowe90a3
5151
输出描述：
字符中所有出现的数字前后加上符号“*”，其他字符保持不变
Jkdi*234*klowe*90*a*3*
*5151*
"""
# while True:
#     try:
#         s1 = input()
#         s2 = ''
#         s3 = ' ' + s1 + ' '
#         for i in range(len(s3) - 1):
#             s2 += s3[i]
#             if (s3[i].isdigit() and not s3[i+1].isdigit()) or (s3[i+1].isdigit() and not s3[i].isdigit()):
#                 s2 += '*'
#         print(s2.strip())
#     except:
#         break

"""
HJ97 记负均正
描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
0即不是正整数，也不是负数，不计入计算
输入描述：
本题有多组输入用例。
首先输入一个正整数n，
然后输入n个整数。
5
1 2 3 4 5
10 
1 2 3 4 5 6 7 8 9 0
输出描述：
输出负数的个数，和所有正整数的平均值。
0 3.0
0 5.0
"""
# while True:
#     try:
#         n1 = int(input())
#         list1 = input().strip().split()
#         list1 = [int(i) for i in list1]
#         list_b = []
#         n2 = 0
#         list_u = []
#         for i in list1:
#             if i == 0:
#                 continue
#             elif i < 0:
#                 list_b.append(i)
#                 n2 += 1
#             else:
#                 list_u.append(i)
#         #           小数点保留小数位方法一
#         #         n3 = round(sum(list_u) / len(list_u),1)
#         #         print(str(n2) + ' ' + str(n3))
#         #           小数点保留小数位方法二
#         n3 = sum(list_u) / len(list_u)
#         print(str(n2) + ' ' + str("%.1f" % n3))
#
#     except:
#         break
"""
HJ99 自守数
描述
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数
接口说明
/*
功能: 求出n以内的自守数的个数
输入参数：
int n
返回值：
n以内自守数的数量。
*/
public static int CalcAutomorphicNumbers( int n)
{
/*在这里实现功能*/
return 0;
}
本题有多组输入数据，请使用while(cin>>)等方式处理
输入描述：
int型整数
2000
输出描述：
n以内自守数的数量。
8
"""
# while True:
#     try:
#         n1 = int(input())
#         n3 = 0
#         for i in range(0,(n1+1)):
#             s2 = str(i**2)[-len(str(i)):]
#             if s2 == str(i) :
#                 n3 += 1
#         print(n3)
#     except:
#         break
"""
HJ100 等差数列
功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
本题为多组输入，请使用while(cin>>)等形式读取数据
输入描述：
输入一个正整数。
2
输出描述：
输出一个相加后的整数。
7
"""
# while True:
#     try:
#         n1 = int(input())
#         n3 = 0
#         for i in range(n1):
#             n2 = 2 + (3*i)
#             n3 += n2
#         print(n3)
#     except:
#         break
"""
HJ101 输入整型数组和排序标识，对其元素按照升序或降
描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
8
1 2 4 9 3 55 64 25
0
输出描述：
输出排好序的数字
1 2 3 4 9 25 55 64
"""
# while True:
#     try:
#         n1 = int(input())
#         list2 = [int(i) for i in input().split()]
#         n3 = int(input())
#         if n3 == 0:
#             list2.sort(reverse = False)
#         else:
#             list2.sort(reverse = True)
#         list2 = [str(i) for i in list2]
#         print(' '.join(list2))
#     except:
#         break
"""
HJ102 字符统计
描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
本题含有多组样例输入
输入描述：
一个只包含小写英文字母和数字的字符串。
aaddccdc
1b1bbbbbbbbb
输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
cda
b1
"""
# while True:
#     try:
#         s1 = input().strip()
#         list2 = []
#         dict1 = {}
#         s3 = ''
#         for i in s1:
#             if i not in list2:
#                 list2.append(i)
#         list2.sort()
#         for j in list2:
#             dict1[j] = s1.count(j)
#         list3 = sorted(dict1.items(),key=lambda x:x[1],reverse=True)
#         for k in list3:
#             s3 += k[0]
#         print(s3)
#     except:
#         break
"""
HJ105 记负均正II
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
数据范围小于1e6
输入描述：
输入任意个整数，每行输入一个。
-13
-4
-7
输出描述：
输出负数个数以及所有非负数的平均值
3
0.0
"""
# ans = 0
# num = 0
# neg = 0
# while True:
#     try:
#         n = int(input())
#         if  n > 0:
#             ans += n
#             num += 1
#         else:
#             neg += 1
#     except EOFError:
#         break
# print(neg)
# print(round(ans/num, 1)) if num > 0 else print(0.0)

"""
HJ107 求解立方根
描述
计算一个数字的立方根，不使用库函数。
保留一位小数。
输入描述：
待求解参数，为double类型（一个实数）216
输出描述：
输入参数的立方根。保留一位小数。6.0
"""
# while True:
#     try:
#         n = float(input())
#         if n == 0:
#             print(0)
#         elif n < 0:
#             n = abs(n)
#             print(round(n**(1/3)*(-1),1))
#         else:
#             print(round(n**(1/3),1))
#     except:
#          break
"""
HJ108 求最小公倍数
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
输入描述：
输入两个正整数A和B。
5 7
输出描述：
输出A和B的最小公倍数。
35
"""
# while True:
#     try:
#         a,b = map(int,input().split())
#         list1 = []
#         for i in range(1,min(a,b)+1):
#             if a%i == 0 and b%i == 0:
#                 list1.append(int(a*b/i))
#         print(min(list1))
#     except:
#         break
# #俩个数的最小公倍数等于俩个数的乘积除以俩个数的最大公约数
