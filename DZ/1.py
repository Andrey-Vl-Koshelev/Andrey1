class Triangle:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f'Координаты {value} должны быть положительными целыми числами')
        instance.__dict__[self.name] = value


class Point:
    x = Triangle()
    y = Triangle()
    z = Triangle()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def check(self) -> str:
        """Проверяет треугольник на его существование."""
        if self.x + self.y < self.z or self.y + self.z < self.x or self.x + self.z < self.y:
            return f'Треугольника со сторонами {self.x, self.y, self.z} не существует'
        return f'Треугольник со сторонами {self.x, self.y, self.z} существует'


p1 = Point(2, 5, 6)
p2 = Point(5, 2, 8)
p3 = Point(7, 3, 6)
print(p1.check())
print(p2.check())
print(p3.check())

# stdout:
# Треугольник со сторонами (2, 5, 6) существует
# Треугольника со сторонами (5, 2, 8) не существует
# Треугольник со сторонами (7, 3, 6) существует

# TypeError: Координаты -5 должны быть положительными целыми числами
# p1 = Point(2, '5', 6)
# TypeError: Координаты 5 должны быть положительными целыми числами
