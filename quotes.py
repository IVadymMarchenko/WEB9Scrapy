import requests
from bs4 import BeautifulSoup
import json

BASE_URL = 'https://quotes.toscrape.com'


def get_quotes(quote):
    # quotes_page = requests.get(url)
    # quotes_soup = BeautifulSoup(quotes_page.text, 'html.parser')
    name_tag = quote.find('div', class_='tags').find_all('a')
    author = quote.find('small', class_='author').text.strip()
    quote_text = quote.find('span', class_='text').text.strip()
    names_tag = [name.text.strip() for name in name_tag]

    all_quotes = {"tags": names_tag,
                  "author": author,
                  "quote": quote_text
                  }
    return all_quotes


def get_quote():
    page_number = 1
    all_data = []

    while True:
        page_url = f'{BASE_URL}/page/{page_number}'
        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        quotes = soup.findAll('div', class_='quote')

        if not quotes:
            break

        for quote in quotes:
            author_info = get_quotes(quote)
            all_data.append(author_info)



        page_number += 1
    return all_data



def save_quotes_to_json(quotes, filename):
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(quotes,file, ensure_ascii=False, indent=4)

# result = get_quote()
#
#
# save_quotes_to_json(result,'test.json')
