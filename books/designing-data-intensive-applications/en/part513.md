*  If transaction A wants to insert, update, or delete any object, it must first check whether either the old
or the new value matches any existing predicate lock. If there is a matching predicate lock held by
transaction B, then A must wait until B has committed or aborted before it can continue. The key idea here is that a predicate lock applies even to objects that do not yet exist in the
database, but which might be added in the future (phantoms). If two-phase locking includes predicate locks,
the database prevents all forms of write skew and other race conditions, and so its isolation
becomes serializable. ### Index-range locks 
Unfortunately, predicate locks do not perform well: if there are many locks by active transactions,
checking for matching locks becomes time-consuming. For that reason, most databases with 2PL
actually implement index-range locking (also known as next-key locking), which is a simplified
approximation of predicate locking [[41](ch07.html#Ports2012uw),
[50](ch07.html#Hellerstein2007be_ch7)].