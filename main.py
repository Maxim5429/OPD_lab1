from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
url = 'https://www.citilink.ru/catalog/smartfony/APPLE/' # передаем необходимы URL адрес
page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
print(page.status_code) # смотрим ответ
soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
block = soup.findAll('span', class_='ProductPrice__price ProductCardHorizontal__price__price')  # находим  контейнер с нужным классом
price=[]
for data in block: # проходим циклом по содержимому контейнера
    price.append(data.find('span',class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price').text.strip()) # находим тег <span> и добавляем цену в список
for i in price:
    print(i)
