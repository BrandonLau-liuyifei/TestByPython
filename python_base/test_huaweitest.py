# ！/usr/bin/env python
# -*- coding：utf-8 -*-
'''HJ01.计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。'''
# a=input("请输入：")
# list_01=a.split()
# print(list_01)
# b=list_01[-1]
# c=len(b)
# print(c)

'''#HJ02.写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写，字符串长度小于500。'''
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
# count_dict = {}
# while True:
#     try:
#         line = input()
#         if not line:
#             continue
#         list_01 = line.split(" ")
#         file_path = list_01[0]
#         error_num = list_01[1]
#         file_name = file_path.split("\\")[-1][-16:]
#         key = file_name +  ' ' + error_num
#         if key not in count_dict.keys():
#             count_dict[key] = 1
#         else:
#             count_dict[key] += 1
#         if key not in log_list:
#             log_list.append(key)
#     except:
#         break
# for i in log_list[-8:]:
#     print(i + " " + str(count_dict[i]))
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
# s=input()
# str_01 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# str_02 = "bcdefghijklmnopqrstuvwxyza22233344455566677778889999"
# s2=''
# for i in s:
#     if i in str_01:
#         index_01 = str_01.find(i)
#         s2=s2+str_02[index_01]
#     else:
#         s2 = s2 + i
# print(s2)
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
# except:
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
