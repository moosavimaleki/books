In Dynamo-style databases, the parameters n, w, and r are typically configurable. A common
choice is to make n an odd number (typically 3 or 5) and to set w = r =
(n + 1) / 2 (rounded up). However, you can vary the numbers as you see fit.
For example, a workload with few writes and many reads may benefit from setting w = n and
r = 1. This makes reads faster, but has the disadvantage that just one failed node causes all
database writes to fail. ###### Note There may be more than n nodes in the cluster, but any given value is stored only on n
nodes. This allows the dataset to be partitioned, supporting datasets that are larger than you can fit
on one node. We will return to partitioning in [Chapter 6](ch06.html#ch_partitioning). The quorum condition, w + r > n, allows the system to tolerate unavailable nodes
as follows: