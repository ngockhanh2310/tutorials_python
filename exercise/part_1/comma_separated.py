values = input("Input some comma-separated numbers: ")

lists = values.split(",")  # tách chuỗi thành list ngăn bằng dấu phẩy

tuples = tuple(lists)  # tạo tuple từ list

# Print the list
print('List : ', lists)

# Print the tuple
print('Tuple : ', tuples)  # tuple là mutable, an toàn dữ liệu hơn list và thường dùng để làm key dictionary


class Student:
    MAX_SCORE = 990

    def __init__(self, student_name, score):  # constructor
        self.student_name = student_name
        self.score = score

    def is_passed(self):
        return self.score >= 450


students = [Student("John", 800), Student("Jane", 900)]
for student in students:
    print(student.student_name, student.score, student.is_passed())
