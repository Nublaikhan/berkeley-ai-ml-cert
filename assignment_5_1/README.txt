Assignment 5.1

The completed Jupiter Notebook with evaluations of the Bar and Coffee House coupon data
can be found at this link
https://github.com/Nublaikhan/berkeley-ai-ml-cert/blob/main/assignment_5_1/prompt.ipynb

Summary:
The notebook will evaluate the data, remove and fill missing data, and provide an analysis of two
coupon types.

Bar coupon:
The first coupon evaluated was the Bar coupon.  The Bar coupons were accepted 6.5%
of the time.  When a Bar coupon was offered, we can see that if the driver went to a
a bar less than 3 times per month they accepted the coupon 33% of the time.  If the
driver went more than 3 times per month, they only accepted 7.5% of the time.  We can
surmise that some people don't want to spend their money at bars but a coupon is enough
to convince them to go.  We then looked at age and more than one visit to a bar per
month.  We saw that if a driver was 25 or older with more than one bar visit per
month they accepted 14% of the time.  This accounts for more than half of the accepted
bar coupons.  Following the more than one visit to a bar per month data we added
passenger and occupation criteria.  Drivers who visited a bar more than once per
month, didn't have kids as passengers, and were not in farming, fishing, or forestry
accepted 19.5% of the time.  This accounts for close to 50% of all the accepted
Bar coupons.  Instead of occupation in the previous query we then added marital status.
We found that marital status doesn't impact the acceptance rate.  This also means
occupation doesn't either.

In short, overall we found that if the driver goes to the bar more than one
time a month they are more likely to accept a coupon. The drivers that go to the bar
often and don't have children passengers account for half of the accepted bar coupons.
Also, people that go to the bar often and are under 30 account for roughly 1/3 of the
accepted coupons.

Coffee House coupon:
The evaluation of the Coffee House coupon followed a similar path as the evaluation
of the Bar coupon.  Firstly, the Coffee House coupons were accepted at 50%.  This
is much higher than the Bar coupons.  The Coffee House coupons accounted for 27%
of all accepted coupons.  We then looked at how the driver's destination impacted
acceptance and found that drivers with no urgent destination accepted at a very
high rate.  We then took a look at how passenger type affected the acceptance.  We
can see that driver's who were alone were offered more coupons but driver's with
friends in the car accepted offered coupons at a higher rate.  Next we looked at
the time of day and saw that between 10AM and 2PM the acceptance rate was higher.
Next we took a look at temperature and found that when it was warmer the acceptance
rate was slightly higher.  Gender was the next dimension we looked at and found that
gender made no difference with acceptance.  We then looked at age and found that
younger people accepted more often than not.  We then looked at a combination of
high acceptance rate criteria.  We believed that if a driver was under 32, the time
was before 3p, and the driver was with friends we would have a high acceptance rate.
In this group, we see that they accept 63% of the time.

Recommendation:
For Coffee House coupons, younger drivers should be targeted before 3p.  If the
driver is with friends, then the acceptance of the coupon is increasingly likely.
If it is known they are with friends, then the coupon should be offered.