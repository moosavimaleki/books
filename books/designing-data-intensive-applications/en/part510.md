### Performance of two-phase locking 
The big downside of two-phase locking, and the reason why it hasn’t been used by everybody since the
1970s, is performance: transaction throughput and response times of queries are significantly worse
under two-phase locking than under weak isolation. This is partly due to the overhead of acquiring and releasing all those locks, but more importantly
due to reduced concurrency. By design, if two concurrent transactions try to do anything that may
in any way result in a race condition, one has to wait for the other to complete. Traditional relational databases don’t limit the duration of a transaction, because they are
designed for interactive applications that wait for human input. Consequently, when one transaction
has to wait on another, there is no limit on how long it may have to wait. Even if you make sure
that you keep all your transactions short, a queue may form if several transactions want to access
the same object, so a transaction may have to wait for several others to complete before it can do
anything.