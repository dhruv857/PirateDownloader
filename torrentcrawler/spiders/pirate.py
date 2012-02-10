from scrapy.spider import BaseSpider
from scrapy import log 
from torrentcrawler.items import Torrent
from scrapy.selector import HtmlXPathSelector

def generate_urls():
	urls = []
	url = "http://thepiratebay.se/torrent/"
	for x in range(7000000,7999999):
		urls.append(url + str(x))
	return urls
	
class Pirate(BaseSpider):
	name = "pirate"
	allowed_domains = ["thepiratebay.se"]
	start_urls = generate_urls()
	

		
	def parse(self, response):
		if response.status != 404:
			torrent = Torrent()
			hxs = HtmlXPathSelector(response)
			torrent['title'] = hxs.select('//title/text()').extract()
			torrent['link'] = hxs.select("//div[@class='download']/a[contains(@href, 'magnet:')]/@href").extract()
			torrent['desc'] = hxs.select('//div[@class="nfo"]/pre/text()').extract()
			return torrent
			
			