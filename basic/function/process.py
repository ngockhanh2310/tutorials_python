def calculate(x, y):
    return x + y, x - y, x * y, x / y if y != 0 else None


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a, b, c, d = calculate(num1, num2)
print(f"Sum: {a}, Difference: {b}, Product: {c}, Quotient: {d}")


def loc_so(danh_sach_goc):
    ket_qua = []
    for so in danh_sach_goc:
        if so % 2 == 0:
            ket_qua.append(so)
    return ket_qua, [so for so in danh_sach_goc if so % 2 != 0]


ds = [1, 2, 3, 4, 5, 6]
so_chan, so_le = loc_so(ds)
print(so_chan)
print(so_le[::-1])
