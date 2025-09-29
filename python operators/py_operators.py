#Toán tử số học (Arithmetic Operators)
a = 10
b = 3
print("a + b =", a + b)       # Cộng
print("a - b =", a - b)       # Trừ
print("a * b =", a * b)       # Nhân
print("a / b =", a / b)       # Chia
print("a % b =", a % b)       # Chia lấy dư
print("a ** b =", a ** b)     # Lũy thừa
print("a // b =", a // b)     # Chia lấy phần nguyên

#Toán tử so sánh (Comparison Operators)
print("a == b:", a == b)     # So sánh bằng
print("a != b:", a != b)     # Khác nhau
print("a > b:", a > b)       # Lớn hơn
print("a < b:", a < b)       # Nhỏ hơn
print("a >= b:", a >= b)     # Lớn hơn hoặc bằng
print("a <= b:", a <= b)     # Nhỏ hơn hoặc bằng

#Toán tử logic (Logical Operators)
x = True
y = False
print("x and y:", x and y)   # Và
print("x or y:", x or y)     # Hoặc
print("not x:", not x)       # Phủ định

#Toán tử gán (Assignment Operators)
c = 5
c += 2  # c = c + 2
print("c sau += 2:", c)
c *= 3  # c = c * 3
print("c sau *= 3:", c)

#Toán tử định danh (Identity Operators)
m = [1, 2, 3]
n = m
print("m is n:", m is n)         # Cùng tham chiếu
print("m is not n:", m is not n) # Khác tham chiếu

#Toán tử kiểm tra thành phần (Membership Operators)
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", "banana" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

#Toán tử nhị phân (Bitwise Operators)
x = 5  # 0101
y = 3  # 0011
print("x & y:", x & y)     # AND
print("x | y:", x | y)     # OR
print("x ^ y:", x ^ y)     # XOR
print("~x:", ~x)           # NOT
print("x << 1:", x << 1)   # Dịch trái
print("x >> 1:", x >> 1)   # Dịch phải