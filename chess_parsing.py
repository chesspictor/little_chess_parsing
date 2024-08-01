import requests
from datetime import datetime
import functions as fun

try:
    number = input('Верхняя дата: ')
except:
    print('Что-то пошло не так')
    number = ''
if not fun.is_date(number):
    current_datetime = datetime.now()
    number = current_datetime.strftime('%d-%m-%Y')
    print('Принята текущая дата')
number_first = ''
while not fun.is_date(number_first):
    try:
        number_first = input('Нижняя дата: ')
    except:
        print('Что-то пошло не так')
number = fun.date_to_week_number(number)
number_first = fun.date_to_week_number(number_first)
while number >= number_first:
    link = 'https://theweekinchess.com/zips/twic' + str(number) +'g.zip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    try:
        responce = requests.get(url=link, headers = headers)
        name = 'week' + str(number) + '.zip'
        with open(name, 'wb') as file:
            file.write(responce.content)
        number -= 1
    except:
        number = number_first
        print('Не удается установить соединение')
print('Парсинг закончен')
