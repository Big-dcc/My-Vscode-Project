
import json
import re


x = '{ "name":"Bill", "age":63, "city":"Seatle"}'
print(type(x))
y = json.loads(x)
print(y)
print(type(y))
print(json.dumps(y, indent=4, sort_keys=True))


txt = "China is a great country"
a = re.search("^China.*country$", txt)
print(a)
