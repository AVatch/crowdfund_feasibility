import datetime

import scrapy
from kickstarter.items import KickstarterItem


class KickstarterSpider(scrapy.Spider):
    name = "kickstarter"
    allowed_domains = ["kickstarter.com"]
    
    reference_product = "https://www.kickstarter.com/projects/ysnet/shenmue-3/description"
    
    start_urls = [
        # product of interest
        reference_product,
        # reference products
        "https://www.kickstarter.com/projects/inxile/wasteland-2/description",
        "https://www.kickstarter.com/projects/1461411552/elite-dangerous/description",
        "https://www.kickstarter.com/projects/webeharebrained/shadowrun-returns/description",
        "https://www.kickstarter.com/projects/doublefine/double-fines-massive-chalice/description",
        "https://www.kickstarter.com/projects/larianstudios/divinity-original-sin/description",
        "https://www.kickstarter.com/projects/22cans/project-godus/description",
        "https://www.kickstarter.com/projects/stoic/the-banner-saga/description",
        "https://www.kickstarter.com/projects/thimbleweedpark/thimbleweed-park-a-new-classic-point-and-click-adv/description",
        "https://www.kickstarter.com/projects/ronimo/awesomenauts-starstorm/description",
        "https://www.kickstarter.com/projects/hiddenpath/defense-grid-2/description",
        "https://www.kickstarter.com/projects/375798653/superhot/description",
        "https://www.kickstarter.com/projects/hinterlandgames/the-long-dark-a-first-person-post-disaster-surviva/description"
    ]

    def extract_estimate_launch_time(self, pledges):
        """Given a selector pointing to the kickstarter pledges, we 
        do our best to estimate the delivery date of the project.
        
        The current implementation is overfitted to the video game example 
        where you typically will see the phrase "COPY OF X" where X is the 
        name of the game.
        
        @input: Selector to pledges
        @output: datetime
        """
        
        KEY = "copy of"
        estimated_time = None
        
        for pledge in pledges:
            pledge_amount = pledge.xpath('h2[contains(@class, "pledge__amount")]/text()').extract_first()
            pledge_info = pledge.xpath('div[contains(@class, "pledge__reward-description")]').extract_first()
            pledge_estimated_time = pledge.xpath('div[contains(@class, "pledge__extra-info")]//time/@datetime').extract_first()
            
            if KEY in pledge_info.lower():
                estimated_time = pledge_estimated_time
                break 
       
        return estimated_time

    def parse(self, response):
        """The main crawler parser
        """
        
        # Handle the project meta info
        project_name = response.xpath('//a[@class="hero__link"]/text()').extract_first()
        project_author =response.xpath('//div[@class="creator-name"]/div[@class="mobile-hide"]/a[contains(@class, "hero__link")]/text()').extract_first()
        
        # Handle the project backer and goal info
        project_stats = response.xpath('//div[@class="NS_projects__spotlight_stats"]')
        project_backers = project_stats.xpath('b/text()').extract_first()
        project_goal = None
        project_pledged = project_stats.xpath('span/text()').extract_first()
        if project_pledged:
            project_pledged = project_pledged.replace("$", "").replace(",", "")
        
        project_data_end_time = response.xpath('//span[@id="project_duration_data"]/@data-end_time').extract_first()
        project_data_duration = response.xpath('//span[@id="project_duration_data"]/@data-duration').extract_first()
        
        # Handle the project pledge info
        # get the rewards list to get the approximate release date
        project_pledges = response.xpath('//div[@class="pledge__info"]')
        project_estimated_time = self.extract_estimate_launch_time( project_pledges )
        
        project_item = KickstarterItem()
        project_item['project_url'] = response.url
        project_item['project_name'] = project_name
        project_item['project_author'] = project_author        
        project_item['backer_count'] = project_pledged
        project_item['estimated_release_date'] = project_estimated_time
        
        yield project_item
        