def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst

my_list = [1, 2, 3, 4, 5, 6]

print(reverse_list(my_list))


def reverse_list2(lst):
    for i in range(len(lst)):
        lst.insert(i, lst.pop())
    return lst

print(reverse_list(my_list))