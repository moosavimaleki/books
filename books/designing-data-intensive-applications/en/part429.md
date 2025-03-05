Fast parallel execution of data warehouse queries is a specialized topic, and given the business
importance of analytics, it receives a lot of commercial interest. We will discuss some techniques for
parallel query execution in [Chapter 10](ch10.html#ch_batch). For a more detailed overview of techniques used in
parallel databases, please see the references
[[1](ch06.html#DeWitt1992fn_ch6),
[33](ch06.html#Babu2013gm_ch6)]. # Summary In this chapter we explored different ways of partitioning a large dataset into smaller subsets.
Partitioning is necessary when you have so much data that storing and processing it on a single
machine is no longer feasible. The goal of partitioning is to spread the data and query load evenly across multiple machines,
avoiding hot spots (nodes with disproportionately high load). This requires choosing a partitioning
scheme that is appropriate to your data, and rebalancing the partitions when nodes are added to or
removed from the cluster. We discussed two main approaches to partitioning: