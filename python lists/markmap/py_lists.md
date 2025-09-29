# Python Lists – Danh sách trong Python

## Access Items – Truy cập phần tử
- `list[0]` → First item – Phần tử đầu tiên
- `list[-1]` → Last item – Phần tử cuối cùng
- `list[2:5]` → Slice – Cắt chuỗi con
- `list[:3]`, `list[::2]` → Cắt và lấy cách phần tử

## Change Item Value – Thay đổi giá trị phần tử
- `list[1] = "new"` → Gán lại giá trị
- `list[1:3] = ["a", "b"]` → Gán nhiều phần tử

## Loop Through a List – Duyệt qua danh sách
- `for item in list:` → Duyệt từng phần tử
- `for i in range(len(list)):` → Duyệt theo chỉ số

## Check if Item Exists – Kiểm tra phần tử có tồn tại
- `"apple" in list` → Trả về `True` nếu tồn tại

## List Length – Độ dài danh sách
- `len(list)` → Trả về số phần tử

## Add List Items – Thêm phần tử vào danh sách
- `append(x)` → Thêm vào cuối
- `insert(i, x)` → Chèn tại vị trí i

## Remove List Items – Xóa phần tử khỏi danh sách
- `remove(x)` → Xóa phần tử đầu tiên có giá trị x
- `pop()` / `pop(i)` → Xóa và trả về phần tử cuối / tại vị trí i
- `del list[i]` → Xóa phần tử tại vị trí i
- `clear()` → Xóa toàn bộ danh sách

## Copy a List – Sao chép danh sách
- `copy()` → Tạo bản sao nông
- `list2 = list1[:]` → Sao chép bằng slicing

## Join Lists – Nối danh sách
- `list1 + list2` → Ghép danh sách
- `list1.extend(list2)` → Nối danh sách

## List Methods – Các phương thức danh sách
- `append()` → Thêm phần tử
- `clear()` → Xóa toàn bộ
- `copy()` → Sao chép
- `count(x)` → Đếm số lần xuất hiện
- `extend(list2)` → Nối danh sách
- `index(x)` → Vị trí phần tử
- `insert(i, x)` → Chèn phần tử
- `pop()` → Xóa và trả về phần tử
- `remove(x)` → Xóa phần tử
- `reverse()` → Đảo ngược thứ tự
- `sort()` → Sắp xếp tăng dần

## Sort Lists – Sắp xếp danh sách
- `list.sort()` → Sắp xếp tại chỗ
- `sorted(list)` → Trả về danh sách đã sắp xếp
- `list.sort(reverse=True)` → Sắp xếp giảm dần
- `list.sort(key=str.lower)` → Sắp xếp theo hàm

## List Comprehension – Diễn đạt danh sách
- `[x for x in list]` → Tạo danh sách từ vòng lặp
- `[x for x in list if x != "apple"]` → Có điều kiện
- `[x if x != "apple" else "orange" for x in list]` → Có nhánh điều kiện

## Nested Lists – Danh sách lồng nhau
- `matrix = [[1, 2], [3, 4]]` → Danh sách 2 chiều
- `matrix[0][1]` → Truy cập phần tử lồng

## List Exercises – Bài tập luyện tập
- Tạo danh sách, thêm/xóa phần tử
- Sắp xếp và lọc dữ liệu
- Duyệt và xử lý danh sách lồng nhau