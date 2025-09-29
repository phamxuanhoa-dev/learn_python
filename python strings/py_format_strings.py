# String Format
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)
# print("\n")

age = 36
txt = f"My name is John, I am {age}"
print(txt)
print("\n")

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
print("\n")

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print("\n")

txt = f"The price is {20 * 59} dollars"
print(txt)