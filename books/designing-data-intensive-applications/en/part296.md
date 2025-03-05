
No special hardware is required by a shared-nothing system, so you can use whatever machines have
the best price/performance ratio. You can potentially distribute data across multiple geographic
regions, and thus reduce latency for users and potentially be able to survive the loss of an entire
datacenter. With cloud deployments of virtual machines, you don’t need to be operating at Google
scale: even for small companies, a multi-region distributed architecture is now feasible. In this part of the book, we focus on shared-nothing architectures—not because they are
necessarily the best choice for every use case, but rather because they require the most caution
from you, the application developer. If your data is distributed across multiple nodes, you need to
be aware of the constraints and trade-offs that occur in such a distributed system—the database
cannot magically hide these from you. While a distributed shared-nothing architecture has many advantages, it usually also incurs
additional complexity for applications and sometimes limits the expressiveness of the data models
you can use. In some cases, a simple single-threaded program can perform significantly better than a
cluster with over 100 CPU cores
[[4](part02.html#McSherry2015vx_pt2)].
On the other hand, shared-nothing systems can be very powerful. The next few chapters go into
details on the issues that arise when data is distributed.