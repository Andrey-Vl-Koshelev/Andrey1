# name_new = "Elena"
# age = 20
# print('Hello ' + name_new + ". I am " + str(age))
#
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# import keyword
# print(keyword.kwlist)

# a = 5
# print(a)
# a = 6
# print(a)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка \nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки.\nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки. символов")
# print('строка \
#       символов')

# print("Документ \"script.py\" находтся \rпо заданному пути: \n\tD:\\Python\\project")

# print(type(46460))
# print(type(4.44564156))
# print(445641564454156341563416548674874896749)
# print(4.445641564454156341563416548674874896749)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 ** 2)
# print(5 % 2)

# a = 5
# b = 7
# c = 3
# s = a + b + c
# print("Сумма:", s)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", s / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 4321  # 432
# print("Исходное число:", num)
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 9573  # 432
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10  # 432
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# print(res)

# a = int(input("Введите число: "))
# # a = int(a)
# print(type(a))
# print(a * 2)

# a = 10
# b = 2
# print("a:", a)
# print("b:", b)
# a = a + b  # a = 10 + 2 = 12
# b = a - b  # b = 12 - 2 = 10
# a = a - b  # a = 12 - 10 = 2
# print("a:", a)
# print("b:", b)

# Функции преобразования типов
# int() - числовой тип
# str() - строковый тип
# float() - вещественный тип
# bool() - булевый тип

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)
# print(type(res))

# print(int(3.8))
# print(round(3.8954144165341, 5))

# print(5 / 2)

# a = '5.2'
# # b = 10
# # c = float(a) + b
# # print(c)
# # print(type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="---", end=" ")
# print("Я учу Python")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степень", power, "равно:", res)

# b1 = True
# # b2 = False
# # print(b1 + 5)
# # print(b2 + 5)
# print(type(b1))

# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(-15.2))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)
# print(type(test))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 5)
# print('привет' > 'Привет')


# print(2 < 14 < 9)
# print(2 * 5 > 7 > 4 + 3)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)


# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# # if a > b:
# #     print("a > b")
# # elif a < b:
# #     print("b > a")
# # else:
# #     print("b == a")
#
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("b == a")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# # if a == b and b == c and c == a:
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or c == a or b == c:
#     print('Треугольник равнобедренный')
# # elif not (a == b and b == c and c == a):
# # elif a != b and b != c and c != a:
# else:
#     print("Треугольник разносторнний")

# num1 = 10
# num2 = 20
# num3 = 20
# if num1 == num2 == num3:
#     print("Равносторонний")
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# m = int(input("Введите номер месяца: "))
# month = int(input('Введите номер месяца: '))
# if month == 1 or month == 2 or month == 12:
#     print('Зима')
# elif month == 3 or month == 4 or month == 5:
#     print('Весна')
# elif month == 6 or month == 7 or month == 8:
#     print('Лето')
# elif month == 9 or month == 10 or month == 11:
#     print('Осень')
# else:
#     print('Ошибка')

# month = int(input('Введите номер месяца: '))
# if 1 <= month <= 12:
#     if 3 <= month <= 5:
#         print('Весна')
#     elif 6 <= month <= 8:
#         print('Лето')
#     elif 9 <= month <= 11:
#         print('Осень')
#     else:
#         print('Зима')
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, "ворона")
#     if 2 <= n <= 4:
#         print("На ветке", n, "вороны")
#     # else:
#     if 5 <= n <= 9 or n == 0:
#         print("На ветке", n, "ворон")
# else:
#     print("Ошибка ввода данных")

# (условие ? True : False)

# a, b = 10, 20
#
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Неправильные данные")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
# # except ValueError:
# #     print("Нельзя вводить строки")
# # except ZeroDivisionError:
# #     print("Нельзя делить на ноль")
#
# print("OK!!!")

# try:
#     a = int(input('Введите первое значение: '))
#     b = int(input('Введите второе значение: '))
#     print(a + b)
# except ValueError:
#     print(str(a) + str(b))


# a = input('Введите первое число: ')
# b = input('Введите второе: ')
# try:
#     a = int(a)  # a = 2
#     b = int(b)  # b = пять
# except ValueError:
#     a = str(a)
#     b = b
# finally:
#     print(a + b)


# while условие:
#     блок инструкций

# i = 10
# while i >= 0:
#     print("i =", i)
#     i -= 1  # i = i + 1

# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1

# i = 1000
# while i >= 1:
#     print(i, end=" ")
#     i //= 10

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# n = int(input('Введите число: '))  # 1
# m = int(input('Введите число: '))  # 5
# # i = n
# res = 0
# while n <= m:
#     if n % 2:
#         res += n  # res = res + n
#         print(n, end=" ")
#     n += 1
# print("Сумма целых нечетных чисел:", res)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное челое число: "))
#     if not n < 0:
#         break
#
# print(n)
# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# n = int(input("Количество символов: "))
# sim = input("Тип символа: ")
# orient = input("0 - горизонтальная\n1 - вертикальная\nориентация линии: ")
# i = 0
# while i < n:
#     if orient == "0":
#         print(sim, end=" ")
#     elif orient == "1":
#         print(sim)
#     else:
#         print("Такой ориентации не предусмотренно")
#         break
#     i += 1

# kol = int(input("Количество чисел последовательности: "))
# i = 0

# number = int(input('Введите количество чисел последоват: '))  # 5
# i = 1
# n = float(input('Введите число: '))  # 4
# summa = n  # 4
# minim = n  # 4
# maxim = n  # 4
# while i < number:
#     n = float(input('Введите число: '))  # 2  3  6  1
#     summa += n  # summa = summa + n  4 + 2 = 6 + 3 = 9 + 6 = 15 + 1 = 16
#     if maxim < n:
#         maxim = n  # maxim = 6
#     if minim > n:
#         minim = n  # minim = 1
#     i += 1
# print('Среднее арифметическое равно:', summa / number)
# print('Минимальное число равно:', minim)
# print('Максимальное число равно:', maxim)


# i = 1
#
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in 5, 6, 7, 8, 9:
#     print(i)

# for i in 'Hello':
#     print(i)

# range(start, stop, step)
# print(range(4, 6))

# for i in range(100, 0, -10):
#     print(i, end=" ")

# a = int(input("Введите целое число: "))  # 36
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):  # 11
#     if i % 10 == i // 10:  # 1 == 1
#         print(i, end=' ')  # 11


# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника: "))  # 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = [i for i in range(6) if i % 2 == 0]
# print(n)


# n = [i * 2 for i in "Hello"]
# print(n)

# Список
# n = [5, 6, [7, 8, 9], "Hello", 5.6, True]
# print(n)
# print(type(n))
# print(n[0])
# print(n[2][0])
# print(n[3])
# print(n[3][1])
#
# print(n[-2])

# n[1] = 256
# n[3] += "100"
# n[-7] = 45
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print([5] * 6)
# print(s)
#
# b = list("Hello")
# print(b)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n is n2:
#     print('Списки равны')
# else:
#     print('Списки разные')

# [выражение for переменная in последовательность]
# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# n = 5
#
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# a = [1, 2, 3]
# b = [4]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print([int(input("-> ")) for i in range(int(input("n = ")))])

# n = [2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for elem in n:
#     print(elem, end=" ")

# n = [-3, 9, -5, -1]
# b = 0
# for i in n:
#     if i < 0:
#         b += i
#
# print(b)

# a = [int(input('Элементов списка: ')) for i in range(int(input('n = ')))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество:", k)
# print("Сумма:", s)

