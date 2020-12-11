##Scrapy Project
##moviepoilers.com

##purpose of this file is the define how the site will be scraped
##follow links & parse contents to extract items

from scrapy import Spider
from scrapy import Request
from ScrapyPlots.items import ScrapyplotsItem

class SpoilersSpider(Spider):
   name = 'spoilers_spider'
   allowed_domains = ['themoviespoiler.com']
   start_urls = ['https://www.themoviespoiler.com']

   def parse(self, response):
      
## current hits

#      current_titles = response.xpath('//span[contains(@class, "box_office_title")]/text()').extract()
#      current_titles = list(map(lambda x: x.strip(), current_titles))
#      idx = -1
      
#      for url in response.xpath('//div[contains(@class, "box_office_item")]/a/@href').extract()[:3]:
#         idx += 1
#         if (len(url) <= 20):
#            continue
#         else:
#            print("url is {}".format(url))
#            yield Request(url=url, meta={'title' : current_titles[idx]}, callback=self.parse_spoiler_page)

## current hits

#      print('START CURRENT HITS')
#      archive_titles_top = response.xpath('//font[@size="1"]/a/text()').extract()
#      idx = -1
      
#      for url in response.xpath('//font[@size="1"]/a/@href').extract():
#         idx += 1
#         if (len(url) <= 20):
#            continue
#         else:
#            print("url is {}".format(url))
#            yield Request(url=url, meta={'title' : archive_titles_top[idx]}, callback=self.parse_spoiler_page)

## archive - part two
      print('START PART TWO')
      archive_titles_bot = response.xpath('//span[contains(@style, "xx-small")]/a/text()').extract()
      idx = -1
      
      for url in response.xpath('//span[contains(@style, "xx-small")]/a/@href').extract():
         idx += 1
         if (len(url) <= 20):
            continue
         else:
            print("URL is {}".format(url))
            full_url = response.urljoin(url)
            print("FULL URL is {}".format(url))
            yield Request(url=full_url, meta={'title' : archive_titles_bot[idx]}, callback=self.parse_spoiler_page)
      
#      for url in response.xpath('//span[contains(@style, "xx-small")]/a/@href').extract()[:3]:
#         idx += 1
#         if (len(url) <= 20):
#            continue
#         else:
#            print("url is {}".format(url))
#            url = "www.themoviespoiler.com/" + url
#            print("url is {}".format(url))
#            yield Request(url=url, meta={'title' : archive_titles_bot[idx]}, callback=self.parse_spoiler_page)
            
## extract the plots from the movie spoiler pages
            
   def parse_spoiler_page(self, response):
      print("PARSE SPOILER")
      try:
         plot = response.xpath('//p/text()').extract()[1:]
         plot = list(map(lambda x: x.strip(), plot))
         plot = " ".join(map(str, plot))
         print("plot is: " + plot)
         print("url for the above is " + response.url)
         print("TITLE for the above is " + response.meta['title'])
      except:
         plot = ""

      item = ScrapyplotsItem()
      item['url'] = response.url
      item['title'] = response.meta['title']
      item['spoiler'] = plot
      yield item



##      current_titles = response.xpath('//span[contains(@class, "box_office_title")]/text()').extract()
##      current_titles = list(map(lambda x: x.strip(), current_titles))

## archive part one

##      archive_urls_top = response.xpath('//font[@size="1"]/a/@href').extract()
##      archive_titles_top = response.xpath('//font[@size="1"]/a/text()').extract()

## archive part two

##      archive_urls_bot = response.xpath('//span[contains(@style, "xx-small")]/a/@href').extract()
##      archive_titles_bot = response.xpath('//span[contains(@style, "xx-small")]/a/text()').extract()

## combine the lists

##      spoilers_urls = current_urls + archive_urls_top + archive_urls_bot
##      spoilers_titles = current_titles + archive_titles_top + archive_titles_bot