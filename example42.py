# Реализовать класс category
# Создать атрибут класса categories (list)
# Написать метод класса dd принимающий на вход название категории, если такой категории в атрибуте класса нет, добавить
# данную категорию в список и вернуть индекс вхождения новой категории в списке. Если такая категория уже есть вызвать
# исключение ValueError
# Написать метод класса get принимающий индекс и возвращающий

class Category:

    categories = []
    @classmethod
    def add(cls, value):
        if value in cls.categories:
            raise ValueError("Категория уже существует")
        cls.categories.append(value)
        return cls.categories.index(value)

    @classmethod
    def get(cls, indx):
        return cls.categories[indx]

    @classmethod
    def del(cls, indx):
        try:
            del cls.categories[indx]
        except IndexError:
            pass
    @classmethod
    def update(cls, i, value):
        if i in range(len(cls.categories))
            cls.categories[i] = value.title()
        else:
            raise ValueError("Категория уже существует")


a = Category()
print(a.add('test2'))
print(a.add('test3'))
print(a.add('test4'))
print(a.get(2))