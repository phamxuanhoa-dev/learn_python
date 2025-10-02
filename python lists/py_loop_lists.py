# loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print("\n")
    
#loop through the index numbers
thislist1 = ["apple", "banana", "cherry"]
for i in range(len(thislist1)):
    print(thislist1[i]) 

# using a while loop
i = 0
while i < len(thislist1):
    print(thislist1[i])
    i = i + 1
print("\n")

# looping using list comprehension
thislist2 = ["apple", "banana", "cherry"]
[print(x) for x in thislist2]