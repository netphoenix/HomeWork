from io import DEFAULT_BUFFER_SIZE
print(DEFAULT_BUFFER_SIZE)
file = open('readme.md', 'r', encoding='utf-8', buffering=-1)

#print(file.read())
#print(file.readline())
#print(file.readlines())
#lines = [line.strip() for line in file if line.strip()]
#         print(lines)

print(file.tell())
print(file.seek(0))

file.close()


with open('readme.md', 'r', encoding='utf-8', buffering=-1) as file:
    print(file.readlines())


with (
    open('readme.md', 'r', encoding='utf-8', buffering=-1) as file,
    open('test01.py', 'w', encoding='utf-8', buffering=-1) as file:
