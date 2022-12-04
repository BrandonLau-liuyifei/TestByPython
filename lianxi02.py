# # -*- coding: utf-8 -*-
# # @Author : Brandon
#
# a = '1'
# print(a.ljust(2, '0'))
# b = '12'
# print(b.rjust(3, '0'))
#
# for i in range(0,101):
#     if i <100:
#         reg = 'regist(12345678{},huawei@123)'.format(str(i).ljust(3,'0'))
#         print(reg,'successful')
#     else:
#         reg = 'regist(12345678{},huawei@123)'.format(str(i).ljust(3, '0'))
#         print(reg, 'failed')
#
# for i in range(0,11):
#     if i< 10:
#         reg = 'regist(12345678{},huaweihuawei)'.format(str(i).ljust(3,'0'))
#         print(reg,'failed')
#     else:
#         reg = 'regist(12345678{},huaweihuawei)'.format(str(i).ljust(3, '0'))
#         print(reg, 'locked')
# passwd = ['aabbccdd','112233445566', 'aaabb112233','qqwweerr6789']
#
# j = 0
# for i in passwd:
#     reg = 'register(123456789{},{})'.format(str(j).ljust(2,'0'),i)
#     print(reg, 'failed')
#     j += 1


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l4 = [str(i) for i in tuple(l1)]
#         l5 = [str(j) for j in tuple(l2)]
#         n1 = int(''.join(l4))
#         n2 = int(''.join(l5))
#         n3 = n1+n2
#         l3 = [ int(i) for i in reversed(list(str(n3)))]
#
#         return l3
#
#
# print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))
# print(Solution().addTwoNumbers([0], [0]))
# print(Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9]))
print(int('0'))


# class Solution:
#     def reverse(self, x: int) -> int:
#         s1 = ''
#         if x>=0:
#             s = str(x)
#             for i in range(len(s)):
#                 s1 += s[-1-i]
#             n = int(s1)
#         else:
#             s = str(x)
#             for i in range(len(s)-1):
#                 s1 += s[-1-i]
#             s2 = s[0]+s1
#             n = int(s2)
#         if n>(-2)**31 and n < 2**31-1:
#             return n
#         else:
#             return 0

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         dict_gewei = {
#             "I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9
#         }
#         dict_shiwei = {
#             "X":10,"XX":20,"XXX":30,"XL":40,"L":50,"LX":60,"LXX":70,"LXXX":80,"XC":90
#         }
#         dict_baiwei = {
#             "C":1,"CC":200,"CCC":300,"CD":400,"D":500,"DC":600,"DCC":700,"DCCC":800,"CM":90
#         }
#         dict_qianwei = {
#             "M":1000
#         }
#         str01 = str(num)
#         n = len(str01)
#         list2 = list()
#         list1 = [dict_gewei, dict_shiwei,dict_baiwei,dict_qianwei]
#         for i in range(n):
#             for item in list1[i].items():
#                 if item[1]==int(str01[-1-i]):
#                     list2.append(item[0])
#         list3 = list2[::-1]
#         str02 = ''.join(list3)
#         return str02

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dict_gewei = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
#         dict_shiwei = {"X": 1, "XX": 2, "XXX": 3, "XL": 4, "L": 5, "LX": 6, "LXX": 7, "LXXX": 8, "XC": 9}
#         dict_baiwei = {"C": 1, "CC": 2, "CCC": 3, "CD": 4, "D": 5, "DC": 6, "DCC": 7, "DCCC": 8, "CM": 9}
#         dict_qianwei = {"M": 1, "MM": 2, 'MMM': 3, 'MMMM': 4}
#         s1 = str()
#         list1 = list()
#         for i in [dict_gewei, dict_shiwei, dict_baiwei, dict_qianwei]:
#             for j in range(len(s) - 3):
#                 key01 = s[-1 - j]
#                 key02 = s[(-2 - j):-1]
#                 key03 = s[(-3 - j):-1]
#
#                 if key01 in i.keys():
#                     n3 = i[key01]
#                     list1.append(i[key01])
#                 elif key02 in i.keys():
#                     list1.append(i[key02])
#                 elif key03 in i.keys():
#                     list1.append(i[key03])
#         list1 = [str(i) for i in list1]
#         s1 = ''.join(list1)
#         s1 = s1[::-1]
#         return s1

class Solution:
    def letterCombinations(self, digits: str):
        a = ['2', '3', '4', '5', '6', '7', '8', '9']
        b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
             ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        list1 = list(digits)
        list2 = []
        list3 = []
        for i in list1:
            if i in a:
                index_01 = a.index[i]
                list2.append(b[index_01])
        if len(digits) == 1:
            for i in list2[0]:
                list3.append(i)
        elif len(digits) == 2:
            for i in list2[0]:
                for j in list2[1]:
                    list3.append(i + j)
        elif len(digits) == 3:
            for i in list2[0]:
                for j in list2[1]:
                    for x in list2[2]:
                        list3.append(i + j + x)
        return list3


if __name__ == '__main__':
    # print(Solution().intToRoman(100))
    # print(Solution().romanToInt('CXCV'))
    print(Solution().letterCombinations('23'))
    # dict_gewei = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
    # print(dict_gewei['I'])
