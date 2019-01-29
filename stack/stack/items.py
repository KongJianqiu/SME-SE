# -*- coding: utf-8 -*-

# Define here the models for your scraped items


from scrapy.item import Item, Field


class StackItem(Item):
    title = Field()
    url = Field()
