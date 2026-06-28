import scrapy

class BooksSpider(scrapy.Spider):
    name = "movies"
    # This site is specifically designed to be scraped
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # 1. Follow links to individual book detail pages
        for book in response.css('article.product_pod'):
            link = book.css('h3 a::attr(href)').get()
            yield response.follow(link, callback=self.parse_book)
        
        # 2. Handle pagination (Go to next page automatically)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        # Extracting data using robust CSS selectors
        yield {
            'title': response.css('h1::text').get(),
            'price': response.css('p.price_color::text').get(),
            'stock': response.css('p.instock.availability::text').get().strip(),
            'rating': response.css('p.star-rating::attr(class)').get().split()[-1],
        }