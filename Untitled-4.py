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
print(a.group())

# 字符串内匹配ip地址
ip = "232.23.9.12"
a = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
print(a)
b = re.match('(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}', ip)
print(b)
obj = re.findall('\d+?', 'u123uu888asf')
if obj:
    print(obj)
content = "123abc456"
# new_content = re.sub('\d+', 'sb', content)
new_content = re.sub('[a-z]+', 'sb', content, 1)
print(new_content)
content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new_content = re.split('[\+\-\*\/]+', content)
# new_content = re.split('\*', content, 1)
print(new_content)
