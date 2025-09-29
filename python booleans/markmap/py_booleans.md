# Python Booleans – Kiểu dữ liệu logic trong Python

## 🔍 What is a Boolean? – Boolean là gì?
- A Boolean represents one of two values: `True` or `False`  
  → Boolean biểu diễn một trong hai giá trị: `True` hoặc `False`
- Used for logical operations and control flow  
  → Dùng trong các phép toán logic và điều khiển luồng chương trình

## 🧪 Boolean Values – Giá trị Boolean
- `True` – Đúng
- `False` – Sai
- Type: `bool`  
  → Kiểu dữ liệu: `bool`

## 📦 Boolean Expressions – Biểu thức logic
- Comparison operators return Boolean values  
  → Các toán tử so sánh trả về giá trị Boolean
  - `==`, `!=`, `>`, `<`, `>=`, `<=`
- Example: `5 > 3` → `True`

## 🔁 Conditional Statements – Câu lệnh điều kiện
- Used in `if`, `elif`, `else` blocks  
  → Dùng trong các khối điều kiện `if`, `elif`, `else`
  - `if x > 0: print("Positive")`

## 🔄 Logical Operators – Toán tử logic
- `and` → Và (cả hai điều kiện đều đúng)
- `or` → Hoặc (một trong hai điều kiện đúng)
- `not` → Phủ định (đảo ngược giá trị Boolean)

## 🔍 Boolean Evaluation – Đánh giá Boolean
- Python treats some values as `False`:
  - `None`, `False`, `0`, `""`, `[]`, `{}`, `set()`
  → Một số giá trị được xem là `False` khi kiểm tra điều kiện
- All other values are treated as `True`  
  → Các giá trị còn lại được xem là `True`

## 🧰 Built-in Functions – Hàm tích hợp
- `bool()` → Convert value to Boolean  
  → Chuyển đổi giá trị sang kiểu Boolean
  - `bool(0)` → `False`
  - `bool("Hello")` → `True`

## 🧠 Use Cases – Ứng dụng thực tế
- Decision making – Ra quyết định
- Loop control – Điều khiển vòng lặp
- Data validation – Kiểm tra dữ liệu
- Flag variables – Biến cờ (đánh dấu trạng thái)