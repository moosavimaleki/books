## Distributed Transactions in Practice 
Distributed transactions, especially those implemented with two-phase commit, have a mixed
reputation. On the one hand, they are seen as providing an important safety guarantee that would be
hard to achieve otherwise; on the other hand, they are criticized for causing operational problems,
killing performance, and promising more than they can deliver
[[81](ch09.html#Hohpe2005hn),
[82](ch09.html#Helland2007td_ch9),
[83](ch09.html#Oliver2011wt),
[84](ch09.html#Rahien2014uz)].
Many cloud services choose not to implement distributed transactions due to the operational
problems they engender [[85](ch09.html#Vasters2012wa),
[86](ch09.html#NServiceBus2015tf)]. 
Some implementations of distributed transactions carry a heavy performance penalty—for example,
distributed transactions in MySQL are reported to be over 10 times slower than single-node
transactions [[87](ch09.html#Wigginton2013vk)], so it is
not surprising when people advise against using them. Much of the performance cost inherent in
two-phase commit is due to the additional disk forcing (fsync) that is required for crash recovery
[[88](ch09.html#Spille2004ur)], and the additional network round-trips. However, rather than dismissing distributed transactions outright, we should examine them in some
more detail, because there are important lessons to be learned from them. To begin, we should be
precise about what we mean by “distributed transactions.” Two quite different types of distributed
transactions are often conflated: