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

Looking at [Shenmue 3](https://www.kickstarter.com/projects/ysnet/shenmue-3)


