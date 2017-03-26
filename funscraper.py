import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime


def acidcow():
    r = requests.get('http://www.acidcow.com')
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    urls = soup.find_all('a', href=True)

    for link in urls:
        if link.text.find('Acid Picdump') != -1:
            picspage = link['href']

            picspage_request = requests.get(picspage)
            picspage_content = picspage_request.content
            picspage_soup = BeautifulSoup(picspage_content, 'html.parser')
            pics = picspage_soup.find_all('div', {'class': 'picture'})

            for pic in pics:
                a = pic.find_all('img')[0].get('src')
                urllib.request.urlretrieve(a, '.\\pics\\' + a.split('/')[-1])


def dilbert():
    r = requests.get('http://dilbert.com/')
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    comic = soup.find_all('img', {'class': 'img-responsive img-comic'})[0].get('src')

    urllib.request.urlretrieve(comic, '.\\pics\\' + 'dilbert-' + str(datetime.datetime.today().strftime('%Y-%m-%d')) + '.jpg')