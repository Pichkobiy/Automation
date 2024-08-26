def square(a):
    area = a ** 2
    return area

a = float(input("Сторона квадрата: "))
result = square(a)
import math
rounded_result = math.ceil(result)
print(f'Округленная сумма - {rounded_result}')