# a = [int(input('-> ')) for i in range(int(input('Введите кол-во элементов списка: ')))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
# print(s / k)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 9, 2, 1, 17, 25]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез
# список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])
# print(s[1:5])
# print(s[6:7])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:3] = [20]
# s[2] = 30
# s[32:] = [9, 18, 28, 38, 48]
# print(s)
#
# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец основного списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, [100, 2])  # добаляет элемент по индексу (первый параметр), с заданным значением (второй параметр)
# print(s)


# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# DZ
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
# # i = 0
#
# # while i < len(a):
# #     c.append(a[i])
# #     c.append(b[i])
# #     i += 1
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)


# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s = [5, 9, 3, 7, 1, 8]
# # s[3:] = []
# print(s)
# # s.remove(9)  # удаляет первый искомый элемент из списка по значению
# # print(s)
# # last = s.pop(-2)  # без параметров - удаляет последний элемент из списка, указанный параметр - это индекс удаляемого
# # # элемента
# # print(last)
# # print(s)
# # s.clear()  # удаляет из списка все элементы
# # print(s)
# del s[2:4]
# print(s)

# s = [int(input("-> ")) for i in range(int(input("введите ко-во элементов списка: ")))]
# # for i in range(len(s)):
# #     k = int(input('Введите индекс: '))
# #     del s[2]
# #     break
# k = int(input('Введите индекс: '))
# s.pop(k)
# print(s)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(3, 9, -1)
# print(ind)

# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# print(s)
# s.reverse()  # переворачивает список
# print(s)
# s.sort(reverse=True)  # сортирует в порядке возрастания, изменяет список, reverse=True - сортировка в порядке убывания
# print(s)
# a = sorted(s, reverse=True)  # сортирует в порядке возрастания, НЕ изменяет список
# print(a)
# print(s)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

# a = [1, 2, 3, 4, 2]
# b = [11, 12, 13]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):  # от 0 до 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # от 3 до 5
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)

# import random
#
# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
#
# print(randint(10, 15))
# print(randrange(0, 10, 2))
# import json
# import random as r

# print(r.randint(10, 15))
# print(r.randrange(10))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
#
# s = [55, 66, 77, 88, 99, 50, 20, 30, 40, 60, 70, 80, 90]
# print(r.choice(s))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
#
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)


#  Функции агрегирования

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# sum = [1, 2, 3]
# print(min(sum))
# print(sum(lst))

# x = [r.randint(0, 100) for i in range(0, 10)]
#
# print(x)
# m = max(x)
# print("Max:", m)
# x.remove(m)
# x.insert(0, m)
# print(x)


# x = [r.randint(-20, 20) for i in range(10)]
# print(x)
# x.sort(reverse=True)
# # x.reverse()
# print(x)

# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# a = min(x)
# print("min:", a)
# b = x.index(a)
# print("index:", b)
# del x[:b]
# print(x)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# #     print("Список пуст")
# if not lst:
#     print("Список пуст")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("a =", a)
# print("b =", b)
# # c = a + b
# # print("c = ", c)
#
# # c = []
# # print('Элементы обоих списков без повторений: ', c)
# # for i in a:
# #     if i not in c:
# #         c.append(i)
# # for i in b:
# #     if i not in c:
# #         c.append(i)
# # print("Элементы обоих списков без повторений", c)
#
# # c = []
# # for i in a:
# #     if i in b and i not in c:
# #         c.append(i)
# # print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()


# a = [1, 2, 3]
# print(a)
# for i in a:
#     print(i, end="\t\t")
# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# print(a)
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# m = [[r.randint(-10, 20) for x in range(8)] for y in range(4)]
#
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print(row, end="\t\t")


# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# i = 0
# while i < size:
#     j = 0
#     while j < symbol:
#         n = 0
#         while n < size:
#             m = 0
#             while m < symbol:
#                 if (i + n) % 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#                 m += 1
#             n += 1
#         print()
#         j += 1
#     i += 1

# for i in range(8):
#     for j in range(8):
#         if i >= j:
#             print("*", end="")
#     print()


# size = int(input('Введите размер поля: '))
# sumbol = int(input('Введите количество символов: '))
# for i in range(size):
#     for j in range(sumbol):
#         for k in range(size):
#             for m in range(sumbol):
#                 if (i+k) % 2 == 0:
#                     print('+', end=' ')
#                 else:
#                     print(' ', end=' ')
#         print()

# for i in range(9):
#     for j in range(9):
#         if i < j:
#             print("*", end="")
#     print()

# print('Вывести треугольник из звездочек')
# print()
#
# size = 8
# for i in range(size):
#     for j in range(size, i, -1):
#         print('*', end='')
#     print()

# n = [[r.randint(0, 4) for x in range(3)] for b in range(4)]
# m = 1
# for row in n:
#     for x in row:
#         if x > 0:
#             m *= x
#         print(x, end="\t\t")
#     print()
# print("Произведение ненулевых элементов: ", m)


# import geometry

# num1 = geometry.sqrt(16)
# num2 = geometry.ceil(3.2)
# num3 = geometry.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(geometry))
# print(geometry.pi)

# rd = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * geometry.pi * rd, 2))

import time

# seconds = time.time()
# print("Секунды с начала эпохи: ", seconds)
# locale_time = time.ctime(454646354)
# print("Местное время:", locale_time)
# res = time.localtime()
# print("Localtime:", res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(4154545347)))


# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "seconds.")

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, "seconds.")

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y."))

# Функция
# print()
#
#
# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum("abc", "def")
# get_sum(2.5, 4.3)


# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     print(a + b)
#     return a + b
#
#
# res = get_sum(1, 8)
# print(res)
# print(get_sum(2, 5))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# x = int(input("a: "))
# y = int(input("b: "))
#
#
# def rs(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(rs(x, y))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     # a, b = 0, 1
#     a = 0
#     b = 0
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(15)


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 15))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print("Количество символов слишком маленькое")
#     else:
#         print("Недопустимые символы")
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a=4, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# s = 2
# print(get_sum(c=s))

# def symbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
#
# symbol(10, "+")
# symbol(5, "*")
# symbol(15, "#")
# symbol(7)
# symbol()

# def digits_sum(n, event=True):
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
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, False))
# print(digits_sum(38271, False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#     print("*" * 20)
#
#
# display_info("Ira", 20)
# display_info(20, "Ira")
# display_info(age=23, name="Igor")
# display_info("Ira", age=23, name="Igor")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
# print(id(lt1))
# print(id(lt2))


# lt1 = 5
# lt2 = 5
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # True
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))

# s = "Hello "
# print(id(s))
# s += "World"  # s = s + "World"
# print(s)
# print(id(s))
# # s[1] = "a"
# # s[1:2] = "a"
# # s = s[:1] + s + s[2:]
# s = s[1:-1]
# print(s)
# print(id(s))

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# a = 5
# b = 5
# print(a == b)
# print(a is b)

# a = True
# b = True
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += 1
#     print("После изменения:", n, "=", id(n))
#     return n
#
#
# x = 1
# print(x, "=", id(x))
# x = add_numbers(x)
# print(x, "=", id(x))


# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += [4]
#     # n = n + [4]
#     print("После изменения:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_numbers(x)
# print(x, "=", id(x))

# типы данных:
# изменяемые: список (list)
# неизменяемые: число (int), строка (str), вещественное число (float), булевы значения (bool)

# Кортеж (tuple) – это неизменяемая структура данных, которая по своему подобию очень похожа на список.
# Кортеж – неизменяемый список. Или списки доступные только для чтения. Cостоит из элементов, разделенных запятыми и
# заключенных в круглые скобки.

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 5, 6, 7, 8)
# print(a)
# print(type(a))
# b = tuple((1, 5, 6, 7, 8))
# print(b)
# print(type(b))
# q = 1, 2, 3, "w"  # упаковка кортежа
# t = (1,)
# print(type(q))
# print(type(t))
# t1 = tuple("hello")
# print(t1)
# print(t1[1])
# print(t1[1:3])
# t1[1] = "i"

# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.insert(0, start)
#     # lst.insert(-1, end)
#     lst.append(end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# s1 = tuple(int(input("-> ")) for i in range(5))
# print(s1)

# s = input("-> ")
# print(tuple(s))

# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)
# mas = tuple(r.randint(0, 100) for i in range(10))
# print(mas)

# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # print(t3.index('l', 4))
# # if 'e' in t3:
# #     print(t3.index('e'))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = ("1", 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)
# print(type(x))
# print(type(t))

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))

# countries = (
#     ("Германия", 20.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

# Множества (set) - неупорядоченная коллекция, которая хранит только уникальные значения

# {}
# set()

# s = {4, 7, 8, 9, 4, 2, 4, 2, 4}
# print(type(s))
# print(len(s))
# print(s)

# s = set("hello")
# print(s)

# c = [1, 5, 4, 2, 2, 6, 4]
# s = set(c)
# print(s)
# c = list(s)
# print(c)
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(el):
#     # st = set(el)
#     # return st, len(st)
#
#     return set(el), len(set(el))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print("green" not in t)
# for i in t:
#     print(i)

# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else i(False) for i in последовательность}
# {i(True) if условие else i(False) for i in последовательность if условие}


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# print("Вносим изменения")
#
# print("Вносим изменения в склонированный проект")
#
# print("PyCharm")

# a = {"Tom", "Bob", "Alice"}
# a.add("Ann")
# print(a)
# # b = "Tom"
# # if b in a:
# #     a.remove(b)
# # a.discard("Tom")
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # c = b - a
# c = a ^ b
# # a |= b
# # a &= b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(max(s))
# print(min(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
#
# one = drawing ^ music
# print(one)
#
# two = drawing & music
# print(two)
#
# drawing = drawing - two
# print(drawing)

# Тип frozenset (замороженное множество)
# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# s = frozenset({"hello", "world"})
# print(s)


# Словарь dict()

# lst = ["one", "two", "three"]
# print(lst)
# print(lst[0])
# d = {"a": "one", "b": "two", "c": "three", "aa": "one"}
# print(d)
# print(d["a"])

# d = {}
# print(d)
# print(type(d))

# d = {'one': 1, 2: "two"}
# print(d)

# d = dict(short='dict', long="dictionary")
# print(d)


# users = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('ann@gmail.com', 'Ann'),
# )
# print(users)
# d_users = dict(users)
# print(d_users)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 15
# d[9] = 4**2
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# # print(d[42][1])
# # print(d[(1, 2.3)])
# #
# # print('one' in d)
# # print('two' in d)
# # key = 'one'
#
# # if key in d:
# #     del d[key]
#
# # try:
# #     del d[key]
# # except KeyError:
# #     print("Такого элемента нет в словаре")
# # print(d)
# for key in d:
#     print(key, "->", d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)
# print(len(d))

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core i5-3450', 5, 4600],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         k = int(input("Количество: "))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")

# d = {'A': 1, "B": 2, "C": 3}
# v = d["B"]
# print("B =", v)
# value = d.get("E", "False")
# d.clear()
# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
# print()
#
# d['E'] = 7
# d2['B'] = 5
#
# print("D =", d)
# print("D2 =", d2)

# d = {'A': 1, "B": 2, "C": 3}
# # a = d.items()
# # print(a)
# # b = d.keys()
# # print(b)
# # c = d.values()
# # print(c)
# # # print(d['A'] + d["B"])
#
# # for key, val in d.items():
# #     print(key, "->", val)
# # item = d.pop("B", 5)
# # print(item)
# # print(d)
# # item = d.setdefault("B", 5)
# # print(item)
# d.update([('R', 7), ('Q', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'Second': {
#         4: 'four',
#         5: 'five',
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Ann": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# data = int(input("Новое значение: "))
# sales[person][region] = data
# print(sales[person])

# data = {"два": 2, "три": 3, "один": 1, "четыре": 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)
# data["один"] = 5
# print(data)
# print(d)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
#
# a = list(b.items())
# print(a)

# a = ["one", 1, 2, 3, "two", 10, 20, 'three', 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d["one"] = []
#         s = i  # s = "one"
#     else:
#         d[s].append(i)
# print(d)

# zip()

# d = zip([12, 1, 2], ["Dec", "Jan", "Feb"])
# print(d)
# print(type(d))
# # print(dict(d))
# print(list(d))

# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# d = {k: v for k, v in zip(a, b)}
# print(d)

# a = ['a', 'b', 'c', 'd']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# q = zip(a, b, c)
# print(list(q))

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


# from geometry import pi
#
#
# def square(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         return kwargs['d1'] * kwargs['d2'] / 2
#     # if figure_type == 'square':
#     #     return kwargs['a'] ** 2
#     # if figure_type == 'trapezoid':
#     #     return 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
#     # if figure_type == 'circle':
#     #     return pi * kwargs['r'] ** 2
#     # return 'invalid data'
#
#
# print(square(figure_type='rhombus', d1=10, d2=8))
# # print(square(figure_type='square', a=5))
# # print(square(figure_type='trapezoid', a=12, b=3, h=6))
# # print(square(figure_type='circle', r=18))
# # print(square(figure_type='unknown', a=1, b=2, c=3))


# lambda (анонимные функции)

# def get_sum(x, y):
#     return x + y
#
#
# print(get_sum(1, 2))
# print(get_sum(3, 4))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 4))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func(3, 4))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())  # 6
# print(summ(10))  # 15
# print(summ(10, 20))  # 33
# print(summ(10, 20, 30))  # 60


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5, 6, 7))
# print(func1('a', 'b', 'c'))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc_'))


# def inc(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = inc(5)
# print(f(2))
#
#
# # def inc1(n):
# #     return lambda x: n + x
# #
# #
# # f1 = inc(5)
# # print(f1(2))
# #
# # inc2 = lambda n: lambda x: n + x
# #
# # f2 = inc(5)
# # print(f2(2))
#
# print((lambda n: lambda x: n + x)(5)(2))

# print((lambda n: lambda x: lambda y: y + x + n)(10)(5)(2))


# d = {'b': 10, 'a': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1], reverse=True)
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last name'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['rating'])
# print(res3)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# b = a[3](5, 3)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# print(d[3])
# d[3]()


# print((lambda a, b: a if a > b else b)(15, 4))

#  map(func, *iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# print(list(map(lambda t: t * 2, lst)))

# b = ['1', '2', '3', '4', '5']
# c = list(map(int, b))
# print(c)
# print(type(c))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: str(x) + y, num, st)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# res = filter(func => (true or false), *iterables)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s < 75, b))
# print(res)

import random

# lst = [random.randint(1, 40) for i in range(10)]
# print(lst)
#
# lst2 =
# print(lst2)

# s = [random.randrange(40) for i in range(10)]
# print(s)
# print(list(filter(lambda x: 10 <= x <= 20, s)))


#  Декораторы


# def hello():
#     return 'Hello, I am func "hello"'  # 3
#
#
# def bye():
#     return "BYE!!!"
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')  # 2
#     print(func())  # 4
#
#
# super_func(hello)  # 1
# super_func(bye)  # 1


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):  # 2
#     def func_wrapper():  # 3
#         print('Code before')  # 4
#         func()  # 5
#         print('Code after')  # 8
#     return func_wrapper  # 3
#
#
# def func_test():  # 6
#     print('func_test')  # 7
#
#
# text = my_decorator(func_test)  # 1
# text()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('func_test')
#
#
# @my_decorator
# def hello():
#     print('hello')
#
#
# func_test()
# print()
# hello()


