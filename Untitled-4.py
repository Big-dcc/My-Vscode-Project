import re


L = [8, 5, 2, 9, 5, 6, 3]
# 冒泡排序


def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


bubble_sort(L)
print(L)

# 正则匹配邮箱
email = "1234a5899@qq.com"
a = re.match("^.+@.+\..+$", email)
print(a)

# 字符串内匹配ip地址
ip = "八达仓库 ip:232.23.9.12 askd "
a = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
print(a)
