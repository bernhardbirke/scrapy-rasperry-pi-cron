import scrapy
import time
from boulderbar.itemloaders import boulderLoader
from boulderbar.items import boulderItem


class boulderSpider(scrapy.Spider):
    name = "boulderbarstp"

    start_urls = [
        "https://flash-cloud.boulderbar.net/modules/bbext/CustomerCapacity.php?gym=stp#no-back-button"]

    def parse(self, response):
        percentageLine = response.css('div.capacity_auslastung')
        boulderbarHbf = boulderLoader(
            item=boulderItem(), selector=percentageLine)
        current_time = int(time.time())
        boulderbarHbf.add_css('capacity', "center h2::text")
        boulderbarHbf.add_value('date', current_time)
        yield boulderbarHbf.load_item()
