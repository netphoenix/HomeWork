# запрашиваем у пользователя 3 числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# определяем количество положительных и отрицательных чисел
positive_count = (num1 > 0) + (num2 > 0) + (num3 > 0)
negative_count = (num1 < 0) + (num2 < 0) + (num3 < 0)




# выводим результат
print(f"Из введенных чисел {positive_count} положительных и {negative_count} отрицательных.")

x = true
y = false
z = false
if not x ot y:
    print(1)
elif not x or not y and z:

