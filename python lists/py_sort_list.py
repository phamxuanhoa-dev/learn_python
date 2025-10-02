# Sort List Alphanumerically
thislist = ["banana", "mango", "kiwi", "orange"]
thislist.sort()
print(thislist)
print("\n")

# Sort descending
thislist.sort(reverse=True)
print(thislist)
print("\n")

# custom sort function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
print("\n")

# reverse order
thislist.reverse()
print(thislist)