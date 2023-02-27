def filter_strings(lst):
    # Используем метод filter() и функцию isinstance() для отбора строк
    lst[:] = filter(lambda x: isinstance(x, str), lst)

lst = [1, 2, "hello", True, "world", 3.14]
filter_strings(lst)
print(lst) # ["hello", "world"]
