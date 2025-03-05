## Stream Joins 
In [Chapter 10](ch10.html#ch_batch) we discussed how batch jobs can join datasets by key, and how such joins form an
important part of data pipelines. Since stream processing generalizes data pipelines to incremental
processing of unbounded datasets, there is exactly the same need for joins on streams. However, the fact that new events can appear anytime on a stream makes joins on streams more
challenging than in batch jobs. To understand the situation better, let’s distinguish three
different types of joins: stream-stream joins, stream-table joins, and table-table joins
[[84](ch11.html#SamzaState)].
In the following sections we’ll illustrate each by example. ### Stream-stream join (window join) 
Say you have a search feature on your website, and you want to detect recent trends in searched-for
URLs. Every time someone types a search query, you log an event containing the query and the results
returned. Every time someone clicks one of the search results, you log another event
recording the click. In order to calculate the click-through rate for each URL in the search
results, you need to bring together the events for the search action and the click action, which are
connected by having the same session ID. Similar analyses are needed in advertising systems
[[85](ch11.html#Ananthanarayanan2013hw)].