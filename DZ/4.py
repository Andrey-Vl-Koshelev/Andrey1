import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(name):
    with open('built_in.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator='\r')
        writer.writerow(name)


name = []


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    s1 = soup.find_all('div', class_='page__content')[0]
    plugins = s1.find_all('h3')
    for plugin in plugins:
        data = plugin.find('a').get('name')
        name.append(data)
        write_csv(name)


def main():
    url = 'https://letpy.com/handbook/builtins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

# stdout:
# abs,all,any,ascii,bin,bool,bytearray,bytes,callable,chr,classmethod,compile,complex,delattr,dir,dict,divmod,enumerate,eval,exec,filter,float,format,frozenset,getattr,globals,hasattr,hash,hex,id,input,int,import,iter,isinstance,issubclass,len,list,locals,map,max,memoryview,min,next,object,open,ord,pow,property,print,range,repr,reversed,round,set,setattr,sorted,str,staticmethod,sum,super,tuple,type,vars,zip
