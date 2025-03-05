Instead of loading the small join input into an in-memory hash table, an alternative is to store the
small join input in a read-only index on the local disk
[[42](ch10.html#Monsch2015vb)].
The frequently used parts of this index will remain in the operating system’s page cache, so this
approach can provide random-access lookups almost as fast as an in-memory hash table, but without
actually requiring the dataset to fit in memory. ### Partitioned hash joins 
If the inputs to the map-side join are partitioned in the same way, then the hash join approach can
be applied to each partition independently. In the case of [Figure 10-2](#fig_batch_join_example), you might
arrange for the activity events and the user database to each be partitioned based on the last
decimal digit of the user ID (so there are 10 partitions on either side). For example, mapper 3
first loads all users with an ID ending in 3 into a hash table, and then scans over all the activity
events for each user whose ID ends in 3.