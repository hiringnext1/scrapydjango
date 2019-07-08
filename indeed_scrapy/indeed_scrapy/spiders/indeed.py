# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from indeed_scrapy.items import IndeedScrapyItem


# -*- coding: utf-8 -*


class IndeedSpider(Spider):
    name = 'indeed'
    allowed_domains = ['indeed.co.in']

    def __init__(self, job='Sales', *args, **kwargs):
        super(IndeedSpider, self).__init__(*args, **kwargs)

        job = clean_job_string(job)
        self.start_urls = [f'https://www.indeed.co.in/jobs?q=&l=Gujarat&sort=date',
                           f'https://www.indeed.co.in/jobs?q=&l=Maharashtra',
                           ]

    def parse(self, response):

        links = response.xpath('//*[@class="title"]/a/@href').extract()

        for link in links:
            if 'company' or 'cmp' or 'jobs' or 'pagead' or 'rc' or 'clk' in link:
                absolute_link = response.urljoin(link)
                yield Request(absolute_link, callback=self.parse_job_offer)

        if not 'start' in response.url:
            link = response.url + '&start=10'
        else:
            link_first, link_second = response.url.split('&start=')
            link_second = int(link_second) + 10
            link = f'{link_first}&start={link_second}'

        yield Request(link, callback=self.parse)

    def parse_job_offer(self, response):
        # title = response.xpath('.//*[@class="cmp-company-name"]/text()').extract_first()
        # company_rating = response.xpath('.//*[@class="cmp-header-rating"]/span/text()').extract_first()
        # # city = response.xpath('.//*[@class="location"]/text()').extract_first()
        # job_url = response.url

        indeedscrapyitem = IndeedScrapyItem()

        # Job Title
        indeedscrapyitem['title'] = response.xpath(
            '//h3[contains(@class, "JobInfoHeader-title")]/text()').extract_first()

        # Company
        if response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[0] is '-':
            indeedscrapyitem['company'] = response.xpath('//*[contains(@class, '
                                                         '"jobsearch-InlineCompanyRating")]/div/a/text()').extract()[0]
        else:
            indeedscrapyitem['company'] = response.xpath('//*[contains(@class, '
                                                         '"jobsearch-InlineCompanyRating")]/div/text()').extract()[0]

        # Location
        if response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[0] is '-':
            indeedscrapyitem['city'] = \
                response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[1]

        elif response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[0] == indeedscrapyitem['company']:
            indeedscrapyitem['city'] = response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[2]

        else:
            indeedscrapyitem['city'] = \
                response.xpath('//*[contains(@class, "jobsearch-InlineCompanyRating")]/div/text()').extract()[0]

        # Salary
        if response.xpath(
                '//*[contains(@class, "jobsearch-JobMetadataHeader-item")]/span/text()').extract_first() == \
                indeedscrapyitem['city']:

            indeedscrapyitem['salary'] = 'Negotiable'

        else:

            indeedscrapyitem['salary'] = response.xpath(
                '//*[contains(@class, "jobsearch-JobMetadataHeader-item")]/span/text()').extract_first()

        # Job Description

        indeedscrapyitem['job_description'] = response.xpath('.//*[contains(@class, '
                                                             '"jobsearch-jobDescriptionText")]').extract()

        # Date Posted

        indeedscrapyitem['date_posted'] = response.xpath('//*[@class="jobsearch-JobMetadataFooter"]/text()').extract_first()

        indeedscrapyitem['job_url'] = response.url

        yield indeedscrapyitem


def clean_job_string(job_string):
    job_string = job_string.strip()
    job_string = job_string.replace(' ', '+')
    return job_string

