file_name = input("Enter file name:")

f_ex = file_name.split(".")  # tách thành mảng ngăn nhau bằng dấu .
f_extension = file_name.split(".")[-1]  # lấy phần tử cuối cùng
f_first = file_name.split(".")[0]  # lấy phần tử đầu tiên
f_name_only = ".".join(
    file_name.split(".")[:-1])  # lấy tất cả phần tử đầu tiên trừ phần tử cuối cùng rồi nối lại bằng dấu .
print(f_ex, '\n', f_first, '\n', f_extension, '\n', f_name_only)
f_test = '.'.join(p for p in f_ex if p != 'com')
print('', f_test)
