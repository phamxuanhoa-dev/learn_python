# Python Strings & Escape Characters – Chuỗi và Ký tự thoát trong Python

## 🔤 String Basics – Cơ bản về chuỗi
- Strings are surrounded by single `'` or double `"` quotes  
  → Chuỗi được bao quanh bởi dấu nháy đơn `'` hoặc nháy kép `"`
- `'hello'` is the same as `"hello"`  
  → `'hello'` giống như `"hello"`
- Use `print()` to display strings  
  → Dùng `print()` để hiển thị chuỗi

## 🗣️ Quotes Inside Strings – Dấu nháy bên trong chuỗi
- You can use quotes inside a string  
  → Có thể dùng dấu nháy bên trong chuỗi
  - `print("It's alright")` → Dấu nháy đơn trong dấu nháy kép
  - `print('He is called "Johnny"')` → Dấu nháy kép trong dấu nháy đơn

## 📦 Assigning Strings – Gán chuỗi cho biến
- Use `=` to assign  
  → Dùng dấu `=` để gán chuỗi cho biến  
  - `a = "Hello"`

## 📜 Multiline Strings – Chuỗi nhiều dòng
- Use triple quotes `'''` or `"""`  
  → Dùng ba dấu nháy đơn hoặc ba dấu nháy kép để tạo chuỗi nhiều dòng

## 🔢 Strings are Arrays – Chuỗi là mảng ký tự
- Strings are arrays of Unicode characters  
  → Chuỗi là mảng các ký tự Unicode
- Access characters with indexing  
  → Truy cập ký tự bằng chỉ số  
  - `a[1]` → Ký tự ở vị trí thứ 2

## 🔁 Looping Through Strings – Duyệt chuỗi bằng vòng lặp
- Use `for` loop  
  → Dùng vòng lặp `for` để duyệt từng ký tự  
  - `for x in "banana": print(x)`

## 📏 String Length – Độ dài chuỗi
- Use `len()` function  
  → Dùng hàm `len()` để lấy độ dài chuỗi  
  - `len("Hello")` → Kết quả là 5

## 🔍 Check Substring – Kiểm tra chuỗi con
- Use `in` keyword  
  → Dùng từ khóa `in` để kiểm tra chuỗi con  
  - `"free" in txt`
- Use `not in` to check absence  
  → Dùng `not in` để kiểm tra không tồn tại

## 🧰 String Methods – Các phương thức chuỗi

### 🔠 Case & Formatting – Định dạng và kiểu chữ
- `capitalize()` → Viết hoa chữ cái đầu
- `casefold()` → Chuyển sang chữ thường mạnh mẽ
- `title()` → Viết hoa đầu mỗi từ
- `upper()` / `lower()` → Chuyển sang chữ hoa / thường
- `swapcase()` → Đổi chữ hoa thành thường và ngược lại

### 📐 Alignment – Căn chỉnh chuỗi
- `center(width)` → Căn giữa
- `ljust(width)` / `rjust(width)` → Căn trái / phải

### ✂️ Trimming – Cắt khoảng trắng
- `strip()` → Xóa khoảng trắng đầu/cuối
- `lstrip()` / `rstrip()` → Xóa bên trái / phải

### 🔄 Replace & Split – Thay thế và tách chuỗi
- `replace(old, new)` → Thay thế chuỗi con
- `split(sep)` / `rsplit(sep)` → Tách chuỗi thành danh sách
- `splitlines()` → Tách theo dòng
- `partition(sep)` / `rpartition(sep)` → Tách thành 3 phần

### 🔎 Search – Tìm kiếm
- `find(value)` / `rfind(value)` → Vị trí đầu / cuối của chuỗi con
- `index(value)` / `rindex(value)` → Giống `find` nhưng lỗi nếu không tìm thấy
- `startswith(value)` / `endswith(value)` → Kiểm tra bắt đầu / kết thúc

### ✅ Validation – Kiểm tra nội dung chuỗi
- `isalnum()` → Chỉ gồm chữ và số
- `isalpha()` → Chỉ gồm chữ cái
- `isdigit()` / `isdecimal()` / `isnumeric()` → Chỉ gồm số
- `islower()` / `isupper()` → Kiểm tra kiểu chữ
- `isspace()` → Chỉ gồm khoảng trắng
- `isidentifier()` → Có phải tên biến hợp lệ
- `isprintable()` → Có thể in được

### 🔧 Other – Khác
- `join(iterable)` → Ghép danh sách thành chuỗi
- `encode()` → Mã hóa chuỗi
- `maketrans()` → Tạo bảng dịch ký tự

## 🔐 Escape Characters – Ký tự thoát

### 🔍 What is an Escape Character? – Ký tự thoát là gì?
- An escape character is a backslash `\` followed by a character  
  → Là dấu `\` đi kèm ký tự đặc biệt
- Used to insert characters that are illegal in a string  
  → Dùng để chèn ký tự không thể viết trực tiếp

### 🔠 Common Escape Characters – Các ký tự thoát phổ biến
- `\'` → Single Quote – Dấu nháy đơn
- `\"` → Double Quote – Dấu nháy kép
- `\\` → Backslash – Dấu gạch chéo ngược
- `\n` → New Line – Xuống dòng
- `\r` → Carriage Return – Trả về đầu dòng
- `\t` → Tab – Thụt đầu dòng
- `\b` → Backspace – Xóa lùi
- `\f` → Form Feed – Ngắt trang
- `\ooo` → Octal value – Giá trị bát phân
- `\xhh` → Hex value – Giá trị thập lục phân

### 💡 Example – Ví dụ
- `txt = "We are the so-called \"Vikings\" from the north."`  
  → Dùng `\"` để chèn dấu nháy kép bên trong chuỗi

## 🎯 Applications – Ứng dụng thực tế
- Text processing – Xử lý văn bản
- Data validation – Kiểm tra dữ liệu
- Automation scripts – Tự động hóa
- Web scraping – Trích xuất dữ liệu từ web
- Formatting output – Định dạng đầu ra
- Embedding quotes – Chèn dấu nháy trong chuỗi