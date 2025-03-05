A transaction commit must be irrevocable—you are not allowed to change your mind and retroactively
abort a transaction after it has been committed. The reason for this rule is that once data has been
committed, it becomes visible to other transactions, and thus other clients may start relying on
that data; this principle forms the basis of read committed isolation, discussed in
[“Read Committed”](ch07.html#sec_transactions_read_committed). If a transaction was allowed to abort after committing, any
transactions that read the committed data would be based on data that was retroactively declared not
to have existed—so they would have to be reverted as well. 
(It is possible for the effects of a committed transaction to later be undone by another,
compensating transaction [[73](ch09.html#Gray1981wi_ch9),
[74](ch09.html#GarciaMolina1987ca_ch9)].
However, from the database’s point of view this is a separate transaction, and thus any
cross-transaction correctness requirements are the application’s problem.) ### Introduction to two-phase commit 
Two-phase commit is an algorithm for achieving atomic transaction commit across multiple
nodes—i.e., to ensure that either all nodes commit or all nodes abort. It is a classic algorithm
in distributed databases [[13](ch09.html#Bernstein1987va_ch9),
[35](ch09.html#Lindsay1979wv_ch9),
[75](ch09.html#Mohan1986hh)]. 2PC is used
internally in some databases and also made available to applications in the form of XA transactions
[[76](ch09.html#XASpec1991vk),
[77](ch09.html#Spille2004vr)] (which are supported by the Java Transaction API, for example)
or via WS-AtomicTransaction for SOAP web services
[[78](ch09.html#Neto2008be),
[79](ch09.html#Johnson2004hl)].