# crowdfund_feasibility
A starting project to evaluate the time estimates for crowdfunded projects

## Motivation
Crowd funding projects can be immense undertakings. From organizing the funding campaign to actually executing, all factors require determination, commitement, and self discipline. It is no surprise then when crowdfunded projects slip their initial target release dates and countless headlines pop up hurting pre-orders and customer satisfaction and trust. 


The latest high profile example is the game "[Mighty Number 9](https://www.kickstarter.com/projects/mightyno9/mighty-no-9/description)" by Keiji Inafune, the creator of the super popular Mega Man franchise. The game suffered miltiple delays including delays in annoucning the delays ([source](http://gameranx.com/updates/id/47082/article/how-much-longer-does-the-mighty-no-9-community-need-to-wait/)).


These delays can come from multiple factors ranging from techincal and financial issues, to simple life happenings such as divorces, marriages, new opportunities, etc. These events become even more likely in long term projects such as video games which can take multiple years to complete.


One simple thing that can be done in evaluating a project's development time is looking at comperable projects in addition to the resources the studio is in possession of. If for example you are working on a 2d platformer and a search shows that most 2d platformers take about 1.5 years to complete, then you should probably not be putting your delievery date for 0.75 years no matter how managable the project appears. Same goes for creating a 3d open world game. 


If a project appears and declares a strangely short turn around cycle, that should signal either that the project has been under development in stealth for a long time prior to announcement on the kickstarter page or that the studio has set unrealistic standards for itself to deliver the product on time.


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
