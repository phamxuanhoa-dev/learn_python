# remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("\n")

# remove specified index
thislist1 = ["apple", "banana", "cherry"]
thislist1.pop(1) # if index is not specified, removes the last item
print(thislist1)
print("\n")
# The del keyword also removes the specified index
thislist2 = ["apple", "banana", "cherry"]
del thislist2[0]
print(thislist2)
print("\n")

# clear the list
thislist3 = ["apple", "banana", "cherry"]   
thislist3.clear()
print(thislist3)    
print("\n")

