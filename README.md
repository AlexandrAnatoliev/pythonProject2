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
    crean_text = str(text)
    while '<' in crean_text:
        crean_text = crean_text[:crean_text.find('<')] + crean_text[crean_text.find('>') + 1:]
    return crean_text
```