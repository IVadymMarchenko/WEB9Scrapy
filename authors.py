import requests
from bs4 import BeautifulSoup
import json

BASE_URL='https://quotes.toscrape.com'

def get_author(author_url):
    author_page = requests.get(author_url)# робим запит
    author_soup = BeautifulSoup(author_page.text, 'html.parser')#
    author_name=author_soup.find('h3').text.strip()#имья автора
    author_birthdate=author_soup.find('span',class_='author-born-date').text.strip()#день народженя автора
    author_birthplace=author_soup.find('span',class_='author-born-location').text.strip()#
    author_description=author_soup.find('div',class_='author-description').text.strip()

    author_info={'fullname': author_name,
                 'born_date': author_birthdate,
                 'born_location':author_birthplace,
                 'description':author_description}
    return author_info


def get_authors():
    page_number=1
    all_data=[]

    while True:
        page_url=f'{BASE_URL}/page/{page_number}'
        page=requests.get(page_url)
        soup=BeautifulSoup(page.text,'html.parser')
        quotes=soup.findAll('div',class_='quote')

        if not quotes:
            break

        for quote in quotes:
            text=quote.find('span',class_='text').text.strip()
            author_url=quote.find('a')['href']
            author_info=get_author(BASE_URL+author_url)

            all_data.append(author_info)
        page_number+=1
    return all_data

def save_authors_to_json(quotes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(quotes, file, ensure_ascii=False, indent=4)

# # Скрапим цитаты
# all_quotes = get_quote()
# # Сохраняем цитаты в JSON файл
# save_authors_to_json(all_quotes, 'author.json')








