import json
import datetime

PRODUCT_OF_INTEREST_URL = "https://www.kickstarter.com/projects/ysnet/shenmue-3/description"

product_of_interest = {}
product_comparables = []

def clean_up_dates(d):
    if d == 'None' or d == None:
        return '0000-00-00'
    return d.split(' ')[0] # we really only care about these sig figs not the hours and such

def calculate_duration(d1, d2):
    """Calculates the difference in time
    """
    d1 = datetime.datetime.strptime(clean_up_dates(d1), '%Y-%m-%d') 
    d2 = datetime.datetime.strptime(clean_up_dates(d2), '%Y-%m-%d')
    
    return d2 - d1
    

def print_products( product_of_interest, product_comparables ):
    """Prints the products for debugging
    """
    print "Announcement\t\t\tEst Release\t\tAct Release\t\tTitle"
    
    print "="*100
    
    print "%s\t\t%s\t\t%s\t\t%s" % ( clean_up_dates(product_of_interest['start_date']),
                                     clean_up_dates(product_of_interest['estimated_release_date']),
                                     clean_up_dates(product_of_interest['actual_release_date']),
                                     product_of_interest['project_name'] )
    
    print "="*100
    
    for product in product_comparables:
        print "%s\t\t%s\t\t%s\t\t%s" % ( clean_up_dates(product['start_date']),
                                         clean_up_dates(product['estimated_release_date']),
                                         clean_up_dates(product['actual_release_date']),
                                         product['project_name'] )

def organize_data(data):
    """populates the product_of_interest and product_comparables
    """
    interest = {}
    comperables = []
    for entry in data:
        if entry['project_url'] == PRODUCT_OF_INTEREST_URL:
            interest = entry
        else:
            comperables.append(entry)
    return interest, comperables


def calculate_average_project_time(projects):
    """given a list of projects returns the average and standard deviation
    of time it took for the project to complete 
    """
    durations = []
    
    for project in projects:
        durations.append( calculate_duration( project['start_date'], project['actual_release_date'] ) )

    return sum(durations, datetime.timedelta()) / len(durations)
    
def calculate_proposed_time(project):
    return calculate_duration( project['start_date'], project['estimated_release_date'] )

if __name__=='__main__':
    with open('projects.json') as data_file:
        data = json.load(data_file)
    product_of_interest, product_comparables = organize_data(data)
    print_products( product_of_interest, product_comparables )
    
    print "Comperables Average Time:\t%s" % str(calculate_average_project_time( product_comparables ))
    print "Product of Interest Time:\t%s" % str(calculate_proposed_time( product_of_interest )) 

