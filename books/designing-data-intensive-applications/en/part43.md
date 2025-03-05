However, the downside of approach 2 is that posting a tweet now requires a lot of extra work. On
average, a tweet is delivered to about 75 followers, so 4.6k tweets per second become
345k writes per second to the home timeline caches. But this average hides the fact that the
number of followers per user varies wildly, and some users have over 30 million followers. This
means that a single tweet may result in over 30 million writes to home timelines! Doing this in a
timely manner—Twitter tries to deliver tweets to followers within five seconds—is a significant
challenge. In the example of Twitter, the distribution of followers per user (maybe weighted by how often those
users tweet) is a key load parameter for discussing scalability, since it determines the fan-out
load. Your application may have very different characteristics, but you can apply similar principles
to reasoning about its load.