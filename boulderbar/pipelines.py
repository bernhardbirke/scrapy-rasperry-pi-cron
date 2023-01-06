# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class toFloatPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # check is capacity present
        if adapter.get('capacity'):

            # converting the capacity to a float
            floatCapacity = float(adapter['capacity'])

            # converting the price from gbp to usd using our hard coded exchange rate
            adapter['capacity'] = round(floatCapacity, 2)

            return item

        else:
            # drop item if no capacity
            raise DropItem(f"Missing capacity in {item}")