# text = my_decorator(func_test)
# text()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# @args_decorator
# def new_func(q):
#     print(q)
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
#
# new_func("Новая функция")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сложение:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def myltiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @myltiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))

# print(int("10"))
# print(int("1010", 2))
# print(int("12", 8))
# print(int("A", 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
#
# print(e * 3)
# print(e * -3)
#
# print(e in "I am learn Python")
# print(e in "I am learn Java")

# s = "Hello"
# print(s[1])
# print(s[-5])
# # print(s[5])
# print(s[::-1])

# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)
# def changeCharToStr(s, c_old, c_new):
#     i = 0
#     s2 = ""
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, 'N', 'P')
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет")

# print('I\'m learning\nPython')
# print('C:\file.txt')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file\\'[:-1])
# print(r'C:\file' + "\\")
# print('C:\\file\\')


# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")

# import geometry
#
#
# print(f"Значение числа pi: {round(geometry.pi, 2)}")
# print(f"Значение числа pi: {geometry.pi:.3f}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")
# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = "my_doc"
# file_name = 'data.txt'
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# def square(n):
#     """Принимает число n, возращает квадрат числа n"""
#     a = 2
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# import geometry as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))


# print(ord("a"))
# print(ord("#"))
# print(ord("к"))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for meee"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(7897))
# print(chr(47))

# a = 122
# b = 97
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65


# from random import randint
#
# short = 8
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(short, longest)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learn Python."
# print(s.capitalize())  # Hello, world! i am learn python.
# print(s.lower())  # hello, world! i am learn python.
# print(s.upper())  # HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARN pYTHON.
# print(s.title())  # Hello, World! I Am Learn Python.


# s = "hello, WORLD! I am learn Python."
# print(s.count("h", 1, -4))  # количество искомых символов
# print(s.find("Python"))  # возвращает индекс первого совпадения
# print(s.find("oPython"))  # если посдстроки нет, возаращается -1

# string = "один два"
# one = string[:string.find(" ")]
# two = string[string.find(" ") + 1:]
# print(two + " " + one)

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# s = "hello, WORLD! I am learn Python."
# print(s.index("Python"))
# print(s.index("oPython"))

# s = "Дана строка сим(волов, среди которых ес)ть одна окрывающаяся"
# ind1 = s.index("(")
# ind2 = s.index(")")
# print(ind1)
# print(ind2)
#
# print(s[ind1+1:ind2])

# s = "hello, WORLD! I am learn Python."
# print(s.find("al"))
# print(s.rfind("al"))
# print(s.index("l"))
# print(s.rindex("l"))
# s = "Some content in this message has been blocked because the sender isn't in your Safe senders list"
# item = "w"
# if s.count(item) == 1:
#     print(s.find(item))
# elif s.count(item) >= 2:
#     print(s.find(item), s.rfind(item))

# s = "hello, WORLD! I am learn Python."
# print(s.endswith("on."))
# print(s.endswith("lo", 3, 5))
#
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))

# print("aab123".isalnum())  # не пустая и состоит из букв или цифр
# print("45%6".isalnum())  #
#
# print("ABCabc".isalpha())  # не пустая и содержит только буквы
# print("123abc".isalpha())
#
# print("123".isdigit())  # не пустая и содержит только цифры
# print("ывав1".isdigit())  #
#
# print('abc'.islower())  # не пустая и содержит только буквенные символы в нижнем регистре, также может сожержать
# # спецсимволы и цифры
# print('abc@98AS'.islower())
#
# print('ABC'.isupper())  # не пустая и содержит только буквенные символы в верхнем регистре, также может сожержать
# # спецсимволы и цифры
# print('ABC1^q'.isupper())

# print(' \t \n '.isspace())  # строка состоит только из пробельных символов + табуляция и перенос на другую строку
# print(' a '.isspace())

# print('py'.center(10))
# print('py'.center(11, "-"))
# print('py'.center(2))

# print("    py".lstrip())  # py
# print("py    ".rstrip())  # py
# print("      py    ".strip())  # py
#
# print("https://www.python.org/".lstrip("th/sp:"))
# print('$py.$$$;'.rstrip(';$.'))
# print('$py.$$$;'.strip(';$.'))
#
# print("https://www.python.org/".lstrip("th/sp:").rstrip("/.org"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(str1.replace("Nython", "Python", 2))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  #  a-b-c
#
# print("..".join(['1', '2']))
# print(":".join("Hello"))

# print('Строка разделенная пробелами'.split("   "))
# print('www.python.org.ru'.split(".", 1))
# print('www.python.org'.rsplit("."))
# print('www...python...org'.rsplit("."))

# a = input("-> ").split()
# print(a)
# def name(name):
#     print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#
#
# a = input("Введите ФИО: ").split()
# name(a)

# s = "В строке заменить пробелы символом"
# # lst = s.split()
# # print(lst)
# # st = "*".join(lst)
# # print(st)
#
# print(s.replace(" ", "*"))

# s = """Ежевику для ежат
# Приносили два ежа.
# Ежевику еле-еле
# Ежата возле ели съели"""
#
# up = s.count("Е")
# down = s.count(" е")
# # print(up)
# # print(down)
# e = up + down
# print("Количество слов:", e)


# Регулярные выражения
import re

# s = "Я ищу сов[паден]ия в 2021 го-да. И я из найду в 2 счёта. 45678"
# # # reg = r'[201]'
# #
# # # print(re.split(reg, s))
# # # print(re.split(reg, s, 1))
# # #
# # # print(re.sub(reg, "!", s, 1))
# # # [] - любой из символов
# # # print(re.findall(reg, s))
# #
# # # reg = r'[12][0-9][0-9][0-9]'
# # # print(re.findall(reg, s))
# #
# reg = r'[А-яё.\[\]-]'
# print(re.findall(reg, s))

# s = "Еда, беду, победа"
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта. 45678"
# reg = r'[^0-9]'
# #  [^abc] - вернет все, за исключением abc
# print(re.findall(reg, s))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T29:40. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2021 года. И \tя из найду в 2 счё_та.\n 20000045678"
# reg = r'20*'
# \d - одна цифра [0-9]
# \w - цифра, буква, символ _ [0-9А-яA-z_]
# \s - пробельный символ (включая табуляцию и перенос строки)
# \D - все кроме цифр [^0-9]
# \W - все кроме цифр, букв, символа _ [^0-9А-яA-z_]
# \S - все кроме пробельного символа (включая табуляцию и перенос строки)
# print(re.findall(reg, s))
# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - 0 или 1

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg1 = r'[+-]?[\d.]+'
# print(re.findall(reg1, d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.*", "", s))
#
# # 05.03.1987
# print("Дата рождения:", re.sub("-", ".", re.sub("#.*", "", s)))

# s = "Предложение. author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831; Предложение"
# reg = r"\w+\s*=\s*[^;]+"
# # reg = r'[^;]+'
# print(re.findall(reg, s))

# s = "12 сентября 2021 года 789"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 года. И \tя из найду в 2 счё_та"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'h+ello world'
# print(re.findall(r"\w\+", text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2021 года. И \tя из найду в 2 счё_та"
# reg = 'я'
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, flags=re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part1
# @         # @
# [a-z.-]+  # past2
# """, 'text@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python_ma5st#er'))


# greedy - захватывает максимально возможное число символов
# ? - lazy - захватывает минимально возможное число символов

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' width='100'> - фон страницы</p>"
# # reg = '<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))
#

# text = "Методы этой группы[16] выполняют[17] преобразование регистра[18][19] строки"
# print(re.findall(r'\[.*?]', text))


