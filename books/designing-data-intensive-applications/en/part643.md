
The best way of building fault-tolerant systems is to find some general-purpose abstractions with
useful guarantees, implement them once, and then let applications rely on those guarantees. This is
the same approach as we used with transactions in [Chapter 7](ch07.html#ch_transactions): by using a transaction, the
application can pretend that there are no crashes (atomicity), that nobody else is concurrently
accessing the database (isolation), and that storage devices are perfectly reliable (durability).
Even though crashes, race conditions, and disk failures do occur, the transaction abstraction hides
those problems so that the application doesn’t need to worry about them. 
We will now continue along the same lines, and seek abstractions that can allow an application to
ignore some of the problems with distributed systems. For example, one of the most important
abstractions for distributed systems is consensus: that is, getting all of the nodes to agree on
something. As we shall see in this chapter, reliably reaching consensus in spite of network faults
and process failures is a surprisingly tricky problem.