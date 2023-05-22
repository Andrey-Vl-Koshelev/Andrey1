# import main
# import re
#
# from car import electrocar
import random


# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()

# from math import pi
#
#
# class Rectangle:
#     def __init__(self, l, h):
#         self.l = l
#         self.h = h
#
#     def get_rect_perimetr(self):
#         res = self.l * 2 + self.h * 2
#         print(f"Периметр прямоугольника: {res}")
#         return res
#
#     def get_rect_area(self):
#         res = self.l * self.h
#         print(f"Площадь прямоугольника: {res}")
#         return res
#
#     def print_rect(self):
#         print(f"Стороны прямоугольника: {self.l}, {self.h}")
#         return {self.l, self.h}
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_circumference(self):
#         res = 2 * pi * self.r
#         print(f"Длина окружности: {round(res, 2)}")
#         return res
#
#     def get_circle_area(self):
#         res = round(pi * self.r ** 2, 2)
#         print(f"Площадь круга: {res}")
#         return res
#
#     def print_circle(self):
#         print(f"Радиус круга: {self.r}")
#         return self.r
#
#
# class Cylinder(Rectangle, Circle):
#     def __init__(self, r, h):
#         Circle.__init__(self, r)
#         Rectangle.__init__(self, self.get_circle_circumference(), h)
#
#     def get_volume(self):
#         res = self.get_circle_area() * self.h
#         print(f"Объем: {res}")
#         return res
#
#     def print_cylinder(self):
#         print(f"Радиус основания: {self.r}, высота: {self.h}")
#
#
# circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]
# rects = [Rectangle(3, 7), Rectangle(2, 7), Rectangle(19, 12)]
# cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]
#
# circle_max_s = max(circles, key=lambda c: c.get_circle_area())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimetr())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinder_v_avr = sum(cylinders_v) / len(cylinders_v)
# print(f"Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}")
# print(f'Прямоугольник с наименьшим периметром: {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
# print(f"Средний объем цилиндров: {round(cylinder_v_avr, 2)}")

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота: ', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут:', self.name)
#
# droid1 = Robot('R2_D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
# print('\nЗдесь роботы делают работу\n')
# print('Роботы закончили работу')
# del droid1
# del droid2
# print('Численность роботов:', Robot.k)


# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = 'Некоректные данные'
#         self.__year = self.__power = self.__price = 0
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_str(model):
#             self.__model =model
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print('Данные должны быть числом')
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print('Данные должны быть строкой')
#             return False
#         return True
#
#     def set_name(self, name):
#         if Car.__check_value_str(name):
#             self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
#     def print_info(self):
#         print('Данные автомобиля'.center(40,'*'))
#         print(f"""Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производитель: {self.__model}
# Мощность двигателя: {self.__power}
# Цвет машины: {self.__color}
# Цена: {self.__price}
# """)
#         print('='*40)
#
#
#
# c1 = Car('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
# c1.print_info()
# c1.set_name('X2')
# print(c1.get_name())
# c1.print_info()


# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, m):
#         self.__age = m
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
#
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# p1.age = 20
# print(p1.age)
# del p1.age
# print(p1.__dict__)


# class Numbers:
#
#     @staticmethod
#     def min_nums(a, b, d, c):
#         min_num = min(a, b, d, c)
#         return min_num
#
#     @staticmethod
#     def max_nums(a, b, d, c):
#         max_num = max(a, b, d, c)
#         return max_num
#
#     @staticmethod
#     def sr_arif(a, b, d, c):
#         arif = (a + b + d + c) / 4
#         return arif
#
#     @staticmethod
#     def factor(a):
#         n = 1
#         for i in range(1, (a + 1)):
#             n = n * i
#         return n
#
#
#
# print('Минимальное число:', Numbers.min_nums(4, 5, 9, 2))
# print('Максимальное число:', Numbers.max_nums(4, 5, 9, 2))
# print('Среднее арифметическое:', Numbers.sr_arif(4, 5, 9, 2))
# print('Факториал числа:', Numbers.factor(9))


# class Weight:
#
#     def __init__(self, k=0):
#         self.__k = k
#
#     @property
#     def kg_k(self):
#         return self.__k
#
#     @kg_k.setter
#     def kg_k(self, k):
#         if isinstance(k, int | float):
#             self.__k = k
#         else:
#             print('Килограммы задаются числами')
#
#     def to_pounds(self):
#         return round(self.__k * 2.205, 2)
#
# w1 = Weight(12)
# print(w1.kg_k, 'кг =>', end='')
# print(w1.to_pounds(), 'фунтов')
# w1.kg_k = 41.5
# print(w1.kg_k, 'кг =>', end='')
# print(w1.to_pounds(), 'фунтов')


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежит {self.surname} был открыт. ')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт. ')
#
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd )
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur )
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете.')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#         self.print_balance()
#
#
#
#
# ass = Account('12345', 'Долгих', 0.03, 1000)
# ass.print_info()
# ass.convert_to_usd()
# ass.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# ass.convert_to_usd()
# Account.set_eur_rate(3)
# ass.convert_to_eur()
# print()
# ass.edit_owner('Дюма')
# ass.print_info()
# print()
# ass.add_percents()
# print()
# ass.withdraw_money(3000)
# print()
# ass.withdraw_money(100)
# print()
# ass.add_money(5000)
# print()
# ass.withdraw_money(3000)
# print()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника: ', end='')
#         return self.__width * self.__height
#
# rect = Rectangle(10, 20, 'green')
# # rect.width = 5
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect.color)
# print(rect.area())


# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*' * 30)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*' * 30)


# class Liguid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, val):
#         self.density = val
#
#     def calc_v(self, m):
#         v = m / self.density
#         print(f'Объем {m} кг {self.name} равен {v} m^3')
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')
#
#     def print_info(self):
#         print(f'Жидкость "{self.name}" (плотность = {self.density}kg/m^3).')
#
#
# class Alcohol(Liguid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# a.calc_v(300)
# a.calc_m(0.5)
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def set_name_notebook(self):
#         print(f'{self.name} => ', end=' ')
#         self.note.set_notebook_all()
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.processor = 'i7'
#             self.memory = 16
#
#         def set_notebook_all(self):
#             print(f'{self.model}, {self.processor}, {self.memory}')
#
#
# s1 = Student('Roman')
# s2 = Student('Vova')
# s1.set_name_notebook()
# s2.set_name_notebook()


# class Point3D:
#     CH = 'Координата должна быть числом'
#     RIGHT = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.__x}, {self.__y}, {self.__z}'
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int | float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     @staticmethod
#     def __check0(v):
#         if v.x == 0 or v.y == 0 or v.z == 0:
#             raise ZeroDivisionError('Ни одна из координат не должна быть нулем')
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print('Неверно задан ключ')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print('Координаты должны быть числами')
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print('Координаты первой точки: ', pt1)
# print('Координаты второй точки: ', pt2)
#
# pt3 = pt1 + pt2
# print(f'Сложение координат: ({pt3})')
#
# pt4 = pt1 - pt2
# print(f'Разность координат: ({pt4})')
#
# pt5 = pt1 * pt2
# print(f'Умножение: ({pt5})')
#
# pt6 = pt1 / pt2
# print(f'Деление: ({pt6})')
#
# pt7 = pt1 == pt2
# print(f'Равенство координат: {pt7}')
#
# print('x=', pt1['x'], 'x1=', pt2['x'])
# print('y=', pt1['y'], 'y1=', pt2['y'])
# print('z=', pt1['z'], 'z1=', pt2['z'])
#
# pt1['x'] = 20
# print('Запись значения в координату x: ', pt1['x'])

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age} года.'
#
#     def make_sound(self):
#         return f'{self.name} мяукает.'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age} года.'
#
#     def make_sound(self):
#         return f'{self.name} гавкает.'
#
#
# c = Cat('Пушок', 2.5)
# # print(c.info())
# d = Dog('Мухтар', 4)
# # print(d.info())
# # shape = [c, d]
# for g in [c, d]:
#     print(g.info(),'\n',g.make_sound())


