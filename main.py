# pythonProject2

# Парсим анекдоты с сайта
# Видео в You Tube от Хауди-Хо "Парсинг в Python за 10 минут!"
# Парсит анекдоты со страницы и выводит в виде списка строк
# Парсит несколько страниц

import requests
from bs4 import BeautifulSoup as BS
from config import site_adress, sel

# парсим первые 20 страниц
page_list = range(1, 2 + 1)
fun_list = []

for page in page_list:
    # Получаем содержимое страницы ("ее адрес") через библиотеку requests
    r = requests.get(site_adress + str(page) + '/')
    # скачанное обрабатываем через библиотеку BeautifulSoup
    html = BS(r.content, 'html.parser')

    # Скачиваем все анекдоты со страницы (с мусором)
    fun = html.select(sel)
    fun_list += fun


# чистим текст строки и формируем анекдот
def clean_text(text):
    """
    Удаляем все символы в спарсенном тексте между скобками < и >
    :param text: вводим текст
    :return: чистый текст
    """
    cl_text = str(text)
    while '<' in cl_text:
        cl_text = cl_text[:cl_text.find('<')] + cl_text[cl_text.find('>') + 1:]
    while '\r\n' in cl_text:
        cl_text = cl_text[:cl_text.find('\r')] + cl_text[cl_text.find('\n') + 1:]
    return cl_text


file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла

# Очищеная страница записывается в список 'jokes' и в текстовый файл 'secondText.txt'
jokes = []
for joke in fun_list:
    jokes.append(clean_text(joke))
    file2.write(clean_text(joke) + '\n')

file2.close()  # закрывает файл
print(jokes)
