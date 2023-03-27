from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://www.citilink.ru/catalog/smartfony/APPLE/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code,"\n") # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('span', class_='ProductPrice__price ProductCardHorizontal__price__price')  # находим  контейнер с нужным классом
    price=[] # создаём список
    for data in block: # проходим циклом по содержимому контейнера
        price.append(data.find('span',class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price').text.strip().replace(' ', '')) # находим тег <span> и добавляем цену в список
    print(price) # вывод списка
    max=-1000   # определил min,max и среднюю цену
    min=500000
    n=0
    S=0
    for i in price:
        i=int(i)
        print(i)
        S=S+i
        if i>max:
            max=i
        if i<min:
            min=i
        n+=1
    sr=S/n
    print("\nСамый дешёвый айфон стоит ",min)
    print("\nСамый дорогой айфон стоит ",max)
    print("\nСредняя цена: ",sr)

