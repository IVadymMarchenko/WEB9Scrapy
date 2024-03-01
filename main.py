from authors import get_authors,save_authors_to_json
from quotes import get_quote,save_quotes_to_json




def main():
    authors_data = get_authors()
    save_authors_to_json(authors_data,'author.json')

    quote_data=get_quote()
    save_quotes_to_json(quote_data,'quotes.json')

if __name__ == '__main__':
    main()#python main.py
    #этот скрипт создает файлы и записывает в них данные. После для того чтобы данные с файлов записать в базу нужно вызвать save_to_db.py


