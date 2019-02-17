import random

print("""
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.""")

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