# s = "Петр и Виталий отлично учатся"
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"(?:int|float)\s*=\s*(\d[.\w+]*)"
# print(re.findall(reg, s))

# (?:  ...) - обозначет, что эта группирующая скобка является не сохраняющей

# s = '127.0.0.1'
# #s = '192.255.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# # reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))


# a = "31-12-2000"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, a))


# s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# # m = re.search(reg, s)
# # print(m[0])
# # print(m[1])
# # print(m[2])
# # print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))

# text = """
# Самара
# Москва
# Сочи
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select>")
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))
# print("</select>")


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*(src=)(?P<q>[\'"])(.+)(?P=q)>'
# # (?P<name>)  (?P=name)
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.findall(reg, s))
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "google.com and google.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))

# def validate_phone(name):
#     reg = r"^\+?7[ (]*\d+[ )]*[\d -]{8,10}$"
#     return re.search(reg, name).group()
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))


# Рекурсия

# def elevator(n):   # n - номер этажа
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)  # 5 4 3 2 1
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)

# 1
# 2
# 3
# 4
# 5

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res  # 25
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:  # базовый случай (условие выхода)
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 3 5 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 15
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 15
#
#
# print(to_str(255, 16))  # FF


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
# # print(names[0])
# # print(isinstance(names[0], list))  # False
# # print(names[1])
# # print(isinstance(names[1], list))  # True
# # print(names[1][1])
# # print(isinstance(names[1][1], list))  # True
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))  # False
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
#
# def func(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
#
# print(func(names))

# def remove(text):
#     if not text:  # ""
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == 'l':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # HelloWorld
#
#
# print(remove(" Hello\tWorld "))

# Файлы

# 1. Открытие файла
# 2. Выполнение операции с файлом (запись, чтение)
# 3. Закрытие файла

# f = open(r'D:\Python225\text.txt', 'r')
#
# # print(f.read(3))
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
#
# # print(f.readlines(26))
# for line in f:
#     print(line)
#
# f.close()

# f = open(r'text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open("file.txt")
# print(len(f.readlines()))

# cnt = 0
# for line in f:
#     cnt += 1

# cnt = 0
# s = f.readline()
# while s != "":
#     s = f.readline()
#     cnt += 1
#
# print(cnt)
# f.close()

# f = open('xyz.txt', 'a')
# # f.write('Hello \nWorld')
# # print(f.write('\nNew text'))
# lines = ['This is line 1', 'This is line 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# # print(lst)  # ['10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211', '1312', '1413', '1514', '1615', '1716', '1817', '1918']
# for index in lst:
#     f.write(index + "\t")
#
# f.close()

# my_file = open("text3.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файл;")
# my_file.close()
#
# my_file = open("text3.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos <= len(read_file):
#     del read_file[pos]
# else:
#     print("Индекс введен неверно!")
# print(read_file)
# my_file.close()
#
# my_file = open("text3.txt", "w")
# my_file.writelines(read_file)
# my_file.close()


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# print(f.write("-PYTHON-"))
# print(f.tell())
# f.close()

# with open("text.txt", 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done!')


# file_name = "res.txt"
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# num_list = list(map(float, nums.split()))
# print(num_list)
# print(len(num_list))

# with open("test.txt", "r") as f:
#     w = f.read().split()
#     print(w)
#     max_length = len(max(w, key=len))
#     # max_length = max(len(word) for word in w)
#     print(max_length)
#     res = [word for word in w if len(word) == max_length]
#     print(res)

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
#
# with open(write_file, 'r') as fw:
#     for line in fw:
#         print(line, end="")

# f = open("test.txt")
# line = 0
#
# for i in f:
#     line += 1
#     word = 0
#     flag = 0
#     for j in i:
#         if j != " " and flag == 0:
#             word += 1
#             flag = 1
#         elif j == " ":
#             flag = 0
#     print(i, len(i), "символов", word, "сл.")
#
# print(line, "строки")
# f.close()

# Модуль os и os.path

import os

# import os.path

# print("Текущая директория:", os.getcwd())
# print(os.listdir())  # вернулся список файлов и папок, находящихся в текущей директории (по умолчанию) или в
# # директории по указанному пути
# print(os.listdir(".."))

# os.mkdir("folder")  # создает директорию по указанному пути

# os.makedirs("nested1/nested2/nested3")  # создание вложенных папок
# os.makedirs("nested1/nested2/nested4")  # создание вложенных папок

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименование папки (файла)

# os.rename("test.txt", "test/test1.txt")

# os.renames('text.txt', "text/text1.txt")

# os.rmdir("text")  # удаление пустой папки

# for root, dirs, files in os.walk("test", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
#
# remove_empty_dirs('test')


# print(os.path.split(r"D:\Python225\test\nested2\nested3\1.txt"))  # разбивает путь на кортеж (head, tail)
#
# print(os.path.dirname(r"D:\Python225\test\nested2\nested3\1.txt"))
# print(os.path.basename(r"D:\Python225\test\nested2\nested3\1.txt"))

# print(os.path.join("D:\Python225", "test", "nested2", "nested3", "1.txt"))

# dirs = ['Work/F1', 'Work/F2/F21']
# # for dir in dirs:
# #     os.makedirs(dir)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work\\F2\\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Некоторый текст в файле {file}.")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)


# print(os.path.exists(r"D:\Python225\test\nested2\nested3\1.txt"))  # проверка не существование файла по заданному пути
# path = 'file.txt'
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу (в секундах)
# print(os.path.getmtime(path))  # возвращает время последнего изменения к файлу (в секундах)
# print(os.path.getctime(path))  # возвращает время создания файла (в секундах)
# print(os.path.getsize(path))  # возвращает размер файла (в байтах)

# import time
#
# path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\plugins\python-ce\helpers\typeshed\stdlib\typing.pyi"
#
# size = os.path.getsize(path)
# k_size = size // 1024
# print("Размер", k_size, "KB")
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))

# print(os.path.isfile(r'C:\Program Files\JetBrains\PyCharm Community Edition '
#                      r'2021.1.2\plugins\python-ce\helpers\typeshed\stdlib\typing.pyi'))
# print(os.path.isdir(r'C:\Program Files\JetBrains\PyCharm Community Edition '
#                      r'2021.1.2\plugins\python-ce\helpers\typeshed\stdlib'))

# ООП (объектно-ориентированное программирование)
# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_coords()
# Point.set_coords(p1)
# # Point.x = 100
# # print(type(p1))
# # print(p1.x, p1.y)
# # print(id(p1))
# # print(id(Point))
# # print(p1.__dict__)
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
#
# p2 = Point()
# p2.set_coords()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)
#
# Point.set_coords(p2, 2, 7)
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Валерия")
# print(h1.get_name())
# h1.set_birthday("12.04.2021")
# print(h1.get_birthday())


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# print(getattr(p1, "x"))
# # print(p1.z)
# print(getattr(p1, "z", "Нет атрибута"))
# print(hasattr(p1, "z"))
# print(hasattr(p1, "y"))
# # p1.z = 7
# setattr(p1, "z", 7)
# # setattr(Point, "z", 7)
# delattr(p1, 'z')
# print(p1.__dict__)

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dilgih")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("This is constructor!")
#     #     return super().__new__(cls)
#
#     def __init__(self):
#         print("This is initializator!")
#
#
# p1 = Point()


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра: " + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1
# print(p1.x)


# class Point:
#     count = 0  # статические свойства
#
#     def __init__(self, x=0, y=0):  # динамические свойства
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(25, 30)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним.")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('С-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot('R-4PO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(q):
#         if isinstance(q, int) or isinstance(q, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(1, 2)
# print(p1.get_coords())
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
#
# p1.set_x(8)
# print(p1.get_x())
# p1.set_y(13)
# print(p1.get_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)

# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = "Некорректные данные"
#         self.__year = self.__power = self.__power = 0
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_str(model):
#             self.__model = model
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print("Данные должны быть числом")
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print("Данные должны быть строкой")
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
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"""Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производитель: {self.__model}
# Мощность двигателя: {self.__power} л.с.
# Цвет машины: {self.__color}
# Цена: {self.__price}
# """)
#
#
# c1 = Car('X7 M50i', "2021", 'BMW', 530, 'white', 10790000)
# c1.print_info()
# c1.set_name('X2')
# print(c1.get_name())
# c1.print_info()


# from geometry import sqrt
#
#
# class Rectangle:
#     def __init__(self, l=0, w=0):
#         self.__l = l
#         self.__w = w
#
#     def get_l(self):
#         return self.__l
#
#     def get_w(self):
#         return self.__w
#
#     def get_rectangle_area(self):
#         res = self.__l * self.__w
#         print("Площадь прямоугольника:", res)
#
#     def square(self):
#         res1 = (self.__l + self.__w) * 2
#         print("Периметр прямоугольника:", res1)
#
#     def hypotenuse(self):
#         res2 = sqrt(self.__l ** 2 + self.__w ** 2)
#         print("Гипотенуза прямоугольника:", round(res2, 2))
#
#     def figur(self):
#         # for i in range(self.__l):
#         #     for j in range(self.__w):
#         #         print('*', end='')
#         #     print()
#         print(("*" * self.__w + "\n") * self.__l)
#
#
# p = Rectangle(3, 9)
# print("Длина прямоугольника", p.get_l())
# print("Ширина прямоугольника", p.get_w())
# p.get_rectangle_area()
# p.square()
# p.hypotenuse()
# p.figur()


# class Point:
#     __slots__ = ['x', 'y', 'z']
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 2
# print(p1.z)
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coord_x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 7
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coord_x(self):  # __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):  # __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @coord_x.deleter
#     def coord_x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x
#
#     # coord_x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 7
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
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
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# p1.old = 31
# print(p1.old)
# del p1.old
# print(p1.__dict__)


# class Point:
#     __count = 0  # статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print("p1 =", Point.get_count())
# p2 = Point()
# print("p2 =", Point.get_count())
# p3 = Point()
# print("p3 =", p1.get_count())


# class Point:
#     __count = 0  # статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# print("p1 =", Point.get_count())
# p2 = Point()
# print("p2 =", Point.get_count())
# p3 = Point()
# print("p3 =", p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <= 3999
#
#
# dates = [
#     '30.12.2020',
#     '30.12.2020',
#     '31.01.2021',
#     '12.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)  # '30.12.2020'
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Некорректная дата")


# d1 = Date.from_string('12.11.2022')
# print(d1.string_to_db())
#
# d2 = Date.from_string('30.04.2021')
# print(d2.string_to_db())

# string_date = '12.11.2022'
# d, m, y = map(int, string_date.split('.'))
# date1 = Date(d, m, y)
# print(date1.string_to_db())


# class Weight:
#     def __init__(self, k=0):
#         self.__k = k
#
#     @property
#     def kg_k(self):
#         return self.__k
#
#     @kg_k.setter
#     def kg_k(self, k):
#         if isinstance(k, (int, float)):
#             self.__k = k
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return round(self.__k * 2.205, 2)
#
#
# w1 = Weight(12)
# print(w1.kg_k, "кг => ", end="")
# print(w1.to_pounds(), 'фунтов')
#
# w1.kg_k = 41.3
# print(w1.kg_k, "кг => ", end="")
# print(w1.to_pounds(), 'фунтов')
#
# w1.kg_k = 20
# print(w1.kg_k, "кг => ", end="")
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
#         print(f'Счет #{self.num} принадлежит {self.surname} был открыт.')
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
#         print(f'Информация о счете:')
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
#         if val > self.value:
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
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         # print(s)
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
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
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
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
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = 'Соболев Игорь Николаевич'
# print(p1.fio)
# p1.old = 35
# p1.password = '4567 123456'
# p1.weight = 70.0
# print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         super().__init__(*args)
#         self.__width = 5
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}')
#
#
# class Rect(Prop):
#
#     def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self.background = bg
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.background}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 3)
# line.draw_line()
# print(line.__dict__)
# # print(line._width)
# # print(type(line))
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# # print(issubclass(Point, object))
# # print(line.__dict__)


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
#             self.__width = 1
#             # raise ValueError
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
#         print(f"Площадь {self.color} прямоугольника: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# # rect.width = -5
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect.color)
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
#
# class Rect(Prop):
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.2, 20), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()


# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         super().__init__(w, h)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.fon}')
#
#
# class RectBorder(Rect):
#     pass
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
#
# shape2 = RectBorder(600, 300, '1px solid red')
# shape2.show_rect()


# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник\nШирина: {self.width}\nВысота {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         super().__init__(w, h)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.fon}')
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, b):
#         super().__init__(w, h)
#         self.border = b
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.border}')
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
#
# shape1 = RectBorder(600, 300, "1px solid red")
# shape1.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3, 4, 5])
# print(v)
# print(type(v))
# q = Vector([5, 7, 3, 4, 5])
# print(q)

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
#
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
#
# line.set_coords(Point(-10, -20))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#     def draw(self):  # абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#
#     def draw(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     pass
#     # def draw(self) -> None:
#     #     print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Ellipse(Prop):
#
#     def draw(self) -> None:
#         print(f'Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# import geometry
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
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(geometry.pi * self._radius ** 2, 2)
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


# from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()


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
#         print(self.value, end=" ")
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
#
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# print('*' * 30)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')


# Интерфейс
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("display1()")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("display2()")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()


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
#         print(f'Объем {m} кг {self.name} равен {v} m^3')
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')
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


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я метод внешнего класса")
#
#     def outer_obj_method(self):
#         print('Обычный метод')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я метод внутреннего класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner("внутренний", out)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print(f"Name: {self.name}")
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print(f"Name: {self.name}")
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# print(g.name)


# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List:")
#         print(f'Name: {self.name}')
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Class Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Class Inner")
#
#         class InnerClass:
#
#             def show(self):
#                 print("Class InnerClass")
#
#
# outer = Outer()
# outer.show()
# # inner1 = outer.inner
# # inner1.show()
# inner2 = outer.inner.inner_inner
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# # comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# # print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("Базовый класс")
#
#     class Inner:
#         def display1(self):
#             print("Вложенный класс в базовый")
#
#
# class Sub_class(Base):
#     def __init__(self):
#         print("Дочерний класс")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Вложенный класс в дочерний")
#
#
# a = Sub_class()
# a.display()
#
# # b = a.db
# b = Sub_class.Inner()
# b.display1()
# b.display2()

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# b = Dog("Buddy")
# b.sleep()
# b.play()
# b.bark()


# class A:
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#     # def hi(self):
#     #     print("A")
#     pass
#
#
# class AA:
#     # def __init__(self):
#     #     print("Инициализатор класса АA")
#     def hi(self):
#         print("AA")
#
#
# class B(A):
#     # def __init__(self):
#     #     # super().__init__()
#     #     print("Инициализатор класса B")
#     # def hi(self):
#     #     print("B")
#     pass
#
#
# class C(AA):
#     # def __init__(self):
#     #     # super().__init__()
#     #     print("Инициализатор класса C")
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print("Инициализатор класса D")
#     # def hi(self):
#     #     print("D")
#     pass
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)
# d.hi()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(f' => {self.brand}, {self.cpu}, {self.ram}')
#
#
# s1 = Student('Roman')
# s2 = Student('Vladimir')
# s1.show()
# s2.show()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1, *args):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#         super().__init__(*args)
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Styles, Pos):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line('green', 5, Point(10, 10), Point(100, 100))
# l1.draw()
# print(Line.__mro__)

