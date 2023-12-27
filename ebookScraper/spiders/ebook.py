import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("################################")

        #######################################

        print(response.css("h3 a::text").get())

        ebooks = response.css("article")
        
        for ebook in ebooks:
            title = ebook.css("a::text").get()  #when taking inner tag use get method
            price = ebook.css("p.price_color::text").get()

            ##print(title, price)

            yield{
                "title": title,
                "price": price
            }







#######################################################
        #using Xpath
        #print( {"XPath"}, response.xpath("//h3/a/text()")[0])
        #print(response.xpath("//a[@title]").get())
        #print(response.xpath("//p[@class = 'price_color']").get())

        #print(response.css("a[href]").get())

        
            #title = ebooks.css("h3 a::attr(title)").get()
            #title = ebook.css("h3 a").attrib['title']
           
           