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
    clean_text = str(text)
    while '<' in clean_text:
        clean_text = clean_text[:clean_text.find('<')] + clean_text[clean_text.find('>') + 1:]
    #while '\r\n' in c
    return clean_text

file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла

# Очищеная страница
jokes = []
for joke in fun:
    jokes.append(clean_text(joke))


file2.write(jokes[0])
file2.close()  # закрывает файл
print(jokes[0])

