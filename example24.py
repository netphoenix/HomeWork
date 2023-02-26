from string import printable

# протокол SMS способен передавать 140 байт информации
# символы входящие в ASCII занимают по 1 байту, русские буквы по 2 байта
# на входд функции поступает еткст необходимо сказать на сколько сообщение необходимо разбить
# текст чтобы его отправить по протколу SMS


def sms_counter(text):
    ascii_chars = len([c for c in text if ord(c) < 128]) # считаем количество символов ASCII
    cyrillic_chars = len(text) - ascii_chars # считаем количество символов кириллицы
    message_size = ascii_chars + cyrillic_chars * 2 # определяем размер сообщения в байтах
    num_messages = (message_size - 1) // 140 + 1 # вычисляем количество сообщений, округляя вверх
    return num_messages

text = input("Введите текст: ")

a = sms_counter(text)
print(a)

def sms_counter2(text):
    bytes_count = 0
    for el in text:
        if el in printable:
            bytes_count += 1
        else:
            bytes_count += 2
    sms_count = bytes_count / 140
    return int(sms_count)

a = sms_counter2(text)
print(a)