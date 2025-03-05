*  Counting the number of records in each group (like in our example of counting page views,
which you would express as a COUNT(*) aggregation in SQL) *  Adding up the values in one particular field (SUM(fieldname)) in SQL *  Picking the top k records according to some ranking function The simplest way of implementing such a grouping operation with MapReduce is to set up the mappers
so that the key-value pairs they produce use the desired grouping key. The partitioning and sorting
process then brings together all the records with the same key in the same reducer. Thus, grouping
and joining look quite similar when implemented on top of MapReduce. 
Another common use for grouping is collating all the activity events for a particular user session,
in order to find out the sequence of actions that the user took—a process called sessionization
[[37](ch10.html#Grover2015tl)].
For example, such analysis could be used to work out whether users who were shown a new version of
your website are more likely to make a purchase than those who were shown the old version (A/B
testing), or to calculate whether some marketing activity is worthwhile.