#  Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubclass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubclass()
# subclass.display("Эта строка будет отображаться и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Инициализатор Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар было продан в 00:00 часов")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()
# print(Notebook.__mro__)


# Перегрузка операторов

# 24*60*60 = 86400 (число секунд в одном дне)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.__DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def get_format_time(self):
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом ")
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 12
# c1["min"] = 20
# c1["sec"] = 130
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())
# c2 = Clock(50)
# print(c2.get_format_time())
# c1 += c2
# print(c1.get_format_time())
# c4 = Clock(300)
# print(c4.get_format_time())
# c3 = c4 % c2
# print(c3.get_format_time())
# if c2 < c1:
#     print("Время второе меньше")
# if c1 != c2:
#     print("Время не равно")


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}, {self.__z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
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
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("Ни одна из координат второго операнда не должна быть равна 0")
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
#             raise ValueError("Ключ должен быть строкой")
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print("Неверно задан ключ")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print("Координаты должны быть числами")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки: ", pt1)
# print("Координаты 2-й точки: ", pt2)
#
# pt3 = pt1 + pt2
# print(f"Сложение координат: ({pt3})")
#
# pt4 = pt1 - pt2
# print(f"Разность координат: ({pt4})")
#
# pt5 = pt1 * pt2
# print(f"Произведение координат: ({pt5})")
#
# pt6 = pt1 / pt2
# print(f"Частное координат: ({pt6})")
#
# print(f"Равенство координат: {pt1 == pt2}")
#
# print("x =", pt1['x'], "x1 =", pt2['x'])
# print("y =", pt1['y'], "y1 =", pt2['y'])
# print("z =", pt1['z'], "z1 =", pt2['z'])
#
# pt1['x'] = 20
# print("Запись значения в координату x:", pt1['x'])


# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
# if isinstance(g, Rectangle):
#     print(g.get_per_rect())
# else:
#     print(g.get_per_sq())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  #  "Python" + "35" = "Python35"
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))


# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]


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
# cat = Cat('Пушок', 2.5)
# dog = Dog('Мухтар', 4)
# # s = [cat, dog]
# for i in (cat, dog):
#     print(i.info(), '\n', i.make_sound())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(5, 7, 9)
# print(len(p))


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# # pt.z = 5
# # print(pt.__dict__)
# pt.length = 10
# print(pt.x, pt.y, pt.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(10, 20)
# pt2 = Point2D(10, 20)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt2 = Point3D(10, 20, 30)
# # pt2.z = 30
# print(pt2.x, pt2.y, pt2.z)
# # print(pt2.__dict__)


# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         # return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1("  ?Hello World!   "))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_string("?:!.; ")
# print(s2("  ?Hello World!   "))


# Класс как декоратор

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Перед вызовом функции")
#         self.func()
#         print('После вызова функции')
#
#
# @MyDecorator
# def func1():
#     print("func")
#
#
# func1()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         st1 = "Перед вызовом функции \n"
#         st2 = '\nПосле вызова функции'
#         res = st1 + str(self.func(a, b)) + st2
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b


# print(func1(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
#
# @Power
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         st1 = "Перед вызовом функции \n"
#         st2 = '\nПосле вызова функции'
#         res = st1 + str(self.func(*args, **kwargs)) + st2
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func3(a, b, c):
#     return a + b + c
#
#
# print(func1(2, 5))
# print(func2(2, 5, 2))
# print(func3(2, 5, 2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("Перед вызовом функции")
#             print(self.name)
#             func(a, b)
#             print('После вызова функции')
#
#         return wrap
#
#
# @MyDecorator("test2")
# def add(a, b):
#     print(a, b)
#
#
# add(2, 5)


# class Power:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.n
#
#         return wrap
#
#
# @Power(2)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# Декораторы классов
# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Инициализатор ActualClass')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(5))


# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         self.__value = value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, value):
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__surname
#
# @surname.setter
# def surname(self, value):
#     self.__surname = value


# p = Person("Ivan", "Petrov")
# print(p.name.get())
# p.name.set("Vadim")
# print(p.name.get())

# Дескрипторы (__get__, __set__, __delete__, __set_name__)


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)
#
# p.name = "Vadim"
# print(p.name)


# import geometry
# from abc import ABC, abstractmethod
#
#
# class Share(ABC):
#     def __init__(self, color):
#         # self.perimeter = perimeter
#         # self.square = square
#         # self.info_fig = []
#         self.color = color
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Square(Share):
#     def __init__(self, w, color):
#         self.w = w
#         # self.h = h
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = self.w * 4
#         return perimeter
#
#     def square(self):
#         return self.w * self.w
#
#     def draw(self):
#         return ('*' * self.w + '\n') * self.w
#
#     def info(self):
#         print(f"===Квадрат===\nСторона: {self.w}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр:"
#               f" {self.perimeter()}\n{self.draw()} ")
#
#
# class Rectangle(Share):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         perimeter = self.w * 2 + self.h * 2
#         return perimeter
#
#     def square(self):
#         return self.w * self.h
#
#     def draw(self):
#         print(('*' * self.h + '\n') * self.w)
#
#
# class Triangle(Share):
#     def __init__(self, w, h, l):
#         self.w = w
#         self.h = h
#         self.l = l
#
#     def perimeter(self):
#         perimeter = (self.w + self.h + self.l) / 2
#         return perimeter
#
#     def square(self):
#         return self.w / 4 * geometry.sqrt(4 * self.h ** 2 - self.w ** 2)
#
#     def draw(self):
#         rows = []
#         for n in range(self.h):
#             rows.append(" " * n + "*" * (self.w - 2 * n) + " " * n)
#         print("\n".join(reversed(rows)))
#
#
# s = Square(3, 'red')
# s.info()
# print(f"===Квадрат===\nСторона: 3\nЦвет: red\nПлощадь: {s.square()}\nПериметр: {s.perimeter()} ")
# s.draw()
# r = Rectangle(3, 7)
# print(f"===Квадрат===\nДлина: 3\nШирина: 7\nЦвет: green\nПлощадь: {r.square()}\nПериметр: {r.perimeter()}")
# # r.draw()
# t = Triangle(11, 6, 6)
# print(
#     f"===Треугольник===\nСторона 1: 11\nСторона 2: 6\nСторона 3: 6\nЦвет: yellow\nПлощадь: {t.square():.2f}\nПериметр: {t.perimeter()}")
# t.draw()

# for i in range(s):
#     for j in range(i):
#         print("*", end="")
#     print()
# a = (s, r, t)
# for i in a:
#     print(i.perimeter())
#     print(i.square())
#     i.draw()


# class OldOrder:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value <= 0:
#             raise ValueError(f"{self.__name} число должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = OldOrder()
#     amount = OldOrder()
#
#     def __init__(self, name, price, amount):
#         self.name = name
#         self.price = price
#         self.amount = amount
#
#     def sum(self):
#         return self.price * self.amount
#
#
# o = Order('apple', 5, 10)
# print(o.sum())


# Виды дискрипторов:
# non-data descriptors (дескриптор не данных) - дескрипторы, которые определили
# только __get__. Они только отдают значение, нельзя ничего сохранить. Например:
# staticmethod(), classmethod()
# • data descriptor (дескриптор данных) - если объект определяет сразу и __get__,
# и __set__ и другие. Например: property()

