def deposit(x: int, y: int) -> tuple[int, int]:
    return x + y, x - y


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_num, diff = deposit(a, b)
print("The sum is:", sum_num, ", the difference is:", diff)
