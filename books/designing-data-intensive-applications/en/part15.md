# Outline of This Book This book is arranged into three parts: 1.  In [Part I](part01.html#part_foundations), we discuss the fundamental ideas that underpin the design of
data-intensive applications. We start in [Chapter 1](ch01.html#ch_introduction) by discussing what we’re actually
trying to achieve: reliability, scalability, and maintainability; how we need to think about
them; and how we can achieve them. In [Chapter 2](ch02.html#ch_datamodels) we compare several different data
models and query languages, and see how they are appropriate to different situations. In
[Chapter 3](ch03.html#ch_storage) we talk about storage engines: how databases arrange data on disk so that we
can find it again efficiently. [Chapter 4](ch04.html#ch_encoding) turns to formats for data encoding (serialization)
and evolution of schemas over time. 2.  In [Part II](part02.html#part_distributed_data), we move from data stored on one machine to data that is
distributed across multiple machines. This is often necessary for scalability, but brings with it
a variety of unique challenges. We first discuss replication ([Chapter 5](ch05.html#ch_replication)),
partitioning/sharding ([Chapter 6](ch06.html#ch_partitioning)), and transactions ([Chapter 7](ch07.html#ch_transactions)). We then
go into more detail on the problems with distributed systems ([Chapter 8](ch08.html#ch_distributed)) and what it
means to achieve consistency and consensus in a distributed system ([Chapter 9](ch09.html#ch_consistency)).