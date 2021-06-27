import scrapy

class bookScraper(scrapy.Spider):
    name = "bookscrape"
    
    start_urls = [
            'http://books.toscrape.com/'
        ]
    def parse(self, response):
        all_books = response.css('.col-lg-3 ')
    
        for book in all_books:
            img_link = book.css('a img::attr(src)').extract()
            title = book.css('h3 a::attr(title)').extract()
            price = book.css('div.product_price p.price_color::text').extract()

            yield {
                'image_url' : img_link,
                'book_title' : title,
                'product_price' : price
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)