# class Integer:
#     @classmethod
#     def verify_coords(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coords(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3d:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3d(1, 2, 3)
# print(p1.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst[0] = 3
# print(lst, lst.get_length())

# type(
# имя класса
# кортеж родительских классов
# словарь, содержащий атрибуты и их значения
# )


# class MyMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         print('Создание нового объекта', args[0])
#         return super(MyMetaClass, cls).__new__(cls, *args, **kwargs)
#
#     def __init__(cls, *args, **kwargs):
#         print('Инициализация класса', args[0])
#         super(MyMetaClass, cls).__init__(*args, **kwargs)
#
#
# class Student(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print('Имя студента: ', stud.get_name())
# print('Тип объекта Student:', type(stud))
# print('Тип класса Student:', type(Student))


# Создание модулей

# import geometry
#
# print(geometry.pi)

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian
# import geometry

# from geometry import *

# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())

# class Integer:
#     @classmethod
#     def verify(cls, coord):
#         if not isinstance(coord, int) or coord <= 0:
#             raise TypeError(f"Координата {coord} должна быть положительным целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify(value)
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     __a = Integer()
#     b = Integer()
#     c = Integer()
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.b = b
#         self.c = c
#
#     def existence(self):
#         if (self.__a + self.b > self.c) and (self.__a + self.c > self.b) and (self.b + self.c > self.__a):
#             return "существует"
#         else:
#             return "не существует"
#
#     def info(self):
#         print(f"Треугольник со сторонами ({self.__a}, {self.b}, {self.c}) {self.existence()}")
#
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
#
# tr = [t1, t2, t3]
# for i in tr:
#     i.info()
# t1.info()
# t2.info()
# t3.info()


# from car import electrocar
#
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()


# from shapes import rectangle, circle, cylinder
#
# circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
# rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
# cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
#
# circle_max_s = max(circles, key=lambda c: c.get_circle_area())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimetr())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinder_v_avr = sum(cylinders_v) / len(cylinders_v)
# print(f"Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}")
# print(f'Прямоугольник с наименьшим периметром: {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
# print(f"Средний объем цилиндров: {round(cylinder_v_avr, 2)}")


# Упаковка данных
# Сериализация
# Десериализация

# В стандартной библиотеке Python
# marshal (.pyc)
# pickle
# json

import pickle

# filename = "basket.txt"
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 100
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
#
# with open(filename, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     dct = {'first': "a", 'second': 2, 'third': [1, 2, 3]}
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.dct}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
#
# d_save = pickle.dumps(obj)
# print(f"Сереализация в строку:\n{d_save}\n")
#
# d_read = pickle.loads(d_save)
# print(f"Десереализация в строку:\n{d_read}\n")

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)   # __getstate__
# item3 = pickle.loads(item2)  # __setstate__
#
# print(item3.__dict__)
# print(item3)

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.read_line())
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())
# print(new_reader.read_line())

# import json

# data = {
#     'first_name': 'Jane',  # fgdfg
#     ('second_name', 'surname'): ('Sergeevna', 'Doe'),
#     'hobbies': ('running', 'sky diving', 'singing'),
#     'age': 35,
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         },
#         {
#             'first_name': 'Bob',
#             'age': 8
#         },
#     ],
# }
# print(data)
# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)

# with open('data_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
#
# data = json.loads(json_string)
# print(data)

# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))
# print(json.dumps(y, ensure_ascii=False))

# import json
#
#
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
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
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     # data.append(person_dict)
#     data[num] = person_dict
#
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
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
#             a += str(i) + ", "
#         return f"Студент: {self.name} {a[:-2]}"
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
#
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
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
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
#         with open(file, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# # Student.load_from_file('student.json')
#
# # Student.dump_to_json(st1, 'student.json')
# # Student.dump_to_json(st3, 'student.json')
# my_group = Group(sts, "ГК Python")
# print(my_group)
# # my_group.add_student(st3)
# # print(my_group)
# # my_group.remove_student(1)
# # print(my_group)
# #
# group22 = [st3]
# my_group2 = Group(group22, "ГК Web")
# print(my_group2)
# #
# # Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print(my_group2)
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())
# # Group.dump_group('group.json', my_group2)
# Group.upload_group('group.json')


# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_file.json', 'w') as data_file:
#     filtered_todos = list(filter(keep, todos))
#     # print(filtered_todos)
#     json.dump(filtered_todos, data_file, indent=2)
#
#
# with open('filtered_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)


import csv

# with open("data.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open("data.csv") as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_new.csv') as f:
#     print(f.read())


# with open('student1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})

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
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=";", lineterminator='\r')
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name")
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_='links')
# row = soup.find("div", {"class": "name"})
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", text="Alena").parent
# row = soup.find("div", text="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all('div', class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

# from bs4 import BeautifulSoup
# import requests
# import re
# import csv

# req = requests.get("https://ru.wordpress.org/")
# # req.encoding = 'utf-8'
# print(req.text)

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title")
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a")['href']
#         url = plugin.find("h3").find("a").get('href')
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#     # return len(plugins)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import json
#
# data = {"Россия": "Москва"}
#
#
# def load_data(func):
#     def wrap(*args, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         func(*args, filename)
#         print("Файл сохранен")
#     return wrap
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     @load_data
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     @load_data
#     def delete_country(cls, del_country, filename):
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     @load_data
#     def search_data(cls, country, filename):
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     @load_data
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break


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
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'],
#                         data['url'],
#                         data['snippet'],
#                         data['active_install'],
#                         data['tested']))
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find("a").get('href')
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active_install': active,
#             'tested': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(12, 13):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parse import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import socket
# from view import index
#
# URLS = {
#     "/": index,
#     "/blog": "blog page"
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]  # GET
#     url = parsed[1]  # / или /blog
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
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
#     return URLS[url]
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

# import sqlite3 as sq
#
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# summa REAL,
# date TEXT
# )""")


# import sqlite3 as sq
#
#
# with sq.connect("users.db") as con:
#     cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT '+79090000000',
# age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )
# """)
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)
# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address TEXT;
# """)

# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# """)

# cur.execute("""
# DROP TABLE person_table;
# """)


# import sqlite3 as sq
#
#
# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT '+79090000000',
#     age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )
#     """)
#     cur.execute("""
#         INSERT INTO person(email, name, age)
#         VALUES ('igor@gmail.com', 'Игор', 20)
#         """)
# cur.execute("""
# INSERT INTO person
# VALUES (1, 'Ирина', '+75052031166', 23, 'irina@gmail.com')
# """)


# import sqlite3 as sq
#
# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)
#
#     res = cur.fetchone()
#     res2 = cur.fetchmany(2)
#     print(res)
#     print(res2)
# res = cur.fetchall()
# print(res)
# for res in cur:
#     print(res)

# import sqlite3 as sq

# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars (
#             cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#         UPDATE cars2 SET price = price + 100;
#         """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audy', 52000)")

# con.commit() - сохраняет все изменения в базу данных
# con.close() - закрывает соединение с БД


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # lastrowid - возвращает id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))


# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
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
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     # print(con.row_factory)
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))

# cur.execute("SELECT model, price FROM cars")

# rows = cur.fetchall()
# rows = cur.fetchone()
# rows = cur.fetchmany(5)
# for res in cur:
#     print(res['model'], "-", res['price'])


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# with open("sql_dump.sql", "w") as f:
#     for sql in con.iterdump():
#         f.write(sql)


# import sqlite3 as sq
#
# data = [('car', "машина"), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]
#
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     ru TEXT
#     )""")
#
#     cur.executemany("INSERT INTO dict VALUES (?, ?)", data)
#
#     cur.execute("SELECT ru FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())


# import os
#
# from models.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
