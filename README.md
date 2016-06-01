# crowdfund_feasibility
A starting project to evaluate the time estimates for crowdfunded projects

## Motivation
Crowd funding projects can be immense undertakings. From organizing the funding campaign to actually executing, all factors require determination, commitement, and self discipline. It is no surprise then when crowdfunded projects slip their initial target release dates and countless headlines pop up hurting pre-orders and customer satisfaction and trust. 


The latest high profile example is the game "[Mighty Number 9](https://www.kickstarter.com/projects/mightyno9/mighty-no-9/description)" by Keiji Inafune, the creator of the super popular Mega Man franchise. The game suffered miltiple delays including delays in annoucning the delays ([source](http://gameranx.com/updates/id/47082/article/how-much-longer-does-the-mighty-no-9-community-need-to-wait/)).


These delays can come from multiple factors ranging from technical and financial issues, to simple life happenings such as divorces, marriages, new opportunities, etc. These events become even more likely in long term projects such as video games which can take multiple years to complete.


One simple thing that can be done in evaluating a project's development time is looking at comperable projects in addition to the resources the studio is in possession of. If for example you are working on a 2d platformer and a search shows that most 2d platformers take about 1.5 years to complete, then you should probably not be putting your delievery date for 0.75 years no matter how managable the project appears. Same goes for creating a 3d open world game. 


If a project appears and declares a strangely short turn around cycle, that should signal either that the project has been under development in stealth for a long time prior to announcement on the kickstarter page or that the studio has set unrealistic standards for itself to deliver the product on time.


This [scrapy](http://scrapy.org/) crawler is a first attempt in creating a tool which can look at a kickstarter project and its comperables and determine if the projected time estimate for the product is in line with prior delivered projects.
The interface is simple and the current implementation is overfitted to just Kickstarter campaigns + video games. Furthermore there is an assumption made that the campaigns being compared are already completed and funded. Otherwise if the campaign undergoing the logic of the spider should be slightly updated to account for the page differences. 

Scrapy was chosen due to its amazing and easy extensibility and scalability. Most of the logic happens in the ```pipelines.py``` file where we make use of the [GiantBomb API](http://www.giantbomb.com/api/) to get data for the games of interest. This can be extended in the future by incorporating searches against Twitter for topics such as "[X GAME] delayed" and the like to get further points. Furthermore assigning weights to the various games based off of funded budgets and teams or if the game is new IP or part of a franchise can make the model more reliable. 


But for now, this simply tells you whether or not the estimated production time of the game based off of the kickstarter campaign is in line with other projects which have already been delivered. 


## Running Things Quick Guide
### Setup - Install Dependencies
```
$ virtualenv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```

### Run scraper with default parameters
```
(env)$ cd kickstarter
(env)$ chmod +x crawl.sh
(env)$ ./crawl.sh
```

### Analyze data
```
(env)$ python analyze.py
```

### Sample Output

Looking at [Shenmue 3](https://www.kickstarter.com/projects/ysnet/shenmue-3) we see that the studio has given itself 900 days to complete the project while other projects have been completed in average of 630 or so days. This means that the studio is being overly cautious with the project or is aware that it will take a longer time than usual. 

![shenmue 3 results](https://raw.githubusercontent.com/AVatch/crowdfund_feasibility/master/kickstarter/sample_shenmue3.png)


On the other hand, looking at [Mighty No 9]() we see that the estimated delivery time fell short of what the average projects have taken. Even with the rough and big assumption taken in implementing this crawler, we see that the studio underestimated the time it would take to deliever the project which lines up with the current state of the project and its multiple delays. 

![mighty no 9 results](https://raw.githubusercontent.com/AVatch/crowdfund_feasibility/master/kickstarter/sample_mightyno9.png)

## Next Steps
Some of these were covered in the Motivation section, but here we go in further details. The most important change is to properly pick a representative sampling of other crowdsourced products which are related to the product of interest. In this implementation I simply picked released games which have been crowdfunded through kickstarter. 

Another optimization is to take into account other details such as funding goals, number of backers, studio reputation, studio size, and press coverage and interest. Also whether or not the product is part of an established franchise or a new IP can all have significant changes to the delivery times. 

Looking at whether or not the other comperables met their delivery times can also perhaps prove useful

Extending the data sources to include more than just GiantBomb, i.e. Twitter, etc. Furthermore generalizing this to other crowdfunding networks and other project topics.

The usual error handling, unit testing, and generalization all projects need


## Interesting Challenges That Were Encountered
Web crawling always tends to produce interesting edge cases and challenges due to the nature of the task.

For starters, KickStarter has a slightly different page structure for completed campaings versus undergoing campaigns. In this first pass, I am only looking at completed campaigns. 

Finding reference data to cross reference was a bit of an obstacle until I came across the GiantBomb API. With that though I encountered issues with not setting a proper User-Agent. If the User-Agent was not properly configured the API would 403. 

Using the API I encountered issues with parsing the search results. Examples include "Shemue 3" (on Kickstarter) vs "Shenmue III" on the GiantBomb API. I just made the assumption they are super good with search and am taking the first result. This should be improved in future iterations with a robust compare function which goes through the /api/search results and finds the appropriate project.

Figuring out the estimated delivery date was hard since this was data not explicitely cited on the Kickstarter campaign page. This was not funding goal date, but instead the date the project was complete. For this I iterated across the Perks section adn looked in the description to find "COPY OF" which i used as an indicator that the Perk said something along the lines of "You will get a copy of game if you pay this much" This simple assumption proved pretty robust and useful. I would then take the perk delivery date as the estimate product delivery date. This though can also use a more robust improvement. One example which can counter my assumption is that the perk gives a copy of Beta access of the game. Altough for my purpose I will consider that as a delivery date. 
