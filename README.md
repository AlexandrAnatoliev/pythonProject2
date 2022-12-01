# parser 1

[Ru] Парсер анекдоты с сайта

## Описание:

Парсит анекдоты со страницы и выводит в виде списка строк. Видео в You Tube от Хауди-Хо "Парсинг в Python за 10 минут!"

## Требования

* Установить внешние зависимости
* $ pip install -r requirements.txt

## Подключаем модули

```python
import requests
from bs4 import BeautifulSoup as BS
```

## Примеры использования

#### Пишем адрес сайта

```python
r = requests.get("https://anekdoty.ru/samye-smeshnye/")
```

#### Ищем на странице нужный селектор и вписываем

```python
fun = html.select(" div > div.holder-body > p")
```

#### Чистим содержимое от лишнего

```python
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
```

#### Записываем спарсенные шутки в тестовый файл. Каждая шутка - с новой строки

"Название текста", w - запись текста, 'кодировка текста'

```python
file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла

# Очищеная страница записывается в список 'jokes' и в текстовый файл 'secondText.txt'
jokes = []
for joke in fun:
    jokes.append(clean_text(joke))
    file2.write(clean_text(joke) + '\n')

file2.close()  # закрывает файл
```