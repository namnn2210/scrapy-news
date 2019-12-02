# -*- coding: utf-8 -*-
import mysql.connector
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NewscrawlerPipeline(object):
    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()
    #
    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         passwd="ngocnam2210",
    #         database="scrapy"
    #     )
    #     self.curr = self.conn.cursor()
    #
    # def create_table(self):
    #     self.curr.execute(""" DROP TABLE IF EXISTS news_tb """)
    #     self.curr.execute(""" CREATE TABLE news_tb(
    #                     id INT AUTO_INCREMENT PRIMARY KEY,
    #                     title text,
    #                     href text,
    #                     raw_content text
    #     )""")
    #
    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     return item
    #
    # def store_db(self, item):
    #     self.curr.execute(""" INSERT INTO news_tb (title,href,raw_content) values (%s,%s,%s) """, (
    #         item['title'],
    #         item['href'],
    #         item['raw_content']
    #     ))
    #     self.conn.commit()

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn["mynews"]
        self.collection = db["news_tb"]

    def process_item(self, item, spider):
        cur = self.collection.find_one({"href": item["href"]})
        if cur is None:
            self.collection.insert(dict(item))
        return item


