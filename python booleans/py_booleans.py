# boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)
print("\n")

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("\n")

# evaluate values and variables
print(bool("Hello")) 
print(bool(15))
print("\n")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print("\n")

# most values are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
print("\n")

# some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print("\n")

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))
print("\n")

# functions can return a boolean
def myFunction():
    return True
print(myFunction())
print("\n")

def myFunction2():
    return False
if myFunction2():
    print("YES!")
else:
    print("NO!")
print("\n")

x = 200
print(isinstance(x, int))