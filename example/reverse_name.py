name = str(input("Enter your name: "))
print("Reversed name:", name[::-1])

# viết hoa toàn bộ tên
print("Uppercase name:")
print(str.upper(name))  # or name.upper()

# viết hoa chữ cái đầu mỗi từ
print("Capitalize each word:")
str_cap = name.strip()  # strip() → xóa khoảng trắng đầu & cuối
result = str_cap.title()  # title() → viết hoa chữ cái đầu mỗi từ
print(result)

# viết hoa từ đầu tiên
print("Capitalize first letter:")
print(name.capitalize())

# viết hoa chữ cái mỗi từ ( cách thủ công )
str_name = name.strip().split()  # tách tên thành nhiều mảng ngăn cách nhau bằng khoảng trắng
capitalized_name = []
for word in str_name:
    capitalized_name.append(word[0].upper() + word[1:].lower())
words = " ".join(capitalized_name)  # nối mảng thành chuỗi cách nhau bằng dấu cách
print(words)

# cách 2
cap_name = ""
for word in str_name:
    cap_name += word[0].upper() + word[1:].lower() + " "
print(cap_name.strip())  # strip() → xóa khoảng trắng thừa ở cuối
