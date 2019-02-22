import random

def newLine(lines):
    print((lines -1) * "\n")

newLine(2)
a = sorted(random.sample(range(30), 15))
b = sorted(random.sample(range(30), 10))
baseLists = a, b

print("Base lists")
for _lists in baseLists:
    print(_lists)

newLine(0)
print("Intersection list")
print(list(set(a).intersection(b)))
newLine(1)
