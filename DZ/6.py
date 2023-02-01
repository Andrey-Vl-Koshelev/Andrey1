from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('plugins2.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['name'],
                         data['urs'],
                         data['snippet'],
                         data['active']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('main', class_='site-main col-9')
    # print(elements)
    for i in elements:
        try:
            name = i.find('h2').text
        except ValueError:
            name = ''
        try:
            urs = i.find('h2').find('a').get('href')
        except ValueError:
            urs = ''

        try:
            snippet = i.find('div', class_='entry-meta').text.split()
        except ValueError:
            snippet = ''

        try:
            active = i.find('span', class_='posted-on')
        except ValueError:
            active = ''

        data = {
            'name': name,
            'urs': urs,
            'snippet': snippet,
            'active': active
        }
        write_csv(data)


def main():
    for i in range(1, 4):
        url = f"https://ru.wordpress.org/news/page/{i}/"
        get_data(get_html(url))


if __name__ == '__main__':
    main()
