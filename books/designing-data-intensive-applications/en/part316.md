*  Statements that have side effects (e.g., triggers, stored procedures, user-defined functions) may
result in different side effects occurring on each replica, unless the side effects are absolutely
deterministic. It is possible to work around those issues—for example, the leader can replace any
nondeterministic function calls with a fixed return value when the statement is logged so that the
followers all get the same value. However, because there are so many edge cases, other replication
methods are now generally preferred. 
Statement-based replication was used in MySQL before version 5.1. It is still sometimes used today,
as it is quite compact, but by default MySQL now switches to row-based replication (discussed shortly) if
there is any nondeterminism in a statement. VoltDB uses statement-based replication, and makes it
safe by requiring transactions to be deterministic
[[15](ch05.html#Hugg2015wp)]. ### Write-ahead log (WAL) shipping 
In [Chapter 3](ch03.html#ch_storage) we discussed how storage engines represent data on disk, and we found that usually
every write is appended to a log: