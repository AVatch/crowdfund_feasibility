# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KickstarterItem(scrapy.Item):
    # define the fields for your item here like:
    project_url = scrapy.Field()
    project_name = scrapy.Field()
    project_author = scrapy.Field()
    backer_count = scrapy.Field()
    
    start_date = scrapy.Field()
    estimated_release_date = scrapy.Field()
    actual_release_date = scrapy.Field()
    project_duration = scrapy.Field()
    