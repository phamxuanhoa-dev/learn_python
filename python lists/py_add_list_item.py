# append item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("\n")

# insert item
thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(1, "orange")
print(thislist1)
print("\n")

# extend list
thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)
print(thislist2)
print("\n")

# Add Any Iterable
thislist3 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist3.extend(thistuple)
print(thislist3)
