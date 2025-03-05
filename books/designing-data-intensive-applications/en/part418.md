
This approach to rebalancing is used in Riak [[15](ch06.html#Riak2014)],
Elasticsearch [[24](ch06.html#Kuc2013uc)],
Couchbase [[10](ch06.html#CouchbaseAdmin)], and Voldemort
[[25](ch06.html#Voldemort2014)]. In this configuration, the number of partitions is usually fixed when the database is first set up
and not changed afterward. Although in principle it’s possible to split and merge partitions (see the
next section), a fixed number of partitions is operationally simpler, and so many fixed-partition
databases choose not to implement partition splitting. Thus, the number of partitions configured at
the outset is the maximum number of nodes you can have, so you need to choose it high enough to
accommodate future growth. However, each partition also has management overhead, so it’s
counterproductive to choose too high a number. Choosing the right number of partitions is difficult if the total size of the dataset is highly
variable (for example, if it starts small but may grow much larger over time). Since each partition
contains a fixed fraction of the total data, the size of each partition grows proportionally to the
total amount of data in the cluster. If partitions are very large, rebalancing and recovery from
node failures become expensive. But if partitions are too small, they incur too much overhead. The
best performance is achieved when the size of partitions is “just right,” neither too big nor too
small, which can be hard to achieve if the number of partitions is fixed but the dataset size
varies.