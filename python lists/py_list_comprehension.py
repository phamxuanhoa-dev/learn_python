# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist1 = [x for x in fruits if "a" in x]
# the syntax
# newlist = [expression for item in iterable if condition == True]

# iterable
newlist2 = [x for x in range(10)]
print(newlist2)