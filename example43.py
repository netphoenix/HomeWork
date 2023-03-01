# написать класс RegisterForm
# конструктор класса принимает аргументы username, password и объявляет атрибуты объекта на их основе
# написать метод объекта is_valid проверяющий атрибуты на критерии
# 1. username - строка, password - строка
# 2. длина username >= 2
# 3. длина password >= 8
# 4. password не должен содержать в себе username
# 5. password должен содержать хотя бы 1 большую букву и 1 цифру
# Если один из пунктов нарушается, метод должен возвращать  False, и True в противном случае

class RegisterForm:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def print_reg_value(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        #return self.username + self.password
    def is_valid(self):
        # Проверяем, что username и password - строки
        if not isinstance(self.username, str) or not isinstance(self.password, str):
            raise TypeError
            return False

        # Проверяем, что длина username >= 2
        if len(self.username) < 2:
            return False

        # Проверяем, что длина password >= 8
        if len(self.password) < 8:
            return False

        # Проверяем, что password содержит хотя бы 1 большую букву и 1 цифру
        has_upper = False
        has_digit = False
        for char in self.password:
            if char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True

        if not has_upper or not has_digit:
            return False

        return True


form = RegisterForm("username_name", "111")
print(form.print_reg_value())

if form.is_valid():
    print("Атрибуты объекта соответствуют критериям")
else:
    print("Атрибуты объекта не соответствуют критериям")