# class Human:
#     def __init__(self, lastname, name, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.lastname} {self.name} {self.age}', end=' ')
#
#
# class Student(Human):
#     def __init__(self, lastname, name, age, direction, group, rating):
#         super().__init__(lastname, name, age)
#         self.direction = direction
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.direction} {self.group} {self.rating}', end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, lastname, name, age, spec, exp):
#         super().__init__(lastname, name, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.exp}', end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, lastname, name, age, direction, group, rating, theme):
#         super().__init__(lastname, name, age, direction, group, rating)
#         self.theme = theme
#
#     def info(self):
#         super().info()
#         print(f'{self.theme}', end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         return res ** 2
#
#
# @Power
# def func1(a, b):
#     return a * b
#
#
# n = func1(2, 3)
# print(n)


# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.name
#         return wrap
#
#
# @Power(2)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))
# import json
#
# data = {
#     "first_name": "Jane",
#     "last_name": "Doe",
#     "hobbies": ("running", "sky diving", "singing"),
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Alice",
#             "age": 6
#         },
#         {
#             "first_name": "Bob",
#             "age": 8
#         },
#     ]
# }
# with open("data_file.json", "w") as fw:
#     json.dump(data, fw,indent=4)
#
# with open("data_file.json", "r") as fw:
#     data = json.load(fw)
#     print(data)
# json_string = json.dumps(data, sort_keys=False)
# print(json_string )
#
# data = json.loads(json_string )
# print(data)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#     key = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     while len(key) != 10:
#         key += choice(nums)
#     # print(key)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, key
#
#
# def write_json(person_dict, key):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#     data[key] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for _ in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ', '
#         return f'Студент: {self.name} {a[:-2]}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f'Группа: {self.group}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bond', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikola', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]

# Student.load_from_file('student.json')
# Student.dump_to_json(st1, 'student.json')
# Student.dump_to_json(st3, 'student.json')

# my_group = Group(sts, 'ГК Python')
# print(my_group)
# Group.dump_group('group.json', my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st3]
# my_group2 = Group(group22, 'ГК Web')
# print(my_group2)
# Group.dump_group('group.json', my_group2)
# Group.upload_group(('group.json'))
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)


# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 4)
# print(st1)
# print(st1.average_mark())

# import json
#
#
# class Country:
#
#     def __init__(self, num):
#         self.data = {}
#         self.num = num
#
#     def __str__(self):
#         return f'{self.num}'
#
#     def pin_country(self):
#         if self.num == 5:
#             with open('country.json', 'r') as f:
#                 return json.load(f)
#
#
#     def add_country(self):
#         if self.num == 1:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны: ')
#             capital = input('Введите название столицы страны: ')
#             self.data[country] = capital
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 print('Файл сохранен')
#
#     def removal_country(self):
#         if self.num == 2:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны для удаления: ')
#             self.data.pop(country)
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 print('Файл сохранен')
#
#     def scan_country(self):
#         if self.num == 3:
#             self.data = json.load(open('country.json'))
#             country = input('Введите название страны для поиска столицы: ')
#             n = self.data[country]
#             return f'Столица - {n}'
#
#     def changes_country(self):
#         if self.num == 4:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны столицу которой хотите изменить: ')
#             capital = input('Введите новое название столицы: ')
#             self.data[country] = capital
#
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 m = self.data.get(country)
#                 return f'Уточненное название столицы - {m}'
#
#     def end_of(self):
#         if self.num == 6:
#             return f'Завершение работы.'
#
#     @classmethod
#     def main(cls):
#
#         while True:
#             print('*' * 40)
#             print(
#                 f'Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                 f'3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                 f'6 - завершение работы'
#             )
#             num = int(input('Ввод: '))
#             if num == 5:
#                 print(Country(5).pin_country())
#             elif num == 1:
#                 print(Country(1).add_country())
#
#             elif num == 2:
#                 print(Country(2).removal_country())
#
#             elif num == 3:
#                 print(Country(3).scan_country())
#
#             elif num == 4:
#                 print(Country(4).changes_country())
#             else:
#                 print(Country(6).end_of())
#                 print('*' * 40)
#                 break
#
#
# Country.main()

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
#
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# month = int(input('Введите номер месяца: '))
# if 1 <= month <= 2 or month == 12:
#     print('Зима')
# elif 3 <= month <= 5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# else:
#     print('Нет такого месяца')

# n = int(input('Введите число от 1 до 99: '))
# if 0 <= n <= 99:
#     if 11 <= n <= 14:
#         print(f'{n} копеек')
#     elif n % 10 == 1:
#         print(f'{n} копейка')
#     elif 2 <= n % 10 <= 4:
#         print(f'{n} копейки')
#     else:
#         print(f'{n} копеек')
# else:
#     print('Не верный диапазон')

# n = input('Ведите число цифрой или прописью: ')
# m = input('Ведите число цифрой или прописью: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# print('*' * 7)

# n = int(input('Ведите начало диапазона: '))
# m = int(input('Ведите конец диапазона: '))
#
# i = n
# res = 0
# while i <= m:
#     if i % 2:
#         res += i
#     i += 1
# print(f'Сумма целых нечетных чисел: {res}')

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print('Результат: ', res)

# res = ''
# while True:
#
#     print('Выберете операцию:')
#     print(f'1 - "g" - выход\n2 - "+" - сложение\n3 - "-" - вычитание\n'
#           f'4 - "/" - деление\n5 - "*" - умножение\n6 - "%" - деление по модулю')
#     n = int(input('Введите цифру: '))
#
#     if n == 1:
#         break
#     m = int(input('Введите первое число: '))
#     s = int(input('Введите второе число: '))
#     if s == 0:
#         print('На 0 делить нельзя')
#     elif n == 2:
#         res = m + s
#         print(res)
#     elif n == 3:
#         res = m - s
#         print(res)
#     elif n == 4:
#         res = m / s
#         print(res)
#     elif n == 5:
#         res = m * s
#         print(res)
#     elif n == 6:
#         res = m % s
#         print(res)

# n = int(input('Количество символов: '))
# m = input('Тип символа: ')
# print(f'0 - горизонтальная\n1 - вертикальная')
# s = int(input('Ориентация линии:'))
# i = 0
# while i < n:
#     if s == 0:
#         print(m, end=' ')
#     elif s == 1:
#         print(m )
#     else:
#         print('Такой ориентации не предусмотрено.')
#         break
#     i += 1

# n = int(input('Введите количество чисел последовательности: '))
# i = 1
# num = float(input('Введите число: '))
# res = 0
# minim = num
# maxim = num
# while i < n:
#     num = float(input('Введите число: '))
#     res += num / n
#     if maxim < n:
#         maxim = n
#     if minim > n:
#         minim = n
#     i += 1
# print('Количество чисел', n)
# print('Среднее арифметическое:', res)
# print('Минимальное число равно:', minim)
# print('Максимальное число равно:', maxim)

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# n = int(input('Введите целое число: '))
# for i in range(1, n):
#     if n % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=' ')

# n = int(input('Введите длину прямоугольника: '))
# m = int(input('Введите высоту прямоугольника: '))
# for i in range(m + 1):
#     for j in range(n + 1):
#         print('*', end=' ')
#     print()

# n = int(input('Введите длину прямоугольника: '))
# m = int(input('Введите высоту прямоугольника: '))
# for i in range(m):
#     for j in range(n):
#         if i == 0 or i == m - 1 or j == 0 or j == n - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# n = 5
# for i in range(1, n + 1):
#     print(i ** 2, end=' ')

