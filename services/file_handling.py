BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    signs: str = ',.!:;?'
    out_text = text[start: start+size]                             #Выделяем выходной текст по длине
    if len(text) >= start+size and text[start+size] in signs and out_text[-1] in signs:   #Определяем есть ли многоточия                                                                                                многоточие в конце текста
        while out_text[-1] in signs:                               # Если есть, обрезаем выходной текст
            out_text = out_text[:-1]
    if out_text[-1] in signs:                                      # Если текст уже кончается знаком, отправляем
        return out_text, len(out_text)
    for i in range(1, len(out_text)+1):                            # Определяем конечный индекс текста
        if out_text[-i] in signs:
            out_text = out_text[:-i + 1]
            break
    return out_text, len(out_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    start: int = 0
    page: int = 1
    with open(path) as f:
        text = f.read()
    while start < len(text):
        page_text, page_len = _get_part_text(text, start, PAGE_SIZE)
        start += page_len
        book[page] = page_text.lstrip()
        page += 1

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
