In this chapter we will explore stronger consistency models that data systems may choose to provide.
They don’t come for free: systems with stronger guarantees may have worse performance or be less
fault-tolerant than systems with weaker guarantees. Nevertheless, stronger guarantees can be
appealing because they are easier to use correctly. Once you have seen a few different consistency
models, you’ll be in a better position to decide which one best fits your needs. There is some similarity between distributed consistency models and the hierarchy of transaction
isolation levels we discussed previously
[[4](ch09.html#Bailis2014vc_ch9),
[5](ch09.html#Viotti2016wr)]
(see [“Weak Isolation Levels”](ch07.html#sec_transactions_isolation_levels)).
But while there is some overlap, they are mostly independent concerns: transaction isolation is
primarily about avoiding race conditions due to concurrently executing transactions, whereas
distributed consistency is mostly about coordinating the state of replicas in the face of delays and
faults. This chapter covers a broad range of topics, but as we shall see, these areas are in fact deeply
linked: