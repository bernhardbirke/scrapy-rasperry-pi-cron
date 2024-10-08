import scrapy
import time
from boulderbar.itemloaders import boulderLoader
from boulderbar.items import boulderItem


class boulderSpider(scrapy.Spider):
    name = "boulderbarhan"

    start_urls = [
        "https://flash-cloud.boulderbar.net/modules/bbext/CustomerCapacity.php?gym=han#no-back-button"]

    def parse(self, response):
        percentageLine = response.css('div.capacity_auslastung')
        boulderbarHan = boulderLoader(
            item=boulderItem(), selector=percentageLine)
        current_time = int(time.time())
        boulderbarHan.add_css('capacity', "center h2::text")
        boulderbarHan.add_value('date', current_time)
        yield boulderbarHan.load_item()
