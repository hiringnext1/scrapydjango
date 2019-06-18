# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy
from sampledjango.models import IndeedJobs
from scrapy_djangoitem import DjangoItem


class IndeedScrapyItem(DjangoItem):
    django_model = IndeedJobs