# генератор ввода кода
# print([int(input('-> ')) for i in range(int(input('n = ')))])

# n = 4
# sum = 0
# for i in range(4):
#     a = int(input('-> '))
#     if a < 0:
#         sum += a
# print(sum)

# sum = 0
# cal = 0
# for i in range(20):
#     if i % 2 == 0:
#         cal += 1
#     else:
#         sum += i
# print('Количество четных элементов: ', cal)
# print('Сумма  нечетных: ', sum)

# s = 0
# k = 0
# n = [6, 3, 0, 8, 2]
# for i in n:
#     if i > 0:
#         s += i
#         k += 1
# print('Среднее арифметическое:', s / k)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# n = int(input('Количество элементов списка: '))
# m = []
# for i in range(n):
#     s = int(input('Введите число кратное 3: '))
#     if s % 3 == 0:
#         m.append(s)
#     else:
#         print(f'{s} не делится на 3 без остатка.')
# print(m)

# n = [1, 2, 3]
# m = [11, 22, 33, 5, 6]
# c = []
# i = 0
# while i < len(m):
#     if i < len(n):
#         c.append(n[i])
#         c.append(m[i])
#     else:
#         c.append(m[i])
#     i += 1
# print(c)

# m = [11, 22, 33, 5, 6]
# del m[2]
# print(m)

# n = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m = []
# for i in n:
#     if n.count(i) == 1:
#         m.append(i)
# print(m)


# import requests
# import json

# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#

#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = ' and '.join(users)
# s = 's' if len(users) > 1 else ''
# print(f'user{s} {max_users} completed {max_complete} TODOs')
#
#

#
#
# with open('filtered_file.json', 'w') as data_file:
#     filtered_todos = list(filter(keep, todos))
#     # print(filtered_todos)
#     json.dump(filtered_todos, data_file, indent=2)
# with open('filtered_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

# import csv

# with open('data.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
# count = 0
# for row in file_reader:
#     print(row)
#     if count == 0:
#         print(f"Файл содержит столбцы: {', '.join(row)}")
#     else:
#         print(f'   {row[0]} - {row[2]}. Родился в {row[2]} году.')
#     count += 1
# print(f'Всего в файле {count} строки.')
# with open('data.csv') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f'{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году')
#         # count += 1
# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '10'])
#     writer.writerow(['Петя', '8', '11'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=',', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
# with open('data_new.csv', 'r') as f:
#     print(f.read())

# with open('student1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow(({'Имя': 'Саша', 'Возраст': '7'}))

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import csv
#
# with open('DZ/data2.csv', 'r') as f:
#     print(f.read())

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='name').text
# row = soup.find_all('div', class_='name')
# row = soup.find_all('div', {'class':'name'})
# row = soup.find('div', {'data-set':'salary'})
# row = soup.find('div', text='Alena').parent
# row = soup.find('div', text='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)
# import re
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv


# reg = requests.get('https://ru.wordpress.org/')
# print(reg.headers['Content-Type'])
# reg.encoding = 'utf-8'
# print(reg.text)


# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title')
#     return p1
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         # url = plugin.find('h3').find('a')['href']
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#         # print(data)
#
#         # print(rating)
#     # return len(plugins)
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def write_csv(name):
#     with open('DZ/built_in.csv', 'w', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=",", lineterminator='\r', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(name)
#
#
# name = []
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     s1 = soup.find_all('div', class_='page__content')[0]
#     plugins = s1.find_all('h3')
#     for plugin in plugins:
#         data = plugin.find('a').get('name')
#         name.append(data)
#         write_csv(name)
#
#
# def main():
#     url = 'https://letpy.com/handbook/builtins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import random as r

# a = [r.randint(0, 100) for i in range(10)]
# n = max(a)
# print(n)
# m = a.remove(n)
# print(a)
# a[0] = n
# print(a)

# a = [r.randint(-20, 20) for i in range(10)]
# a.sort(reverse=True)
# print(a)
# m = []
# n = []
# for i in a:
#     if i >= 0:
#         m.append(i)
#     else:
#         n.append(i)
# print(m + n)
# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# n = min(a)
# m = a.index(n)
# a[:m] = []
# print(a)

# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print('a=', a)
# print('b=', b)
# c = a + b
# print('c=', c)
# c = []
# for i in a:
#     for j in b:
#         if i not in c:
#             c.append(i)
#         elif j not in c:
#             c.append(j)
# print('Элементы обоих списков без повторений', c)
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#         elif j == i:
#             c.append(j)
# print('Общие для двух списков', c)
# c = [min(a),min(b),max(a),max(b)]
# print(c)

# m = [[r.randint(0, 4) for i in range(3)] for j in range(4)]
# print(m)
# res = 1
# for i in m:
#     for x in i:
#         if x > 0:
#             res *= x
#         print(x, end='\t')
#     print()
# print(res)

# n = [[r.randint(0, 10) for i in range(6)] for j in range(6)]
# m = [r.randint(0, 10) for b in range(6)]
# print(n)
# print(m)
# c = []
# for i in range(len(n)):
#     if i % 2 == 0:
#         n[i] = m
# for i in n:
#     for x in i:
#         print(x, end='\t ')
#     print()

# def fun(a, b, c):
#     for i in range(c):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# fun('+', '-', 9)
# fun('X', 'O', 7)

# def fun(n, m):
#     if n > m:
#         return n - m
#     else:
#         return n + m
#
#
# print(fun(5, 9))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     # a = lst.pop(0)
#     # b = lst.pop(-1)
#     # lst.insert(0, b)
#     # lst.append(a)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def fun(n=20, m='-'):
#     return m * n
#
#
# print(fun(10, m='+'))
# print(fun(5, m='*'))
# print(fun(15, m='#'))
# print(fun(7))
# print(fun())


# def fun(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр: ')
# print(fun(9874023))
# print(fun(38271))
# print(fun(123456789))
# print('Сумма нечетных цифр: ')
# print(fun(9874023, False))
# print(fun(38271, False))
# print(fun(123456789, False))

# import math

# def fun(n):
#     if n == 1:
#         a = int(input('Высота: '))
#         b = int(input('Ширина'))
#         return f'Площадь: {a * b}'
#     elif n == 2:
#         c = int(input('Основание: '))
#         s = int(input('Высота: '))
#         return f'Площадь: {0.5 * c * s}'
#     elif n == 3:
#         v = int(input('Радиус: '))
#         return f'Площадь: {round(math.pi * v ** 2, 2)}'
#     else:
#         return 'Выход'
#
#
# m = 0
# while m <= 3:
#     print('1-прямоугольник\n2-треугольник\n3-круг\n4-выход')
#     m = int(input('Введите цифру: '))
#     print(fun(m))

# n = []
# for i in range(1, 13):
#     n.append(2 ** i)
# print(tuple(n))

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             n = tpl.index(el)
#             m = tpl.index(el, n + 1)
#             return tpl[n:m + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def to_set(el):
#     n = set(el)
#     return n, len(n)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# n = ('ab', 'abcd', 'cde', 'abc', 'def')
# if n.count('ab'):
#     print('Yes')
# else:
#     print('No')
# s = {'Yes' for i in n if i == 'ab'}

# n = tuple(input('Введите элементы кортежа: '))
# m = set(n)
# s = 0
# for i in m:
#     if i:
#         print('Количество', i, '=', n.count(i))

# a, b, c, d, s, f, x = {1, 2}, {3}, {4, 5}, {3, 2, 6}, {6}, {7, 8}, {9, 8}
# n = a | b | c | d | s | f | x
# print(n)
# print('Длина:', len(n))
# print('Мин:', min(n))
# print('Максимум:', max(n))

