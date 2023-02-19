# запрашиваем у пользователя 3 числа
num1 = float(input("Введите число A: "))
num2 = float(input("Введите число B: "))
num3 = float(input("Введите число C: "))

# определяем количество положительных и отрицательных чисел
positive_count = 0
negative_count = 0

if num1 > 0:
    positive_count += 1
else:
    negative_count += 1

if num2 > 0:
    positive_count += 1
else:
    negative_count += 1

if num3 > 0:
    positive_count += 1
else:
    negative_count += 1

print(f"Из введенных чисел {positive_count} положительных и {negative_count} отрицательных.")
