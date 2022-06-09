import time


def new_func():
    for i in range(0, 10):
        print(i)
        if i == 5:
            print("ok")
            print(time.time)

    for b in ["1", "2", "3"]:
        print(b)


new_func()

i = 1
while i < 7:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print("end")
i = 1
while i < 7:
    print(i)
    if i == 3:
        break
    i += 1

thislist = ["apple", "banana", "cherry"]
if "appe" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, applep is not in the fruits")
thislist.append("orange")
print(thislist)

thisdict = {"brand": "Porsche", "model": "911", "year": 1963}
print(thisdict)
print(thisdict["model"])
for n in thisdict:
    print(thisdict[n])
for x, y in thisdict.items():
    print(x, y)

for x in range(3, 50, 6):
    print(x)
print("===========分割线===========")


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
        print("................")
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")

tri_recursion(3)

x = lambda a: a + 10

print(x(3))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Bill", 63)
p1.myfunc()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# 使用 Person 来创建对象，然后执行 printname 方法：


x = Person("Bill", "Gates")
x.printname()
