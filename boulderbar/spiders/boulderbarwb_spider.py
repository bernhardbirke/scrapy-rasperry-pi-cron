import scrapy
import time
from boulderbar.itemloaders import boulderLoader
from boulderbar.items import boulderItem


class boulderSpider(scrapy.Spider):
    name = "boulderbarwb"

    start_urls = [
        "https://flash-cloud.boulderbar.net/modules/bbext/CustomerCapacity.php?gym=wb#no-back-button"
    ]

    def parse(self, response):
        percentageLine = response.css("div.capacity_auslastung")
        boulderbarWb = boulderLoader(item=boulderItem(), selector=percentageLine)
        current_time = int(time.time())
        boulderbarWb.add_css("capacity", "center h2::text")
        boulderbarWb.add_value("date", current_time)
        yield boulderbarWb.load_item()
