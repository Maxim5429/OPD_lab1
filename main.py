from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
url = 'https://www.citilink.ru/catalog/smartfony/APPLE/' # передаем необходимы URL адрес
page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
print(page.status_code) # смотрим ответ
