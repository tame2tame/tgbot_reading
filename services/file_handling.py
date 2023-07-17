import os

BOOK_PATH = 'books/1.txt'
PAGE_SIZE = 100

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    punctuation_marks = [',', '.', '!', ':', ';', '?']
    page_text = text[start:start+page_size]

    for index, char in enumerate(reversed(page_text)):
        if char in punctuation_marks and page_text[index-2] not in punctuation_marks:
            break
    if index != 0:
        page_text = page_text[:-(index)]

    page_size = len(page_text)

    return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    text = open(path, encoding='utf8').read()
    counter = 1
    start = 0
    while start < len(text):
        text_and_size = _get_part_text(text, start, PAGE_SIZE)
        book[counter] = text_and_size[0].lstrip()
        start += text_and_size[1]
        counter += 1



# prepare_book(os.path.join(os.getcwd(), BOOK_PATH))

print(prepare_book(BOOK_PATH))