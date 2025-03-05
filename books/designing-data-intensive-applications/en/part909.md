### Message brokers compared to databases 
Some message brokers can even participate in two-phase commit protocols using XA or JTA (see
[“Distributed Transactions in Practice”](ch09.html#sec_consistency_dist_trans)). This feature makes them quite similar in nature to databases, although
there are still important practical differences between message brokers and databases: *  Databases usually keep data until it is explicitly deleted, whereas most message brokers
automatically delete a message when it has been successfully delivered to its consumers. Such
message brokers are not suitable for long-term data storage. *  Since they quickly delete messages, most message brokers assume that their working set is fairly
small—i.e., the queues are short. If the broker needs to buffer a lot of messages because the
consumers are slow (perhaps spilling messages to disk if they no longer fit in memory), each
individual message takes longer to process, and the overall throughput may degrade
[[6](ch11.html#Sackman2016ws)]. *  Databases often support secondary indexes and various ways of searching for data, while message
brokers often support some way of subscribing to a subset of topics matching some pattern. The
mechanisms are different, but both are essentially ways for a client to select the portion of the
data that it wants to know about.