# s1 = set('Hello')
# s2 = set('How are you')
# n = s1 & s2
# for i in n:
#     print(i, end=' ')

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in d:
#     res *= d[i]
# print(res)

# d = {key:input('-> ') for key in range(1,5)}
# d1 = {1: 'карт', 2: 'мор', 3: 'бак', 4: 'лук'}
# del d1[3]
# print(d1)
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# n = x | y
# print(n)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# n = {}
# n['name'] = d.pop('name')
# n['salary'] = d.pop('salary')
# print(n)
# print(d)

# d = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     ' Anna': {
#         'N': 5239,
#         'S': 4802,
#         'E': 8441,
#         'W': 2694
#     },
#     'Fiona': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     }
#
# }
# for x in d:
#     print(x)
#     for y in d[x]:
#         print('\t', y, ':', d[x][y], sep='')
# name = input('Введите имя: ')
# region = input('Введите регион: ')
# print(d[name][region])
# data = int(input('Введите: '))
# d[name][region] = data
# print(d[name])

# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d = {k: v for k, v in data.items() if v <= 2 }
# print(d)

# s = 'Hello'
# b = {i: i for i in s}
# print(b)

# print(list(zip(range(100), range(5))))

# one = {"name": "Igor", "last_name": "Smith", "job": "Consultant"}
# two = {"name": "Olga", "last_name": "Doe", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# Распаковка последовательности
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)


# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в", m, "=", profit)

# one = {'apple': 20, 'orange': 35, 'pepper': 60}
# two = {'pepper': 40, 'onion': 55}
# print([two, one])
# print({**two, **one})
# {{'pepper': 40, 'onion': 55}, {'apple': 20, 'orange': 35}}


# for i in range(3):
#     print(i)
#
# colors = ["red", "yellow", "green"]
# j = 1
# for i in colors:
#     print(j, i)
#     j += 1

# colors = ["red", "yellow", "green"]
# for j, i in enumerate(colors, 1):
#     print(j, i)

# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i, "STOP"))
# print(next(i, "STOP"))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 1, 3))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(7, 3))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def ch(*args):
#     res = []
#     sr_ar = sum(args) / len(args)
#     print(sr_ar)
#
#     for i in args:
#         if i < sr_ar:
#             res.append(i)
#
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))

# def print_scores(student, *scores):
#     print("Student Name: " + student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Irina", 100, 95, 88, 92, 99)
# print_scores("Igor", 96, 20, 33)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))

# def intro(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# intro(first_name="Irina", last_name="Fokina", age=22)
# intro(first_name="Igor", last_name="WOOD", email='igor@gmail.com', age=25, phone='9594567895')

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age='31', weight=61, eyes_color='gray')
# print('my_dict =', my_dict)

# def db(b, c, w, *args, name, **kwargs):
#     print(b, c, w, args, name, kwargs)
#
#
# db(7, 8, 9, a=5, name='Olga', q=5)

# name = 'Tom'  # глобальная область видимости
#
#
# def hi():
#     global name
#     name = 'Sam'  # локальная область видимости
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# # print(name)
# hi()
# # bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print("i =", i)
#     print("arg =", arg)
#
#
# i = 6
# func()  # 5 или 6

# x = 4
#
#
# def add_two(a):
#     # x = 2
#
#     def add_some():
#         # x = 5
#         print('x =', x)
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# min = [4, 5, 6]
# print(max(min))
# print(min(min))

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!!!")

# a = 2
#
#
# def func1():
#     a = 6
#
#     def func2(b):
#         global a
#         a = 4
#         print("Сумма:", a + b)
#
#     print("Значение переменной a:", a)
#     func2(4)
#
#
# func1()
# print(a)


# def fn1():
#     x = 25  # 1
#
#     def fn2():
#         # x = 33  # 3
#
#         def fn3():
#             nonlocal x
#             x = 55  # 5
#             print("fn3.x =", x)  # 6
#
#         fn3()  # 4
#         print("fn2.x =", x)  # 7
#
#     fn2()  # 2
#     print("fn1.x =", x)  # 8
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner(x):
#         return number + x
#     return inner
#
#
# a = increment(10)
# print(a(5))
# print(a(4))
#
# b = increment(1)
# print(b(7))
#
# print(increment(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()
#
# res1()


# student = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def students(exem):
#         return {k: v for k, v in exem.items() if lower <= v < upper}
#
#     return students
#
#
# a = make_classifier(80, 100)
# b = make_classifier(70, 80)
# c = make_classifier(50, 70)
# d = make_classifier(0, 50)
#
# print(a(student))
# print(b(student))
# print(c(student))
# print(d(student))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def fun(*args):
#     l = []
#     res = sum(args) / len(args)
#     print(res)
#     for i in args:
#         if i < res:
#             l.append(i)
#     return l
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# n = a | b | c
# print(n)

# d = {'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Bred', 'salary': 6500}
#      }
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j], sep='')

# d = {}
#
#
# def my_dict(**kwargs):
#     d.update(kwargs)
#     return d
#
#
# print(my_dict(one='first'))
# print(my_dict(k1=22, k2=31, k3=11, k4=91))
# print(my_dict(name='bob', age=31))


# def fun(name):
#     col = 0
#
#     def new_fun():
#         nonlocal col
#         col += 1
#         return f'{name} {col}'
#
#     return new_fun
#
#
# a = fun('Москва')
# b = fun('Сочи')
# print(a())
# print(a())
# print(b())

# def fun(name, **kwargs):
#     if name == 'rhombus':
#         d1, d2 = kwargs.values()
#         return (d1 * d2) / 2
#
#
# print(fun('rhombus', d1=10, d2=8))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda x:lambda y:lambda b:x + y + b)(2)(4)(6))

# d = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
# res1 = sorted(d, key=lambda x: x['last name'])
# print(res1)
# res2 = sorted(d, key=lambda y: y['raiting'])
# print(res2)
# res3 = sorted(d, key=lambda y: y['raiting'], reverse=True)
# print(res3)


# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'],
#                           data['url'],
#                           data['snip'],
#                           data['active'],
#                           data['tested']
#                           ))
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elem = soup.find_all('article', class_='plugin-card')
#     for el in elem:
#         try:
#             name = el.find('h3').text
#             # print(name)
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get('href')
#             # print(url)
#         except ValueError:
#             url = ''
#
#         try:
#             snip = el.find('div', class_='entry-excerpt').text.strip()
#             # print(snip)
#         except ValueError:
#             snip = ''
#
#         try:
#             active = el.find('span', class_="active-installs").text.strip()
#             # print(active)
#         except ValueError:
#             active = ''
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#             print(cy)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snip': snip,
#             'active': active,
#             'tested': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(2,6):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from bs4 import BeautifulSoup
# import requests
# import csv
#
# from parse import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()
#
# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page not found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# from random import *
#
# n = [randint(1, 40) for i in range(10)]
# print(n)
# m = list(filter(lambda s: 10 <= s <= 20, n))
# print(m)


# def decor(func):
#     n = 0
#
#     def wrap():
#         nonlocal n
#         n += 1
#         func()
#         return n
#
#     return wrap
#
#
# @decor
# def hello():
#     print('Hello')
#
#
# print(hello())
# print(hello())
# print(hello())

# def multiply(n):
#     def nambers(fn):
#         def wrap(*args):
#             return n * fn(*args)
#
#         return wrap
#
#     return nambers
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print('Результат : ',return_num(5))

# s = 'Test string for me'
# n = []
# for i in s:
#     n.append(ord(i))
# n = [ord(x) for x in s]
# print('ASCII коды:', n)
# n = [int(sum(n) / len(n))] + n
# print('Среднее арифметическое:', n)
# n += [x for x in [ord(x) for x in (input('-> '))[:3]] if x not in n]
# print(n)
# if n[-1] in n[:-1]:
#     print('Количество последних элементов:', n.count(n[-1]) - 1)
# n.sort(reverse=True)
# print(n)

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')

