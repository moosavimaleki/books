In this chapter, we will examine many examples of things that can go wrong, and explore the
algorithms that databases use to guard against those issues. We will go especially deep in the area
of concurrency control, discussing various kinds of race conditions that can occur and how
databases implement isolation levels such as read committed, snapshot isolation, and
serializability. This chapter applies to both single-node and distributed databases; in [Chapter 8](ch08.html#ch_distributed) we will
focus the discussion on the particular challenges that arise only in distributed systems. # The Slippery Concept of a Transaction 
Almost all relational databases today, and some nonrelational databases, support transactions. Most
of them follow the style that was introduced in 1975 by IBM System R, the first SQL database
[[1](ch07.html#Chamberlin1981im),
[2](ch07.html#Gray1976us),
[3](ch07.html#Eswaran1976uu)].
Although some implementation details have changed, the general idea has remained virtually the same
for 40 years: the transaction support in MySQL, PostgreSQL, Oracle, SQL Server, etc., is uncannily
similar to that of System R.