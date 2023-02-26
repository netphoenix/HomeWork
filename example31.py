def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

print(decimal_to_binary(255))

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        if digit == '1':
            decimal += 2 ** power
        power = power + 1
    return decimal

print(binary_to_decimal('1111'))

