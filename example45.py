class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f"Car__(color={self.color}, count_passenger_seats={self.count_passenger_seats}, " \
               f"is_baby_seat={self.is_baby_seat}, is_busy={self.is_busy})"

class Taxi:
    def __init__(self, cars: list):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> Car:
        for car in self.cars:
            if not car.is_busy and car.count_passenger_seats >= count_passengers + int(is_baby):
                car.is_busy = True
                return car
        return None

class Category:
    categories = []

    @classmethod
    def add(cls, name: str) -> int:
        if name in [category['name'] for category in cls.categories]:
            raise ValueError("Category already exists")
        else:
            cls.categories.append({'name': name, 'is_published': False})
            return len(cls.categories) - 1

    @classmethod
    def get(cls, index: int) -> dict:
        try:
            return cls.categories[index]
        except IndexError:
            raise IndexError("Index out of range")

    @classmethod
    def delete(cls, index: int) -> None:
        if 0 <= index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index: int, name: str) -> None:
        if name in [category['name'] for category in cls.categories if category['name'] != cls.categories[index]['name']]:
            raise ValueError("Category already exists")
        else:
            cls.categories[index]['name'] = name

    @classmethod
    def make_published(cls, index: int) -> None:
        try:
            cls.categories[index]['is_published'] = True
        except IndexError:
            raise IndexError("Index out of range")

    @classmethod
    def make_unpublished(cls, index: int) -> None:
        try:
            cls.categories[index]['is_published'] = False
        except IndexError:
            raise IndexError("Index out of range")


car1 = Car(color='red', count_passenger_seats=4, is_baby_seat=False)
print(car1)
