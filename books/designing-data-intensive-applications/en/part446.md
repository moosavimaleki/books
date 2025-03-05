Isolation in the sense of ACID means that concurrently executing transactions are isolated from
each other: they cannot step on each other’s toes. The classic database textbooks formalize
isolation as serializability, which means that each transaction can pretend that it is the only
transaction running on the entire database. The database ensures that when the transactions have
committed, the result is the same as if they had run serially (one after another), even though in
reality they may have run concurrently
[[10](ch07.html#Bernstein1987va_ch7)]. ![ddia 0701](assets/ddia_0701.png) ###### Figure 7-1. A race condition between two clients concurrently incrementing a counter. 
However, in practice, serializable isolation is rarely used, because it carries a performance
penalty. Some popular databases, such as Oracle 11g, don’t even implement it. In Oracle there is an
isolation level called “serializable,” but it actually implements something called snapshot
isolation, which is a weaker guarantee than serializability
[[8](ch07.html#Bailis2013tn),
[11](ch07.html#Fekete2005ee)].
We will explore snapshot isolation and other forms of isolation in
[“Weak Isolation Levels”](#sec_transactions_isolation_levels).