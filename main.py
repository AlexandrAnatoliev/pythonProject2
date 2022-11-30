# pythonProject2

# Парсим анекдоты с сайта
# Видео в You Tube от Хауди-Хо "Парсинг в Python за 10 минут!"
# Парсит анекдоты со страницы и выводит в виде списка строк

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://anekdoty.ru/samye-smeshnye/")
html = BS(r.content, 'html.parser')

# Скачиваем все анекдоты со страницы (с мусором)
fun = html.select(" div > div.holder-body > p")


# чистим текст строки и формируем анекдот
def clean_text(text):
    """
    Удаляем все символы в спарсенном тексте между скобками < и >
    :param text: вводим текст
    :return: чистый текст
    """
    crean_text = str(text)
    while '<' in crean_text:
        crean_text = crean_text[:crean_text.find('<')] + crean_text[crean_text.find('>') + 1:]
    return crean_text


# Очищеная страница
jokes = []
for joke in fun:
    jokes.append(clean_text(joke))

print(jokes)