# n = 'один два'
# m = n[:n.find(' ')]
# v = n[n.find(' ') + 1:]
# s = v + ' ' + m
# print(s)

# s = 'ab12c59p7dq'
# n = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         n.append(int(i))
# print(n)

# n = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# v = n.index('(')
# c = n.index(')')
# m = n[v + 1:c]
# print(m)

# s = 'В строке заменить пробелы символом'
# n = s.split()
# print('*'.join(n))

# import re
# n = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, n))

# s = '05-03-1987 # Дата рождения'
# n = re.sub('#.*','',s)
# print('Дата рождения:', re.sub('-', '.', n))

# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# n = r'\w+\s*=\s*[^;]+'
# print(re.findall(n, s))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# # n = r'\s[+]*\d{11}'
# n = r'\+?7\d{10}'
# print(re.findall(n, s))

# s = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru'
# n = r'[A-zА-я0-9_-]+@[A-zА-я0-9\.]+'
# print(re.findall(n, s))

# s = 'Desktop\ДЗ[76] по курсу[65] PYTHON[22]5\venv\Scripts\python.exe"[78] \Desktop\ДЗ по курсу '
# n = r'\[.*?]'
# print(re.findall(n, s))

# s = '28-08-2021'
# n = '(0[1-9]|[1-3][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(n, s))


# def validate_phone(name):
#     reg = r'\+?[0-9\s\(\)-]+$'
#     # reg = r'^\+?7[ (]*\d+[ )]*[\d -]{8,10}$'
#     return re.search(reg, name).group()
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for _ in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# Рекурсия

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# f = open(r'C:\Users\User\Desktop\ДЗ по курсу PYTHON\ДЗ_Python225\text.txt', 'r')
# n = []
# for i in f:
#     n.append(i)
# print(len(n))
# print(len(f.readlines()))

# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# f = open(r'C:\Users\User\Desktop\ДЗ по курсу PYTHON\ДЗ_Python225\text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()
# s = ['This is line4', 'This is line4']
# f = open('text.txt', 'a')
# f.writelines(s)
# f.close()
# f = open('text.txt', 'w')
# s = [str(i) + str(i -1) for i in range(1,20)]
# # print(s)
# for i in s:
#     f.write(i + '\t')
# f.close()
# n = [-2, 3, 8, -11, -4, 6]


# def my(lst):
#     count = 0
#     for i in lst:
#         if i > 0:
#             count += 1
#     return count
#
#
# print(my(n))
# def my(lst):
#     count = 0
#     for i in lst[:]:
#         if i > 0 or len(lst) == 0:
#             lst[0] += my(lst[1:])
#         else:
#             count += 1
#     return count
#
#
# print(my(n))

# s = ['методами', 'символов', 'попыткой']
# with open('text.txt', 'w') as f:
#     n = ' '.join(s)
#     f.write(n)
# with open('text.txt', 'r') as f:
#     m = f.read().split()
#     b = len(max(m, key=len))
#     res = [i for i in m if len(i) == b]
#     print(res)

# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10'
#
# with open('text.txt', 'w', encoding='utf-8') as f:
#     f.write(text)

# read_file = 'text.txt'
# write_file = 'text2.txt'
#
# with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
# with open(write_file, 'r', encoding='utf-8') as fw:
#     for line in fw:
#         print(line, end='')
# f = open('text.txt',)
# line = 0
# for i in f:
#     line += 1
# print(line, ' строк')
# f.close()
# import os

# print('Текущая директория:', os.getcwd())
# # print(os.listdir())
# print(os.listdir('..'))

# os.mkdir('folder')
# os.makedirs()

# import sqlite3 as sq
#
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('DROP TABLE users')
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data TEXT
#     # )""")
# import math

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные'.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\n'
#               f'Номер телефона: {self.phone}\nСтрана: {self.country}\n'
#               f'Город: {self.city}\nДомашний адрес: {self.address}')
#         print(40 * '=')
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Валерия')
# print(h1.get_name())

# class Book:
#     name = 'name'
#     year = 'year'
#     publisher = 'publisher'
#     genre = 'genre'
#     author = 'author'
#     price = 'price'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Название книги: {self.name}\n'
#               f'Год выпуска: {self.year}\n'
#               f'Издатель: {self.publisher}\n'
#               f'Жанр: {self.genre}\n'
#               f'Автор: {self.author}\n'
#               f'Цена: {self.price}')
#         print('=' * 40)
#
#     def input_info(self, name, year, publisher, genre, author, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
#
# h2 = Book()
# h2.input_info('Дон', '1960', 'Москва', 'Фантастика', 'Иванов', '100руб')
# h2.print_info()
# h2.set_name('Волга')
# print(h2.get_name())

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'Выключается!')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Осталось :', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут:', self.name)
#
#
# r1 = Robot('R2-D2')
# r1.say_hi()
# print('Численность роботов:', Robot.k)
# r2 = Robot('C-3PO')
# r2.say_hi()
# print('Численность роботов:', Robot.k)
#
# print('\nЗдесь роботы проделывают работу\n')
# print('Роботы закончили работу.Давайте их выключим')
# del r1
# del r2
# print('Численность роботов:', Robot.k)

# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.name = self.model = self.color = 'Некорректные данные'
#         self.year = self.power = self.price = 0
#         if Car.__check_value_str(name):
#             self.name = name
#             self.model = model
#             self.color = color
#         if Car.__check_value_int(year):
#             self.year = year
#             self.power = power
#             self.price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int | float):
#             print('Данные должны быть числом')
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print('Данные должны быть строкой')
#             return False
#         return True
#
#     def set_name(self, name):
#         if Car.__check_value_str(name):
#             self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def print_info(self):
#         print('Данные автомобиля'.center(40, '*'))
#         print(f"""Название модели: {self.name}
# Год выпуска: {self.year}
# Производитель: {self.model}
# Мощность двигателя: {self.power} л.с.
# Цвет машины: {self.color}
# Цена: {self.price}""")
#         print(40 * '=')
#
#
# c1 = Car('X7 M50i', '2021', 'BMW', 530, 'white', 10790000)
# c1.print_info()
# c1.set_name(122)
# print(c1.get_name())
# c1.print_info()
# import math
#
#
# class Rectangle:
#
#     def __init__(self, length, width):
#         if Rectangle.__check_value_int(length):
#             self.length = length
#         if Rectangle.__check_value_int(width):
#             self.width = width
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print('Данные должны быть числом')
#             return False
#         return True
#
#     def set_length(self, length):
#         if Rectangle.__check_value_int(length):
#             self.length = length
#
#     def set_width(self, width):
#         if Rectangle.__check_value_int(width):
#             self.width = width
#
#     def get_length(self):
#         return self.length
#
#     def get_width(self):
#         return self.width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return self.length * 2 + self.width * 2
#
#     def hypotenuse(self):
#         return round(math.sqrt(self.length ** 2 + self.width ** 2), 2)
#
#     def picture(self):
#         print(('*' * self.width + '\n') * self.length)
#
#
# r1 = Rectangle(3, 9)
# print('Длина прямоугольника:', r1.get_length())
# print('Ширина прямоугольника:', r1.get_width())
# print('Площадь прямоугольника:', r1.area())
# print('Периметр прямоугольника:', r1.perimeter())
# print('Гипотенуза прямоугольника:', r1.hypotenuse())
# r1.picture()
# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def coord(self):
#         return self.__name
#
#     @property
#     def coord_age(self):
#         return self.__age
#
#     @coord.setter
#     def coord(self, name):
#         self.__name = name
#
#     @coord_age.setter
#     def coord_age(self, age):
#         self.__age = age
#
#     @coord.deleter
#     def coord(self):
#         del self.__name
#
#     @coord_age.deleter
#     def coord_age(self):
#         del self.__age
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.coord = 'Igor'
# p1.coord_age = 31
# print(p1.__dict__)
# del p1.coord_age
# print(p1.__dict__)

