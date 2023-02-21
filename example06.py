# if (a := int(input()))

while not (a := input('Введите цифру: ')).isdigit():
        print('test')
print(a)
