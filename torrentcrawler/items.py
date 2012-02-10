# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Torrent(Item):
	title = Field()
	size = Field()
	seeders = Field()
	leechers = Field()
	link = Field()
	desc = Field()