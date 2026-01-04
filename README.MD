# 🕹️ Pacman AI Search: State Space Modeling & Pathfinding

Đồ án môn học **Nhập môn Trí tuệ Nhân tạo** - Trường Đại học Tôn Đức Thắng (TDTU). Dự án tập trung vào việc áp dụng thuật toán tìm kiếm không gian trạng thái giúp Pacman ăn hết mồi và đi qua 4 góc bản đồ.

## 📋 Mô hình hóa bài toán
* **Không gian trạng thái**: Vị trí Pacman $(x, y)$ và các điểm mồi còn lại.
* **Hành động**: `North`, `South`, `East`, `West`, `Stop`.
* **Trạng thái đích**: Khi Pacman ăn hết tất cả điểm mồi (đã bao gồm 4 góc).

## 🧠 Thuật toán cài đặt
### 1. Uniform Cost Search (UCS)
* Sử dụng `PriorityQueue` để mở rộng các trạng thái có chi phí $g(n)$ thấp nhất.
* Đảm bảo tìm ra đường đi tối ưu đến điểm mồi tiếp theo.

### 2. A* Search với Manhattan Heuristic
* Sử dụng hàm đánh giá $f(n) = g(n) + h(n)$.
* **Heuristic ($h(n)$)**: Khoảng cách Manhattan từ vị trí hiện tại đến điểm mồi gần nhất.
* **Tính chất**: Hàm $h(n)$ đảm bảo tính **Admissible** (không bao giờ ước lượng cao hơn chi phí thực tế) và **Consistent**.

## 📂 Cấu trúc mã nguồn (OOP)
* `MapGame.py`: Xử lý bản đồ và tự động thêm điểm mồi vào 4 góc.
* `SearchStrategy.py`: Class cơ sở cho các thuật toán và logic trực quan hóa.
* `UCS.py` & `Astar.py`: Cài đặt chi tiết hai thuật toán tìm kiếm.
* `Test.py`: File thực thi chính, nhận input từ Console.

## 🚀 Hướng dẫn chạy
1. Mở Terminal tại thư mục dự án.
2. Chạy lệnh: `python Test.py`
3. Nhập tên file bản đồ trong folder `Sample_input` và chọn thuật toán (`A*` hoặc `UCS`).

---
**Sinh viên thực hiện:** NguyenMinhNhut