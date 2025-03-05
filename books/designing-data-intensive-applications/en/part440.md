
In the late 2000s, nonrelational (NoSQL) databases started gaining popularity. They aimed to
improve upon the relational status quo by offering a choice of new data models (see
[Chapter 2](ch02.html#ch_datamodels)), and by including replication ([Chapter 5](ch05.html#ch_replication)) and partitioning
([Chapter 6](ch06.html#ch_partitioning)) by default. Transactions were the main casualty of this movement: many of this
new generation of databases abandoned transactions entirely, or redefined the word to describe a
much weaker set of guarantees than had previously been understood
[[4](ch07.html#ACIDClaims)]. With the hype around this new crop of distributed databases, there emerged a popular belief that
transactions were the antithesis of scalability, and that any large-scale system would have to
abandon transactions in order to maintain good performance and high availability
[[5](ch07.html#Cook2009ui),
[6](ch07.html#Clarke2012vx)].
On the other hand, transactional guarantees are sometimes presented by database vendors as an
essential requirement for “serious applications” with “valuable data.” Both viewpoints are pure
hyperbole. The truth is not that simple: like every other technical design choice, transactions have advantages
and limitations. In order to understand those trade-offs, let’s go into the details of the
guarantees that transactions can provide—both in normal operation and in various extreme (but
realistic) circumstances.