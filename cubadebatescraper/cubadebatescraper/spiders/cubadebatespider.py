import scrapy
from cubadebatescraper.items import CubadebatescraperItem


class CubadebatespiderSpider(scrapy.Spider):
    
    #the name of the spider
    name = "cubadebatespider"
    allowed_domains = ["cubadebate.cu"]
    #the url of the first page that we will start scraping
    start_urls = ["http://www.cubadebate.cu/"]

    def parse(self, response):
        #Get all the divs that have the following css classes assigned.
        articles = response.css('.image_post,.bigimage_post,.gallery_post,.newspaper_post')
        intranet_item = CubadebatescraperItem()
        for article in articles:
            #here we put the data returned into the format we want to output for our csv or json file
            intranet_item['title']      = article.css('div.title a::text').get(),
            intranet_item['url']        = article.css('div.title a').attrib['href'],
            intranet_item['tags']       = article.css('h3.cat_title a::text').extract(),
            intranet_item['image_text'] = article.css('div.spoiler img::attr(src)').get(),
            intranet_item['shore_text'] = article.css('div.excerpt p::text').get(),
            yield intranet_item

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
           next_page_url = next_page
           yield response.follow(next_page_url, callback=self.parse)