# class Numbers:
#
#     @staticmethod
#     def minimum(a, b, c, d):
#         n = min(a, b, c, d)
#         return n
#
#     @staticmethod
#     def max(a, b, c, d):
#         m = max(a, b, c, d)
#         return m
#
#     @staticmethod
#     def sr(a, b, c, d):
#         k = (a + b + c + d) / 4
#         return k
#
#     @staticmethod
#     def num(a):
#         n = 1
#         for i in range(1, a + 1):
#             n *= i
#         return n
#
#
# print('Минимальное число: ', Numbers.minimum(4, 5, 6, 7))
# print('Максимальное число: ', Numbers.max(4, 5, 6, 7))
# print('Среднее число: ', Numbers.sr(4, 5, 6, 7))
# print('Факториал: ', Numbers.num(5))

# import sqlite3 as sq

# with sq.connect('users.db') as con:
#     cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT +79090000000,
# age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )
# """)
# cur.execute("""
# ALTER TABLE person
# RENAME TO prson_table
# """)
# cur.execute("""
#     ALTER TABLE prson_table
#     ADD COLUMN address TEXT
#     """)
# cur.execute("""
#         ALTER TABLE prson_table
#         RENAME COLUMN address TO home_address
#         """)

# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS person(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         phone BLOB NOT NULL DEFAULT +79090000000,
#         age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#         email TEXT UNIQUE
#         )
#         """)
#     cur.execute("""
#         INSERT INTO person
#         VALUES(1, 'Ирина', '+7509866666', 23, 'irina@gmail.ru')
#         """)
# import sqlite3 as sq

# with sq.connect('db_4.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM Ware
#         ORDER BY Price DESC
#         LIMIT 5 OFFSET 2
#         """)
#     res = cur.fetchone()
#     res2 = cur.fetchmany(2)
#     print(res)
#     print(res2)

# class Convert:
#     def __init__(self, heft=0):
#         self.__heft = heft
#
#     @property
#     def heft(self):
#         return self.__heft
#
#     @heft.setter
#     def heft(self, heft):
#         if isinstance(heft, int | float):
#             self.__heft = heft
#         else:
#             print('Данные должны быть цифрой')
#
#     def res(self):
#         m = round(self.__heft * 2.205,2)
#         return f'{self.__heft} кг => {m} фунтов'
#
#
# c1 = Convert(12)
# print(c1.heft)
# print(c1.res())
# c1.heft = '41'
# print(c1.res())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете: ')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if self.value < val:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# a1 = Account('12345', 'Долгих', 0.03, 1000)
# a1.print_info()
# a1.convert_to_usd()
# a1.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# a1.convert_to_usd()
# Account.set_eur_rate(3)
# a1.convert_to_eur()
# print()
# a1.edit_owner('Дюма')
# a1.print_info()
# print()
# a1.add_percents()
# print()
# a1.withdraw_money(100)
# print()
# a1.add_money(5000)
# print()
# a1.withdraw_money(3000)
# print()
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_ps(ps)
#         self.verify_weight(weight)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Не верный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for i in f:
#             if len(i.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес от 20 кг и выше')
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Не верный формат паспорта')
#         for i in s:
#             if not i.isdigit():
#                 raise TypeError('Серия и номер должны быть цифрами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
# p1.fio = 'Петров Игорь Николаевич'
# print(p1.fio)
# print(p1.__dict__)
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете: ')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if self.value < val:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# a1 = Account('12345', 'Долгих', 0.03, 1000)
# a1.print_info()
# a1.convert_to_usd()
# a1.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# a1.convert_to_usd()
# Account.set_eur_rate(3)
# a1.convert_to_eur()
# print()
# a1.edit_owner('Дюма')
# a1.print_info()
# print()
# a1.add_percents()
# print()
# a1.withdraw_money(100)
# print()
# a1.add_money(4000)
# print()
# a1.withdraw_money(3000)
# print()

# def queue_time(customers, n):
#     tills = [0] * n
#     for i in customers:
#         tills[0] += i
#         tills.sort()
#     return max(tills)
#
#
# print(queue_time([], 1))
# print(queue_time([5], 1))
# print(queue_time([2], 5))
# print(queue_time([1, 2, 3, 4, 5], 1))
# print(queue_time([1, 2, 3, 4, 5], 100))
# print(queue_time([2, 2, 3, 3, 4, 4], 2))

# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             # self._width = width
#             # self._length = length
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):  # абстрактный метод
#         raise NotImplementedError('В дочернем классе должен быть метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=30)
# print(t2.__dict__)
# print(t2.calc_area())

# class Liquid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, val):
#         self.density = val
#
#     def calc_v(self, m):
#         v = m / self.density
#         print(f"Объем {m} кг {self.name} равен {v} m^3")
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f"Вес {v} m^3 of {self.name} составляет {m} кг.")
#
#     def print_info(self):
#         print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.computer = self.Computer()
#
#     def print_info(self):
#         print(f'{self.name} => ', end='')
#         self.computer.print_info()
#
#     class Computer:
#         def __init__(self):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.memory = 16
#
#         def print_info(self):
#             print(f' {self.model}, {self.cpu}, {self.memory}')
#
#
# s = Student('Roman')
# s.print_info()
# s = Student('Vladimir')
# s.print_info()
# from math import sqrt


# import sqlite3 as sq
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 50000),
#     ('Daewoo', 56000),
#     ('Citroen', 57000),
#     ('Honda', 58000)
# ]
# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT, price INTEGER);
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, "Renault", 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print('Ошибка запроса')
# finally:
#     if con:
#         con.close()
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT, price INTEGER)
#
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE'B%'", {'Price': 0})
# cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)
# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL,?,?)", car)
# cur.execute('INSERT INTO cars VALUES(1, "Renault", 22000)')
# cur.execute('INSERT INTO cars VALUES(2, "Volvo", 29000)')
# cur.execute('INSERT INTO cars VALUES(3, "Mercedes", 52000)')
# cur.execute('INSERT INTO cars VALUES(4, "Bentley", 59000)')
# cur.execute('INSERT INTO cars VALUES(5, "Audy", 62000)')
#
# with sq.connect('db/cars.db') as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT, price INTEGER);
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL,'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # это id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья',?,?)", (last_row_id, buy_car_id))

# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f'avatars/avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     # print(con.row_factory)
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name Text,
#         ava BLOB,
#         score INTEGER)
#
#     """)
#
#     cur.execute('SELECT ava FROM users LIMIT 1')
#     img = cur.fetchone()['ava']
#     write_ava('out.png', img)

# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute('INSERT INTO users VALUES ("Илья", ?, 1000)', (binary,))
# cur.execute('SELECT model, price FROM cars')
# rows = cur.fetchall()
# print(rows)
# rows = cur.fetchmany(5)
# print(rows)
# for res in cur:
#     print(res['model'], -  res['price'])
# import sqlite3 as sq
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()

