
from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class boulderLoader(ItemLoader):

    default_output_processor = TakeFirst()
    capacity_in = MapCompose(lambda x: x.split("%")[0])
