add = lambda x: x * x  # biểu thức lambda
language = list(("Python", "Java", "C#", "JavaScript"))
num = list((1, 2, 3, 4, 5, 6, 7, 8, 9))

print(list(map(add, num)))
print(list(filter(lambda x: x % 2 == 0, num)))