# with open('sql_dump.sql', 'w') as f:
#     for sql in con.iterdump():
#         f.write(sql)
# with open('sql_dump.sql', 'r') as f:
#     sql = f.read()
#     cur.executescript(sql)
# import sqlite3 as sq
#
# data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево')]
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     ru TEXT)""")
#     cur.executemany('INSERT INTO dict VALUES(?, ?)', data)
#     cur.execute('SELECT ru FROM dict WHERE eng LIKE "c%"')
#     print(cur.fetchall())

# import sqlite3 as sq
#
# text = [
#     ('Вишня', 2000, 2),
#     ('Слива', 3000, 1),
#     ('Яблоня', 1500, 3),
# ]
#
# with sq.connect('db/garden.db') as gar:
#     cur = gar.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS garden(
#     garden_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     price INTEGER,
#     year INTEGER)
#     """)
#
#     cur.executescript("""
#     DELETE FROM garden WHERE garden_id > 4;
#     UPDATE garden SET price = price + 200
#     """)
# cur.execute('INSERT INTO garden VALUES(1, "груша", 2500, 2)')
# cur.executemany('INSERT INTO garden VALUES(NULL, ?, ?, ?)', text)
# for i in text:
#     cur.execute('INSERT INTO garden VALUES(NULL,?,?,?)', i)
# import os
# from sqlalchemy import and_, or_, not_, desc, func, distinct, text
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     print(session.query(Lesson).all())# результат запроса по всем элементам в списке
#     print('*' * 60)
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print('*' * 60)
#
#     for it in session.query(Student).filter(text('surname like "М%"')).order_by(text('name, id desc')):
#         print(it)
#
# i = session.query(Lesson).get(7)
# i.lesson_title = 'Информатика'
# session.add(i)
# session.commit()
#
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print('*' * 60)
#
# session.query(Lesson).filter(Lesson.lesson_title.like('%м%')).update({'lesson_title': 'М'}, synchronize_session='fetch')
# session.commit()
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print('*' * 60)
#
# session.add(Lesson(lesson_title="Физика"))
# session.commit()
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print('*' * 60)
#
# i = session.query(Lesson).filter(Lesson.lesson_title == "Физика").first()
# session.delete(i)
# session.commit()
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print('*' * 60)
#
# print(session.query(Lesson).count())
# print('*' * 60)
# print(session.query(Lesson).first())
# print('*' * 60)
# print(session.query(Lesson).get(3))
# print('*' * 60)
# for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):
#     print(it)
# print('*' * 60)
# for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print('*' * 60)
# for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print('*' * 60)
#
# for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
#         and_(association_table.c.lesson_id == Lesson.id, association_table.c.group_id == Group.id,
#              Group.group_name == 'MDA-7')):
#     print(it, gr)
# print('*' * 60)
#
# for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print('*' * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
# print('*' * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
# print('*' * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
# print('*' * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
# print('*' * 60)
#
# print(session.query(Student).filter(Student.age.between(16, 17)).all())
# print('*' * 60)
#
# print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
# print('*' * 60)
#
# print(session.query(Student).filter(Student.age.like('1%')).all())
# print('*' * 60)
#
# for it in session.query(Student).filter(Student.age.like('1%')).limit(4):
#     print(it)
# print('*' * 60)
#
# for it in session.query(Student).filter(Student.age.like('1%')).limit(4).offset(3):
#     print(it)
# print('*' * 60)
#
# for it in session.query(Student).order_by(Student.surname):
#     print(it)
# print('*' * 60)
#
# for it in session.query(Student).order_by(desc(Student.surname)):
#     print(it)
# print('*' * 60)
#
# for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
#     print(it)
# print('*' * 60)
#
# for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
#     print(it)
# print('*' * 60)
#
# for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
#         Group.group_name).having(func.count(Student.surname) < 25):
#     print(it)
# print('*' * 60)
#
# for it in session.query(distinct(Student.age)):
#     print(it)
# print('*' * 60)
#
# for it in session.query(Student.age).filter(Student.age < 20).distinct():
#     print(it)
# print('*' * 60)

# import os
#
# from mytables.my_database import DATABASE_NAME
# import mytable_database as db_mytable
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_mytable.mytable_database()

# class Point3D:
#     CH = 'Координата должна быть числом'
#     RIGHT = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.__x}, {self.__y}, {self.__z}'
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int | float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     @staticmethod
#     def __check0(v):
#         if v.x == 0 or v.y == 0 or v.z == 0:
#             raise ZeroDivisionError('Ни одна из координат не должна быть нулем')
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print('Не верно задан ключ')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print('Координаты должны быть числами')
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print('Координаты 1-й точки: ', pt1)
# print('Координаты 2-й точки: ', pt2)
#
# pt3 = pt1 + pt2
# print(f'Сложение координат: ({pt3})')
#
# pt4 = pt1 - pt2
# print(f'Разность координат: ({pt4})')
#
# pt5 = pt1 * pt2
# print(f'Умножение координат: ({pt5})')
#
# pt6 = pt1 / pt2
# print(f'Частное координат: ({pt6})')
#
# pt7 = pt1 == pt2
# print(f'Равенство координат: ({pt7})')
#
# print('x=', pt1['x'], 'x1=', pt2['x'])
# print('y=', pt1['y'], 'y1=', pt2['y'])
# print('z=', pt1['z'], 'z1=', pt2['z'])
#
# pt1['x'] = 20
# print('Запись значения в координату x:', pt1['x'])

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# c = Cat('Пушок', 2.5)
# d = Dog('Мухтар', 4)
# n = [c, d]
# for i in n:
#     print(i.info())
#     print(i.make_sound())

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args)
#         return res ** 2
#
#
# @Power
# def res(a, b):
#     return a * b
#
#
# print(res(2, 3))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res ** self.func
#
#         return wrap
#
#
# @Power(3)
# def add(a, b):
#     return a * b
#
#
# print(add(2, 2))

# import os
# from sqlalchemy import and_, or_, not_, desc, func, distinct, text
#
# from mytables.my_database import DATABASE_NAME, Session
# import mytable_database as db_mytable
# from mytables.lesson import Lesson, association_table
# from mytables.name import Name
# from mytables.number import Number
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_mytable.mytable_database()
#
#     session = Session()
#     print(session.query(Lesson).all())
#     print('*' * 60)
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print('*' * 60)
#
#     print(session.query(Lesson).count())
#     print('*' * 60)
#
#     print(session.query(Lesson).first())
#     print('*' * 60)
#
#     print(session.query(Lesson).get(2))
#     print('*' * 60)
#
#     for it in session.query(Lesson).filter(Lesson.id >= 4, Lesson.lesson_title.like('В%')):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Lesson).filter(or_(Lesson.id >= 4, Lesson.lesson_title.like('В%'))):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Lesson).filter(and_(Lesson.id >= 4, Lesson.lesson_title.like('В%'))):
#         print(it)
#     print('*' * 60)
#
#     for it, num in session.query(Lesson.lesson_title, Number.group_name).filter(
#             and_(association_table.c.lesson_id == Lesson.id, association_table.c.group_id == Number.id,
#                  Number.group_name == 'WELL-222')):
#         print(it, num)
#     print('*' * 60)
#
#     for it in session.query(Lesson).filter(not_(Lesson.id >= 2), not_(Lesson.lesson_title.like('В%'))):
#         print(it)
#     print('*' * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
#     print('*' * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
#     print('*' * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.in_(['История', 'Тактика'])).all())
#     print('*' * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['История', 'Тактика'])).all())
#     print('*' * 60)
#
#     print(session.query(Name).filter(Name.age.between(17, 19)).all())
#     print('*' * 60)
#
#     print(session.query(Name).filter(not_(Name.age.between(17, 25))).all())
#     print('*' * 60)
#
#     print(session.query(Name).filter(Name.age.like('1%')).all())
#     print('*' * 60)
#
#     for it in session.query(Name).filter(Name.age.like('1%')).limit(5):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Name).filter(Name.age.like('1%')).limit(5).offset(4):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Name).order_by(Name.surname):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Name).order_by(desc(Name.surname)):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(Name).join(Number).filter(Number.group_name == 'WELL-221'):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(func.count(Name.surname), Number.group_name).join(Number).group_by(Number.group_name):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(func.count(Name.surname), Number.group_name).join(Number).group_by(
#             Number.group_name).having(func.count(Name.surname) < 20):
#         print(it)
#     print('*' * 60)
#
#     for it in session.query(distinct(Name.age)):
#         print(it)
#     print("*" * 60)
#
#     i = session.query(Lesson).get(8)
#     i.lesson_title = 'История'
#     session.add(i)
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
#
#     session.query(Lesson).filter(Lesson.lesson_title.like('%р%')).update({'lesson_title': 'Р'},
#                                                                          synchronize_session='fetch')
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
#
#     session.add(Lesson(lesson_title='Стрельба'))
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
#
#     i = session.query(Lesson).filter(Lesson.lesson_title == "Стрельба").first()
#     print(i)
#     session.delete(i)
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
#
#     for it in session.query(Name).filter(text("surname like 'В%'")).order_by(text("name, id desc")):
#         print(it)
#     print("*" * 60)
#
# from jinja2 import Template

