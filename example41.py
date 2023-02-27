# Конструктор класса принимает координаты точек по диагонали (правая нижня левая верхняя или права верхняя и левая нижняя)
# написать метод обънетка perimetr возвращающий периметр получившегося прямоугольника

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.width = abs(x1 - x2)
        self.height = abs(y1 - y2)

    def perimeter(self):
        return 2 * (self.width + self.height)

a = Rectangle(1, 2, 3, 4)
print(a.perimeter())
