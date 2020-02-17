# -*- coding: utf-8 -*-
import scrapy
import re


class PscrapeSpider(scrapy.Spider):
    name = 'pscrape'
    start_urls = ['https://store.playstation.com/en-au/grid/STORE-MSF75508-FULLGAMES/1?direction=desc&gameContentType=games&platform=ps4&sort=release_date']

    def parse(self, response):
        for result in response.css("div.grid-cell__body"):
            title = result.css("div.grid-cell__title span::text").get()
            price = result.css("h3.price-display__price::text").get()
            cbargs = {'title': title, 'price': price}
            filtTitle = re.sub(r'[^a-zA-Z ]+', '', title).split(' ')
            urlTitle = 'https://www.metacritic.com/search/game/'+'%20'.join(filtTitle)+'/results?plats[72496]=1&search_type=advanced'
            yield scrapy.Request(urlTitle, callback=self.parseMetacritic, cb_kwargs=cbargs)
        if newlink := response.css('a.paginator-control__next.paginator-control__arrow-navigation--disabled::attr(href)').get() is None:
            nextlink = response.css(
                'a.paginator-control__next::attr(href)').get()
            yield response.follow(nextlink, callback=self.parse)

    def parseMetacritic(self, response, title, price):
        rating = 'unknown'
        for result in response.css('div.result_wrap'):
            rtitle = result.css('h3.product_title a::text').get().strip()
            rate = result.css('span.metascore_w::text').get()
            if rtitle == title:
                rating = rate
        yield { 'title' : title, 'rating' : rating, 'price' : price }
