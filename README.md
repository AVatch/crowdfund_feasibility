# crowdfund_feasibility
A starting project to evaluate the time estimates for crowdfunded projects


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
