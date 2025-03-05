
There is one important question with regard to rebalancing that we have glossed over: does the
rebalancing happen automatically or manually? 
There is a gradient between fully automatic rebalancing (the system decides automatically when to
move partitions from one node to another, without any administrator interaction) and fully manual
(the assignment of partitions to nodes is explicitly configured by an administrator, and only
changes when the administrator explicitly reconfigures it). For example, Couchbase, Riak, and
Voldemort generate a suggested partition assignment automatically, but require an administrator to
commit it before it takes effect. Fully automated rebalancing can be convenient, because there is less operational work to do for
normal maintenance. However, it can be unpredictable. Rebalancing is an expensive operation, because
it requires rerouting requests and moving a large amount of data from one node to another. If it is
not done carefully, this process can overload the network or the nodes and harm the performance of
other requests while the rebalancing is in progress.