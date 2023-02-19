input_string = input("Веедите текст: ")
print(input_string)

# заменяем пробелы на дефисы
result1 = input_string.split()
print('-'.join(result1))

result2 = input_string.replace(' ','--')
print(result2)