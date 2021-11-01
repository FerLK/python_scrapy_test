import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        count = 0
        for filmes in response.css('.titleColumn'):
            count += 1
            yield{
                'pos' : count,
                'titulos' : filmes.css('.titleColumn a::text').get(),
                'ano' : filmes.css('.secondaryInfo ::text').get()[1:-1],
                'nota' : response.css('strong::text').get()
            }

        pass
