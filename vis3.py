import requests, csv
from bs4 import BeautifulSoup

dict0={}
with open("price01.csv", encoding='utf-8') as price_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(price_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            for char in row[1]:
                phrase = row[1]
                plist = list(phrase)
                if plist[1]=='\xa0':
                    plist.pop(1)
            new_phrase = ''.join(plist)
            dict0[row[0]] = ''.join(new_phrase.split())
        count += 1
    print(f'Всего в файле {count} строк.')

#цикл для перебора страниц сайта с анализами по артикулу
for i, k in dict0.items():
    
    #артикул подставляется в адрес сайта, чтобы выйти на нужную страницу исследования, и получаем запрос
    result = requests.get("https://helix.ru/catalog/item/{0}".format(i))
    #печать артикула
    print(i)
    #пРОБУЕМ ОТКРЫТЬ ФАЙЛ ЗАПИСАТЬ АРТИКУЛ И ЦЕНУ
    my_file = open("some.txt", "w")
    #присвоение переменной ответа от сервера со страницу
    src = result.content
    #парсинг
    soup = BeautifulSoup(src, 'lxml')
    #ищем данные по тегу
    links = soup.find_all('tr')
    #цикл поиска внутри тега <tr> слова "цена услуги", и если есть, то ищем тег <b>, внутри которой цифры с ценами
    for link in links:
        if "Цена услуги" in link.text:
            price_tag = soup.find_all('b')[2]
            price = price_tag.text
            print(price)
