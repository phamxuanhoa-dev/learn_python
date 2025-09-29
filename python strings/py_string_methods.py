# String Methods

# Chuyển đổi chữ cái
# capitalize(): Converts the first character to upper case(Viết hoa ký tự đầu tiên)
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
print("\n")
# casefold(): Converts string into lower case(Chuyển đổi chuỗi thành chữ thường)
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
print("\n")
# lower(): Converts a string into lower case(Chuyển đổi chuỗi thành chữ thường)
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
print("\n")
# upper(): Converts a string into upper case(Chuyển đổi chuỗi thành chữ hoa)
txt = "Hello my friends"
x = txt.upper()
print(x)
print("\n")
# swapcase(): Swaps cases, lower case becomes upper case and vice versa(Đảo ngược chữ hoa thành chữ thường và ngược lại)
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
print("\n")
# title(): Converts the first character of each word to upper case(Chuyển đổi ký tự đầu tiên của mỗi từ thành chữ hoa)
txt = "Welcome to my world"
x = txt.title()
print(x)
print("\n")

# Căn chỉnh và định dạng
# center(): Returns a centered string(căn giữa)
txt = "banana"
x = txt.center(20)
print(x)
print("\n")
# ljust(): Returns a left justified version of the string(căn trái của chuỗi)
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
print("\n")
# rjust(): Returns a right justified version of the string(căn phải của chuỗi)
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print("\n")
# zfill(): Fills the string with a specified number of 0 values at the beginning(Điền chuỗi với một số giá trị 0 nhất định ở đầu)
txt = "50"
x = txt.zfill(10)
print(x)
print("\n")
# format(): Formats specified values in a string(Định dạng các giá trị được chỉ định trong một chuỗi)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
print("\n")
# format_map(): Formats specified values from a dictionary in a string(Định dạng các giá trị được chỉ định từ một từ điển trong một chuỗi)
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
print("\n")

# Tìm kiếm và kiểm tra
# find(): Searches the string for a specified value and returns the position of where it was found(Tìm kiếm chuỗi một giá trị được chỉ định và trả về vị trí của nơi nó được tìm thấy)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
print("\n")
# rfind(): Searches the string for a specified value and returns the last position of where it was found(Tìm kiếm chuỗi một giá trị được chỉ định và trả về vị trí cuối cùng của nơi nó được tìm thấy)
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
print("\n")
# index(): Searches the string for a specified value and returns the position of where it was found(Tìm kiếm chuỗi một giá trị được chỉ định và trả về vị trí của nơi nó được tìm thấy)
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
print("\n")
# rindex(): Searches the string for a specified value and returns the last position of where it was found(Tìm kiếm chuỗi một giá trị được chỉ định và trả về vị trí cuối cùng của nơi nó được tìm thấy)
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
print("\n")
# count(): Returns the number of times a specified value occurs in a string(Trả về số lần một giá trị được chỉ định xuất hiện trong một chuỗi)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
print("\n")
# startswith(): Returns true if the string starts with the specified value(Trả về true nếu chuỗi bắt đầu bằng giá trị được chỉ định)
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
print("\n")
# endswith(): Returns true if the string ends with the specified value(Trả về true nếu chuỗi kết thúc bằng giá trị được chỉ định)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
print("\n")

# Kiểm tra nội dung chuỗi
# isalnum(): Returns True if all characters in the string are alphanumeric(Trả về True nếu tất cả các ký tự trong chuỗi đều là chữ và số)
txt = "Company12"
x = txt.isalnum()
print(x)
print("\n")
# isalpha(): Returns True if all characters in the string are in the alphabet(Trả về True nếu tất cả các ký tự trong chuỗi đều thuộc bảng chữ cái)
txt = "CompanyX"
x = txt.isalpha()
print(x)
print("\n")
# isascii(): Returns True if all characters in the string are ascii characters(Trả về True nếu tất cả các ký tự trong chuỗi đều là ký tự ascii)
txt = "Company123"
x = txt.isascii()
print(x)
print("\n")
# isdecimal(): Returns True if all characters in the string are decimals(Trả về True nếu tất cả các ký tự trong chuỗi đều là số thập phân)
txt = "1234"
x = txt.isdecimal()
print(x)
print("\n")
# isdigit(): Returns True if all characters in the string are digits(Trả về True nếu tất cả các ký tự trong chuỗi đều là chữ số)
txt = "50800"
x = txt.isdigit()
print(x)
print("\n")
# isidentifier(): Returns True if the string is an identifier(Trả về True nếu chuỗi là một định danh)
txt = "Demo"
x = txt.isidentifier()
print(x)
print("\n")
# islower(): Returns True if all characters in the string are lower case(Trả về True nếu tất cả các ký tự trong chuỗi đều là chữ thường)
txt = "hello world!"
x = txt.islower()
print(x)
print("\n")
# isnumeric(): Returns True if all characters in the string are numeric(Trả về True nếu tất cả các ký tự trong chuỗi đều là số)
txt = "565543"
x = txt.isnumeric()
print(x)
print("\n")
# isprintable(): Returns True if all characters in the string are printable(Trả về True nếu tất cả các ký tự trong chuỗi đều có thể in được)
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
print("\n")
# isspace(): Returns True if all characters in the string are whitespaces(Trả về True nếu tất cả các ký tự trong chuỗi đều là khoảng trắng)
txt = "   "
x = txt.isspace()
print(x)
print("\n")
# istitle(): Returns True if the string follows the rules of a title(Trả về True nếu chuỗi tuân theo các quy tắc của một tiêu đề)
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
print("\n")
# isupper(): Returns True if all characters in the string are upper case(Trả về True nếu tất cả các ký tự trong chuỗi đều là chữ hoa)
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
print("\n")

# Cắt, tách, thay thế
# split(): Splits the string at the specified separator, and returns a list(Tách chuỗi tại dấu phân cách được chỉ định và trả về một danh sách)
txt = "welcome to the jungle"
x = txt.split()
print(x)
print("\n")
# rsplit(): Splits the string at the specified separator, and returns a list(Tách chuỗi tại dấu phân cách được chỉ định và trả về một danh sách)
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
print("\n")
# splitlines(): Splits the string at line breaks and returns a list(Tách chuỗi tại các ngắt dòng và trả về một danh sách)
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print("\n")
# replace(): Returns a string where a specified value is replaced with a specified value(Trả về một chuỗi trong đó một giá trị được chỉ định được thay thế bằng một giá trị được chỉ định)
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
print("\n")
# partition(): Returns a tuple where the string is parted into three parts(Trả về một bộ ba trong đó chuỗi được chia thành ba phần)
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print("\n")
# rpartition(): Returns a tuple where the string is parted into three parts(Trả về một bộ ba trong đó chuỗi được chia thành ba phần)
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print("\n")

# Kết hợp và mã hóa
# join(): Converts the elements of an iterable into a string(Chuyển đổi các phần tử của một iterable thành một chuỗi)
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print("\n")
# encode(): Returns an encoded version of the string(Trả về phiên bản được mã hóa của chuỗi)
txt = "My name is Stale"
x = txt.encode()
print(x)
print("\n")
# expandtabs(): Sets the tab size of the string(Đặt kích thước tab của chuỗi)
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print("\n")
# maketrans(): Returns a translation table to be used in translations(Trả về một bảng dịch để sử dụng trong các bản dịch)
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
print("\n")
# translate(): Returns a translated string(Trả về một chuỗi đã dịch)
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))