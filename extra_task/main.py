from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders import QuotesSpider1,QuotesSpider2

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSpider1)
    process.crawl(QuotesSpider2)
    process.start()

if __name__ == "__main__":
    main() #python main.py