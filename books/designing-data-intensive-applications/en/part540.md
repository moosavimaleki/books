# Chapter 8. The Trouble with Distributed Systems

# Chapter 8. The Trouble with Distributed Systems Hey I just met you
The network’s laggy
But here’s my data
So store it maybe Kyle Kingsbury, Carly Rae Jepsen and the Perils of Network Partitions (2013) ![](assets/ch08-map-ebook.png) 
A recurring theme in the last few chapters has been how systems handle things going
wrong. For example, we discussed replica failover ([“Handling Node Outages”](ch05.html#sec_replication_failover)), replication lag
([“Problems with Replication Lag”](ch05.html#sec_replication_lag)), and concurrency control for transactions
([“Weak Isolation Levels”](ch07.html#sec_transactions_isolation_levels)). As we come to understand various edge cases that can occur
in real systems, we get better at handling them. However, even though we have talked a lot about faults, the last few chapters have still been too
optimistic. The reality is even darker. We will now turn our pessimism to the maximum and assume
that anything that can go wrong will go wrong.[i](ch08.html#idm140605761218736) (Experienced systems operators
will tell you that is a reasonable assumption. If you ask nicely, they might tell you some
frightening stories while nursing their scars of past battles.)