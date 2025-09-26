# Strings
print("Hello")
print('Hello')
print("\n")

# Quotes inside quotes
print("It's alright")
print("He is called 'Johnny' ")
print('He is called "Johnny" ' )
print("\n")

# Assign String to a Variable
a = "Hello"
print(a)
print("\n")

# Multiline Strings
# use three double quotes
a = """Lorem ipsum dolor sit am,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n")
# use three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("\n")

# Strings are Arrays
a = "Hello, World!"
print(a[1])
print("\n")

# Looping through a String
for x in "banana":
    print(x)
print("\n")

# String Length
a = "Hello, World!"
print(len(a))
print("\n")

# Check String
txt = "The best things in life are free!"
print("free" in txt)
print("\n")
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
print("\n")    

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
print("\n")
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, expensive is NOT present.")