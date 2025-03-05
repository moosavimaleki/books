Similar issues arise if you want to ensure that a bank account balance never goes negative, or that
you don’t sell more items than you have in stock in the warehouse, or that two people don’t
concurrently book the same seat on a flight or in a theater. These constraints all require there to
be a single up-to-date value (the account balance, the stock level, the seat occupancy) that all
nodes agree on. In real applications, it is sometimes acceptable to treat such constraints loosely (for example, if
a flight is overbooked, you can move customers to a different flight and offer them compensation for
the inconvenience). In such cases, linearizability may not be needed, and we will discuss such
loosely interpreted constraints in [“Timeliness and Integrity”](ch12.html#sec_future_integrity). However, a hard uniqueness constraint, such as the one you typically find in relational databases,
requires linearizability. Other kinds of constraints, such as foreign key or attribute constraints,
can be implemented without requiring linearizability
[[19](ch09.html#Bailis2014th_ch9)].