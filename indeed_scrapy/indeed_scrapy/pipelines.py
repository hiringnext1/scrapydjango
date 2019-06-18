# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# If you don't want to store the information in the localhost MongoDB Database, comment this pipeline

class IndeedPipeline(object):

    def process_item(self, item, spider):
        item.save()
        return item
