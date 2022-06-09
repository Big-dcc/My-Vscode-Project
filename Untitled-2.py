
import mymodule
import datetime
import time


mymodule.greeting("Bill")
x = dir(mymodule)
print(x)
print(mymodule.person1["name"])


print(dir(datetime))
# print(help(datetime))
print(datetime.datetime)


time_str = time.strftime('%Y-%m-%d/%H-%M-%S')
print(time_str)
print(time.time())
print(time.asctime())
print(time.localtime())
print(time.mktime(time.localtime()))
