*  We will start by looking at one of the strongest consistency models in common use,
linearizability, and examine its pros and cons. *  We’ll then examine the issue of ordering events in a distributed system
([“Ordering Guarantees”](#sec_consistency_ordering)), particularly around causality and total ordering. *  In the third section ([“Distributed Transactions and Consensus”](#sec_consistency_consensus)) we will explore how to atomically commit a
distributed transaction, which will finally lead us toward solutions for the consensus problem. # Linearizability 
In an eventually consistent database, if you ask two different replicas the same question at the
same time, you may get two different answers. That’s confusing. Wouldn’t it be a lot simpler if the
database could give the illusion that there is only one replica (i.e., only one copy of the data)?
Then every client would have the same view of the data, and you wouldn’t have to worry about
replication lag. This is the idea behind linearizability
[[6](ch09.html#Herlihy1990jq)]
(also known as atomic consistency
[[7](ch09.html#Lamport1986cg)],
strong consistency, immediate consistency, or external consistency
[[8](ch09.html#Gifford1981tu)]).
The exact definition of linearizability is quite subtle, and we will explore it in the rest of this
section. But the basic idea is to make a system appear as if there were only one copy of the data,
and all operations on it are atomic. With this guarantee, even though there may be multiple replicas
in reality, the application does not need to worry about them.