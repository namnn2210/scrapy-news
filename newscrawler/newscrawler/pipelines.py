# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NewscrawlerPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn["mynews"]
        self.collection = db["news_tb"]

    def process_item(self, item, spider):
        cur = self.collection.find_one({"title": item["title"]})
        if cur is None:
            self.collection.insert(dict(item))
        return item
