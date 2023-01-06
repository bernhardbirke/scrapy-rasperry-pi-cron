import scrapy
import time
from boulderbar.itemloaders import boulderLoader
from boulderbar.items import boulderItem


class boulderSpider(scrapy.Spider):
    name = "boulderbarhbf"

    start_urls = [
        "https://shop.boulderbar.net:8080/modules/bbext/CustomerCapacity.php?gym=hbf"]

    def parse(self, response):
        percentageLine = response.css('div.capacity_auslastung')
        boulderbarHbf = boulderLoader(
            item=boulderItem(), selector=percentageLine)
        current_time = int(time.time())
        boulderbarHbf.add_css('capacity', "center h2::text")
        boulderbarHbf.add_value('date', current_time)
        yield boulderbarHbf.load_item()
