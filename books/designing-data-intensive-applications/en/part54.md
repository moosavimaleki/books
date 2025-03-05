
Some systems are elastic, meaning that they can automatically add computing resources when they
detect a load increase, whereas other systems are scaled manually (a human analyzes the capacity and
decides to add more machines to the system). An elastic system can be useful if load is highly
unpredictable, but manually scaled systems are simpler and may have fewer operational surprises
(see [“Rebalancing Partitions”](ch06.html#sec_partitioning_rebalancing)). While distributing stateless services across multiple machines is fairly straightforward, taking
stateful data systems from a single node to a distributed setup can introduce a lot of additional
complexity. For this reason, common wisdom until recently was to keep your database on a single
node (scale up) until scaling cost or high-availability requirements forced you to make it
distributed. As the tools and abstractions for distributed systems get better, this common wisdom may change, at
least for some kinds of applications. It is conceivable that distributed data systems will become the
default in the future, even for use cases that don’t handle large volumes of data or traffic. Over the
course of the rest of this book we will cover many kinds of distributed data systems, and discuss how
they fare not just in terms of scalability, but also ease of use and maintainability.