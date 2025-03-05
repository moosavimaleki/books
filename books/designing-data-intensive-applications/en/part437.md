A client may read data that doesn’t make sense because it has only partially been updated. *  Race conditions between clients can cause surprising bugs. In order to be reliable, a system has to deal with these faults and ensure that they don’t cause
catastrophic failure of the entire system. However, implementing fault-tolerance mechanisms is a lot
of work. It requires a lot of careful thinking about all the things that can go wrong, and a lot of
testing to ensure that the solution actually works. 
For decades, transactions have been the mechanism of choice for simplifying these issues. A
transaction is a way for an application to group several reads and writes together into a logical
unit. Conceptually, all the reads and writes in a transaction are executed as one operation: either
the entire transaction succeeds (commit) or it fails (abort, rollback). If it fails, the
application can safely retry. With transactions, error handling becomes much simpler for an
application, because it doesn’t need to worry about partial failure—i.e., the case where some
operations succeed and some fail (for whatever reason).