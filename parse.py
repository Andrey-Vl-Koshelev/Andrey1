from bs4 import BeautifulSoup
import requests


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        r = requests.get(self.url).text
        self.html = BeautifulSoup(r, 'lxml')

    def parsing(self):
        news = self.html.find_all('div', class_='caption')
        for i in news:
            title = i.find('h3').text
            href = i.find('a').get('href')
            avtor = i.find('a', class_="topic-info-author-link").text.strip()
            self.res.append({'title': title, 'href': href, 'avtor': avtor})
        # print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            n = 1
            for i in self.res:
                f.write(f'Новость № {n}\n\nНазвание: {i["title"]}\n'f'Ссылка: {i["href"]}\nАвтор:{i["avtor"]}'f'\n\n{"*" * 20}\n')
            print(f)

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
