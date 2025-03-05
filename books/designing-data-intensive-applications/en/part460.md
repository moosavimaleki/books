
For that reason, databases have long tried to hide concurrency issues from application developers by
providing transaction isolation. In theory, isolation should make your life easier by letting you
pretend that no concurrency is happening: serializable isolation means that the database
guarantees that transactions have the same effect as if they ran serially (i.e., one at a time,
without any concurrency). In practice, isolation is unfortunately not that simple. Serializable isolation has a performance
cost, and many databases don’t want to pay that price
[[8](ch07.html#Bailis2013tn)]. It’s therefore common for systems to use
weaker levels of isolation, which protect against some concurrency issues, but not all. Those
levels of isolation are much harder to understand, and they can lead to subtle bugs, but they are
nevertheless used in practice
[[23](ch07.html#Kleppmann2014ut)]. 
Concurrency bugs caused by weak transaction isolation are not just a theoretical problem. They have
caused substantial loss of money [[24](ch07.html#DAgosta2014uy), [25](ch07.html#bitcointhief2014wt)], led to investigation by financial auditors
[[26](ch07.html#Jorwekar2007uq_ch7)],
and caused customer data to be corrupted [[27](ch07.html#Melanson2014wq)].
A popular comment on revelations of such problems is “Use an ACID database if you’re handling
financial data!”—but that misses the point. Even many popular relational database systems (which
are usually considered “ACID”) use weak isolation, so they wouldn’t necessarily have prevented these
bugs from occurring.