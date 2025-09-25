# Python Strings

## 🧠 Khái niệm
- Chuỗi ký tự (`str`)
- Immutable (không thể thay đổi)
- Unicode hỗ trợ đa ngôn ngữ

## 🛠️ Khởi tạo chuỗi
- Dấu nháy đơn `'Hello'`
- Dấu nháy kép `"Hello"`
- Chuỗi nhiều dòng: `'''Hello'''` hoặc `"""Hello"""`

## ✂️ Các thao tác cơ bản
- Nối chuỗi: `"Hello" + "World"` → `"HelloWorld"`
- Nhân chuỗi: `"Hi" * 3` → `"HiHiHi"`
- Truy cập ký tự: `s[0]`, `s[-1]`
- Cắt chuỗi:
  - `s[1:4]`: từ vị trí 1 đến 3
  - `s[:3]`: từ đầu đến vị trí 2
  - `s[::2]`: lấy cách 2 ký tự

## 🧰 Hàm và phương thức thông dụng
- `len(s)` – độ dài chuỗi
- `s.upper()` / `s.lower()` – viết hoa / viết thường
- `s.strip()` / `s.lstrip()` / `s.rstrip()` – xóa khoảng trắng
- `s.replace("a", "b")` – thay thế ký tự
- `s.find("x")` / `s.index("x")` – tìm vị trí ký tự
- `s.startswith("Hi")` / `s.endswith("Bye")` – kiểm tra bắt đầu/kết thúc
- `s.split(",")` – tách chuỗi thành danh sách
- `",".join(list)` – ghép danh sách thành chuỗi

## 🧾 Định dạng chuỗi
- f-string: `f"Hello {name}"`
- `format()`: `"Hello {}".format(name)`
- `%` formatting: `"Hello %s" % name`

## 🔍 Kiểm tra chuỗi
- `s.isalpha()` – chỉ chứa chữ cái
- `s.isdigit()` – chỉ chứa số
- `s.isalnum()` – chữ + số
- `s.isspace()` – chỉ khoảng trắng
- `s.islower()` / `s.isupper()` – kiểm tra viết thường / viết hoa

## 🔄 Chuyển đổi kiểu dữ liệu
- `str(123)` → `"123"` – số thành chuỗi
- `int("123")` → `123` – chuỗi thành số nguyên
- `float("3.14")` → `3.14` – chuỗi thành số thực

## 🧪 Kỹ thuật nâng cao
- Regular Expressions (`re` module)
- Encoding/Decoding: `s.encode()` / `b.decode()`
- Raw strings: `r"\n"` giữ nguyên ký tự đặc biệt

## 🎯 Ứng dụng thực tế
- Xử lý văn bản
- Phân tích dữ liệu
- Tự động hóa file văn bản
- Web scraping