import matplotlib.pyplot as plt  # Import và đặt tên tắt là plt cho gọn

# 1. Chuẩn bị dữ liệu
sinh_vien = ["Nam", "Lan", "Hung", "Khanh", "Tuan"]
diem_so = [7.5, 9.0, 8.2, 9.5, 6.5]

# 2. Thiết lập biểu đồ
plt.figure(figsize=(10, 5))  # Tạo khung hình kích thước 10x5

# Vẽ biểu đồ cột (Bar chart)
# Cú pháp: plt.bar(trục_ngang, trục_dọc, màu_sắc...)
plt.bar(sinh_vien, diem_so, color='pink', width=0.5)

# 3. Trang trí thêm thông tin
plt.title("Biểu đồ điểm số Lớp Học Python", fontsize=16, color='blue')
plt.xlabel("Tên sinh viên")
plt.ylabel("Điểm số")

# Thêm lưới mờ cho dễ nhìn
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Hiển thị
print("Đang hiển thị biểu đồ...")
plt.show()
