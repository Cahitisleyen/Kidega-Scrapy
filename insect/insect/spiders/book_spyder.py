import scrapy


class BookSpyder(scrapy.Spider):

    name = "books"

    start_urls = [
        'https://kidega.com/kitap/bilisim-bilgisayar/tur?query=%22%22&page=1',
        'https://kidega.com/kitap/bilisim-bilgisayar/tur?query=%22%22&page=2',
        'https://kidega.com/kitap/bilisim-bilgisayar/tur?query=%22%22&page=3',
        'https://kidega.com/kitap/bilisim-bilgisayar/tur?query=%22%22&page=4',
        'https://kidega.com/kitap/bilisim-bilgisayar/tur?query=%22%22&page=5',
        
    ]


    def parse(self,response):

        books_name = response.css("div.title a.book-name::text").extract()
        book_author= response.css("div.authorArea a::text").extract()
        book_publisher = response.css("div.publisherArea a::text").extract()
        book_priceDiscount = response.css("div.itemFooter span::text").extract()
        book_priceFirst = response.css("div.itemFooter u::text").extract()
        book_priceLast = response.css("div.itemFooter b::text").extract()

       

        i = 0
        while (i < (len(book_author))):
            yield {
                "name": books_name[i],
                "author": book_author[i],
                "publisher": book_publisher[i],
                "priceDiscount": book_priceDiscount[i],
                "bookPriceLast": book_priceLast[i],
                "bookPriceFirst":book_priceFirst[i]
            }
            i +=1
      
       
