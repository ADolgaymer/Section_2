# ЗАДАНИЕ:

# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:

# Путь к файлу с текстом;
# Путь к файлу с результатом;
# Язык с которого перевести;
# Язык на который перевести (по-умолчанию русский).
# У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком. Функция должна взять каждый файл
# с текстом, перевести его на русский и сохранить результат в новом файле.

# Для переводов можно пользоваться API Yandex.Переводчик.

import requests

# ===FR====
def translate_it_fr(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    with open('FR.txt', encoding="utf8") as f:
      text = f.read()
    params = {
        'key': key,
        'lang': 'fr-ru',
        'text': text
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

tr_fr = translate_it_fr('text')
print(tr_fr)

with open('FR_translated.txt', 'w', encoding='utf8') as f:
  f.write(tr_fr)

# ===DE====

def translate_it_de(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    with open('DE.txt', encoding='utf8') as f:
      text = f.read()
    params = {
        'key': key,
        'lang': 'de-ru',
        'text': text
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

tr_de = translate_it_de('text')
print(tr_de)

with open('DE_translated.txt', 'w', encoding='utf8') as f:
  f.write(tr_de)

# ===ES====

def translate_it_es(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    with open('ES.txt', encoding='utf8') as f:
      text = f.read()
    params = {
        'key': key,
        'lang': 'es-ru',
        'text': text
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

tr_es = translate_it_es('text')
print(tr_es)

with open('ES_translated.txt', 'w', encoding='utf8') as f:
  f.write(tr_es)