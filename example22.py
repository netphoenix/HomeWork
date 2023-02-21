text = input("Введите текст: ")
counts = {} # создаем пустой словарь для подсчета вхождений букв

for letter in text:
    if letter in counts:
        counts[letter] += 1 # увеличиваем счетчик для буквы
    else:
        counts[letter] = 1 # создаем новую запись для буквы

print(counts)