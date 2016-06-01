# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import datetime
import requests

GIANT_BOMB_API_KEY = os.environ.get('GIANT_BOMB_API_KEY')
GIANT_BOMB_API_URL = "http://www.giantbomb.com/api/search"

def giant_bomb_strategy(product_name):
    """Performs a lookup for the game by its
    product_name then returns the project 
    start and end date as described in the 
    giant bomb DB.
    
    If product is not find, returns (None,None)
    
    GiantBomb API Reference: http://www.giantbomb.com/forums/api-developers-3017/quick-start-guide-to-using-the-api-1427959/#14
    
    @input: product_name
    @output: (product_start_date, product_end_date)
    """    
    product_start_date = None
    product_end_date = None
    
    # Generated from POSTMAN
    querystring = {"query":product_name,"api_key":GIANT_BOMB_API_KEY,"resources":"game","format":"json"}

    headers = {
        'cache-control': "no-cache",
        'User-Agent': 'vatchinsky-scrapy-bot'
    }

    response = requests.request("GET", GIANT_BOMB_API_URL, headers=headers, params=querystring)

    if response.status_code == 200:
        
        query_results = response.json()['results']
        if query_results:
            # handle the response, for now let's be naive and accept the first search result as the correct game!
            result = query_results[0]
            
            print "#### %s : %s" % (result['name'], product_name)
            if result['date_added']:
                product_start_date = datetime.datetime.strptime(result['date_added'], '%Y-%m-%d %H:%M:%S')
            
            if result['original_release_date']:
                product_end_date = datetime.datetime.strptime(result['original_release_date'], '%Y-%m-%d %H:%M:%S')

    else:
        # TBD: Handle 500s, 403s, 404s, etc better
        print "BOO :'("

    return product_start_date, product_end_date
    


class KickstarterPipeline(object):
    def process_item(self, item, spider):
        """Uses the GiantBomb API to pull the release date
        of the game if it is released and calculate the 
        time it took the game to be released
        """
        product_start_date, product_end_date = giant_bomb_strategy( item["project_name"] )

        item['start_date'] = str(product_start_date)
        item['actual_release_date'] = str(product_end_date)
        
        return item
