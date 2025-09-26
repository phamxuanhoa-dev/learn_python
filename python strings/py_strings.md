# Python Strings – Chuỗi trong Python

## 🧠 Concept – Khái niệm
- String is a sequence of characters – Chuỗi là một dãy ký tự
- Immutable – Không thể thay đổi sau khi tạo
- Supports Unicode – Hỗ trợ mã hóa Unicode

## 🛠️ Initialization – Khởi tạo chuỗi
- Single quotes `'Hello'` – Dấu nháy đơn
- Double quotes `"Hello"` – Dấu nháy kép
- Multiline strings `'''Hello'''` – Chuỗi nhiều dòng

## ✂️ Basic Operations – Các thao tác cơ bản
- Concatenation `"Hello" + "World"` – Nối chuỗi
- Repetition `"Hi" * 3` – Nhân chuỗi
- Indexing `s[0]`, `s[-1]` – Truy cập ký tự
- Slicing `s[1:4]`, `s[:3]` – Cắt chuỗi

## 🧰 Common Methods – Các phương thức thông dụng
- `len(s)` – Length of string – Độ dài chuỗi
- `s.upper()` / `s.lower()` – Viết hoa / viết thường
- `s.strip()` – Remove whitespace – Xóa khoảng trắng
- `s.replace("a", "b")` – Thay thế ký tự
- `s.find("x")` – Tìm vị trí ký tự
- `s.split(",")` – Tách chuỗi
- `",".join(list)` – Ghép danh sách thành chuỗi

## 🧾 String Formatting – Định dạng chuỗi
- f-string: `f"Hello {name}"` – Cách hiện đại
- `format()`: `"Hello {}".format(name)` – Cách linh hoạt
- `%` formatting: `"Hello %s" % name` – Cách cũ

## 🔍 String Checks – Kiểm tra chuỗi
- `s.isalpha()` – Only letters – Chỉ chứa chữ cái
- `s.isdigit()` – Only digits – Chỉ chứa số
- `s.isalnum()` – Letters and digits – Chữ và số

## 🔄 Type Conversion – Chuyển đổi kiểu
- `str(123)` → `"123"` – Số thành chuỗi
- `int("123")` → `123` – Chuỗi thành số nguyên
- `float("3.14")` → `3.14` – Chuỗi thành số thực

## 🧪 Advanced – Kỹ thuật nâng cao
- Regular Expressions – Biểu thức chính quy
- Encoding/Decoding – Mã hóa / Giải mã
- Raw strings `r"\n"` – Giữ nguyên ký tự đặc biệt

## 🎯 Applications – Ứng dụng thực tế
- Text processing – Xử lý văn bản
- Data analysis – Phân tích dữ liệu
- Automation – Tự động hóa
- Web scraping – Trích xuất dữ liệu từ web