import json

data = {"Россия": "Москва"}


def decorator_in(func):
    def wrap(*args, filename):
        try:
            data = json.load(open(filename))
            func(*args, filename)
        except FileNotFoundError:
            data = {}

    return wrap


def decorator_too(func):
    def wrap(*args, **kwargs):
        func(*args, **kwargs)
        print('Файл сохранен')

    return wrap


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @classmethod
    @decorator_too
    @decorator_in
    def add_country(cls, new_country, new_capital, filename):
        data[new_country] = new_capital
        with open(filename, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    @decorator_too
    @decorator_in
    def delete_country(cls, del_country, filename):
        if del_country in data:
            del data[del_country]

            with open(filename, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")

    @classmethod
    @decorator_in
    def search_data(cls, country, filename):
        if country in data:
            print(f"Страна {country} столица {data[country]} есть в словаре!")
        else:
            print(f"Страна {country} отсутствует в словаре")

    @classmethod
    @decorator_too
    @decorator_in
    def change_capital(cls, country, new_value, filename):
        if country in data:
            data[country] = new_value

            with open(filename, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


index = ''
filename1 = 'list_capital.json'
with open(filename1, "w") as fw:
    json.dump(data, fw, indent=2, ensure_ascii=False)

while index != 6:
    try:
        print("*" * 40)
        index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
                          '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
                          '6 - завершение работы\nВвод: '))
        if index == 1:
            country_name = input("Введите название страны (с заглавной буквы): ")
            capital_name = input("Введите название столицы страны (с заглавной буквы): ")
            CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
        if index == 2:
            country_name = input("Введите страну для удаления (с заглавной буквы): ")
            CountryCapital.delete_country(country_name, filename='list_capital.json')
        if index == 3:
            country_name = input("Введите название страны (с заглавной буквы): ")
            CountryCapital.search_data(country_name, filename='list_capital.json')
        if index == 4:
            country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
            new_capital = input("Введите новое название столицы: ")
            CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
        if index == 5:
            CountryCapital.load_from_file('list_capital.json')
    except IndexError:
        break
