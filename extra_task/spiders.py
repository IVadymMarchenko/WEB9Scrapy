import scrapy
import json

class QuotesSpider1(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com',

    ]
    quote=[]

    def parse(self,response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            self.quote.append({
                'tags': tags,
                'author':author,
                'quote':text
            })


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



    def closed(self, reason):
        with open('quotes.json', 'w',encoding='utf-8') as f:
            json.dump(self.quote, f,ensure_ascii=False,indent=4)


class QuotesSpider2(scrapy.Spider):
    name = "authors"
    start_urls = [
        'http://quotes.toscrape.com',

    ]
    author=[]

    def parse(self,response):
        for quote in response.css('div.quote'):
            link = quote.css('span small.author + a::attr(href)').get()
            if link:
                print(link)
                author_url = response.urljoin(link)
                yield scrapy.Request(author_url, callback=self.parse_author)

    def parse_author(self, response):
        author_info = response.css('div.author-details')
        for author in author_info:
            name = author.css('h3.author-title::text').get()
            data = author.css('span.author-born-date::text').get()
            location = author.css('span.author-born-location::text').get()
            description = author.css('div.author-description::text').get()


            self.author.append({
                'fullname': name,
                'data': data,
                'location': location,
                'description': description.strip()
            })

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_author)




    def closed(self, reason):
        with open('authors.json', 'w', encoding='utf-8') as f:
            json.dump(self.author, f, ensure_ascii=False, indent=4)