# name = 'Игорь'
# age = 28

# tm = Template('Мне {{a*2}} лет. Меня зовут {{n.upper()}}.')
# msg = tm.render(n=name, a=age)

# per = {'name': 'Игорь', 'age': 28}
#
# tm = Template('Мне {{p.age}} лет. Меня зовут {{p.name}}.')
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# per = Person('Игорь', 28)
#
# tm = Template('Мне {{p.get_age()}} лет. Меня зовут {{p.get_name()}}.')
# msg = tm.render(p=per)
# print(msg)

# data = """{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставить соответствующие значения {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)
# from jinja2 import Template

# data = """{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставить соответствующие значения {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)

# link = """В HTML-документе ссылка определяется так:
# <a href='#'>Ссылка</a>
# """
# tm = Template('{{ link | e }}')
# msg = tm.render(link=link)
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Смоленск'},
#     {'id': 4, 'city': 'Минск'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select name='cities'>
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value='{{ c['id']}}'>{{ c['city'] }}</option>
# {% elif c.city == 'Москва' -%}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'}
# ]
#
# link = """<ul>
# {% for c in menu -%}
# {% if m['url'] == '/index' -%}
#     <li><a href='{{ m['url'] }}
#
#     <li value='{{ c['href']}}'>{{ c['link'] }}</option>
#
# {% endfor -%}
# </ul>"""
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# menu = [
#     {'url': '/index', 'title': 'Главная '},
#     {'url': '/news', 'title': 'О нас'},
#     {'url': '/about', 'title': 'Новости'},
#     {'url': '/shop', 'title': 'Магазин'},
#     {'url': '/contacts', 'title': 'Контакты'}
# ]
#
# text = """
#     <ul>
#     {% for m in menu -%}
#         {% if m['url'] == '/index' -%}
#             <li><a href='{{ m['url'] }}' class='active'>{{ m['title'] }}</a></li>
#         {% else %}
#             <li><a href='{{ m['url'] }}'>{{ m['title'] }}</a></li>
#         {% endif -%}
#     {% endfor -%}
#     </ul>
# """
#
# tm = Template(text)
# msg = tm.render(menu=menu)
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renault', 'price': 22000},
#     {'model': 'Mers', 'price': 24000}
# ]
# lst = [1, 2, 3, 4, 5, 6]
# # tpl = 'Сумарная цена автомобилей {{ (cs | min(attribute="price")).model }}'
# # tpl = 'Сумарная цена автомобилей {{ cs | random() }}'
# tpl = 'Сумарная цена автомобилей {{ cs | replace("model", "brand") }}'
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Николай', 'year': 20, 'weight': 58.5},
#     {'name': 'Сергей', 'year': 26, 'weight': 48.5}
# ]
#
# tpl = """
# {%- for u in user -%}
#     {%filter upper%} {{ u.name }} {%endfilter%} {%filter string %} {{u.year}} - {{u.weight}} {%endfilter%}
# {% endfor -%}
# """
# tm = Template(tpl)
# msg = tm.render(user=persons)
# print(msg)

# html = """
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
#
# {%- endmacro %}
# <p>{{ input('username')}}</p>
# <p>{{ input('email')}}</p>
# <p>{{ input('password')}}</p>
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)

# html = """
# {% macro input(name, placeholder, type='text') -%}
#     <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
#
# {%- endmacro %}
# <p>{{ input('firstname', 'Имя')}}</p>
# <p>{{ input('lastname', 'Фамилия')}}</p>
# <p>{{ input('address', 'Адрес')}}</p>
# <p>{{ input('address', 'Адрес', 'tel')}}</p>
# <p>{{ input('address', 'Адрес', 'email')}}</p>
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Николай', 'year': 20, 'weight': 58.5},
#     {'name': 'Сергей', 'year': 26, 'weight': 48.5}
# ]
# html = """
#     {% macro list_users(list_of_user) -%}
#     <ul>
#         {% for u in list_of_user -%}
#         <li>{{ u.name }}  {{ caller(u)}}</li>
#         {% endfor %}
#     </ul>
#     {%- endmacro %}
#
#     {% call(user) list_users(users) %}
#         <ul>
#             <li>age: {{ user.year}}</li>
#             <li>weight: {{ user.weight}}</li>
#         </ul>
#     {% endcall -%}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
#
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Николай', 'year': 20, 'weight': 58.5},
#     {'name': 'Сергей', 'year': 26, 'weight': 48.5}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons)
#
# print(msg)

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Николай', 'year': 20, 'weight': 58.5},
#     {'name': 'Сергей', 'year': 26, 'weight': 48.5}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title='About Jinja')
#
# print(msg)
#
# from jinja2 import Environment, FileSystemLoader
#
# file_loader = FileSystemLoader('my_templates')
# on = Environment(loader=file_loader)
#
# tm = on.get_template('main.html')
# msg = tm.render()
#
# print(msg)

# def decrypt(encrypted_text, n):
#     if encrypted_text in ("", None):
#         return encrypted_text
#
#     ndx = len(encrypted_text) // 2
#
#     for i in range(n):
#         a = encrypted_text[:ndx]
#         b = encrypted_text[ndx:]
#         encrypted_text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
#     return encrypted_text
#
#
# def encrypt(text, n):
#     for i in range(n):
#         text = text[1::2] + text[::2]
#     return text
#
#
# print(encrypt("This is a test!", 0))
# print(encrypt("This is a test!", 3))
# print(decrypt(" Tah itse sits!", 3))

# from jinja2 import Environment, FileSystemLoader
# from jinja2 import Template
# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# text = """
# <ul>
# {% for i in menu %}
#     {% if i['href'] == '/index' -%}
#         <li><a href='{{ i['href'] }}' class='active'>{{ i['link']}}</a></li>
#     {% else %}
#         <li><a href='{{ i['href'] }}'>{{ i['link']}}</a></li>
#     {% endif %}
# {% endfor %}
# </ul>
# """
#
# tm = Template(text)
# msg = tm.render(menu=menu)
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# subs = ['Культура','Наука','Политика','Спорт']
#
# file_loader = FileSystemLoader('templates')
# on = Environment(loader=file_loader)
#
# tm = on.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)
# import openai
#
# # Replace YOUR_API_KEY with your OpenAI API key
# openai.api_key = "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"
#
#
# def cube_checker(volume, side):
#     if volume <= 0 or side <= 0:  # Проверка на недопустимые значения
#         return False
#     calculated_side = round(volume ** (1/3))  # Вычисление стороны параллелепипеда
#     return calculated_side ** 3 == volume and calculated_side == side  # Проверка на равные стороны
#
# print(cube_checker(-12,2))
# print(cube_checker(8, 3))
# print(cube_checker(-8,-2))
# print(cube_checker(0, 0))
# print(cube_checker(125, 5))
# print(cube_checker(125,-5))






