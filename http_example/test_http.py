import requests  # Import thư viện vừa cài

print("Đang tải dữ liệu từ server...")

# 1. Gửi yêu cầu đến một API mẫu (trả về dữ liệu người dùng giả lập)
response = requests.get("https://jsonplaceholder.typicode.com/users")

# 2. Kiểm tra xem việc lấy dữ liệu có thành công không (Mã 200 là OK)
if response.status_code == 200:
    # Chuyển đổi dữ liệu từ dạng text sang List/Dictionary của Python
    data = response.json()

    print(f"Đã tìm thấy {len(data)} người dùng:\n")

    # Duyệt qua dữ liệu (bạn đã rành cái này rồi)
    for user in data:
        # Lấy tên và email
        ten = user["name"]
        email = user["email"]
        city = user["address"]["city"]

        print(f"- {ten} ({email}) - Sống tại: {city}")
else:
    print("Lỗi kết nối!")
