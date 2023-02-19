# запрашиваем у пользователя 3 поля
var_name = input("Введите Имя: ")
var_age = input("Введите Возраст: ")
var_city = input("Введите Город: ")

print(f"Добрый день {var_name}! Ваш возраст {var_age} из города {var_city}.")

print("Добрый день "+var_name + "! Ваш возраст " + var_age + " из города " + var_city + ".")

print("Добрый день {var_name}! Ваш возраст {var_age} из города {var_city}.".format(var_name=var_name, var_age=var_age, var_city=var_city))

message = "Привет, %s! Тебе уже %s лет и ты живешь в городе %s." % (var_name, var_age, var_city)
print(message)

message = "Привет 2, {}! Тебе уже {} лет и ты живешь в городе {}.".format(var_name, var_age, var_city)
print(message)