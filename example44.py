# Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average - возвращающий среднее арифимитическое между всеми числами
#

class Numbers:

    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def print_value(self):
        print(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def max_count(self):
        from collections import Counter
        counter = Counter(self.numbers)
        max_common = counter.most_common(1)[0][1]
        numbers = [*filter(lambda x: self.numbers.count(x) == max_common, self.numbers)]
        return sum(numbers) / len(numbers)
        
num = Numbers([1, 2, 3])
num.print_value()

print(num.average())
