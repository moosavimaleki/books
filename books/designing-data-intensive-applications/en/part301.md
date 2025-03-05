If the data that you’re replicating does not change over time, then replication is easy: you just
need to copy the data to every node once, and you’re done. All of the difficulty in replication lies
in handling changes to replicated data, and that’s what this chapter is about. We will discuss
three popular algorithms for replicating changes between nodes: single-leader, multi-leader, and
leaderless replication. Almost all distributed databases use one of these three approaches. They
all have various pros and cons, which we will examine in detail. There are many trade-offs to consider with replication: for example, whether to use synchronous or
asynchronous replication, and how to handle failed replicas. Those are often configuration options
in databases, and although the details vary by database, the general principles are similar across
many different implementations. We will discuss the consequences of such choices in this chapter. 
Replication of databases is an old topic—the principles haven’t changed much since they were
studied in the 1970s
[[1](ch05.html#Lindsay1979wv_ch5)],
because the fundamental constraints of networks have remained the same. However, outside of
research, many developers continued to assume for a long time that a database consisted of just one
node. Mainstream use of distributed databases is more recent. Since many application developers are
new to this area, there has been a lot of misunderstanding around issues such as eventual
consistency. In [“Problems with Replication Lag”](#sec_replication_lag) we will get more precise about eventual consistency and
discuss things like the read-your-writes and monotonic reads guarantees.