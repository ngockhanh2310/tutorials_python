arr = list(range(10, 30))
fruits = ['apple', 'banana', 'cherry']
is_true = True
a = 0
for i in arr:
    print(i, end=' ')
print("\n")
while is_true:
    print("Nhập số (1, 2): ", end='')
    a = int(input())
    if a == 1:
        add_str = str(input("Nhập chuỗi cần thêm: "))
        fruits.append(add_str)
        print("Thêm thành công!")
    elif a == 2:
        is_true = False
        print("Thoát chương trình!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
print("\nDanh sách trái cây hiện tại:")
for fruit in fruits:
    print(fruit, end=' ')

print(fruits)
