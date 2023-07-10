import requests as requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://knijky.ru/'


# ------------------------------------------------------------------------------- #
def find_book(book_name: str):
    session = requests.Session()

    s = {}  # Название: Автор, Жанры, Читали_страницы
    headers = {"user-agent": UserAgent().chrome, "Accept-Language": "ru"}
    r = session.get(url=url, headers=headers)
    if r:
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.find_all('div', attrs={'class': "views-field views-field-title"})
        # for i in range(len(text)): ...
    else:
        print('error')


def take_text_from_page(page: int):
    session = requests.Session()

    if page == 1:
        url = 'https://knijky.ru/books/dezertir'
        div = 'p'
    else:
        url = f'https://knijky.ru/books/dezertir?page={page - 1}'
        div = 'td'

    headers = {"user-agent": UserAgent().chrome, "Accept-Language": "ru"}
    r = session.get(url=url, headers=headers)

    if r:
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.find(f'{div}')
        # text2 = soup.find('div', attrs={'class': 'title', 'id': 'h1'})

        print(text)
    else:
        print(print('error'))


# -------------------------------------------------------------------------------#

